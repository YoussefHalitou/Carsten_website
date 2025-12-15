/**
 * AJAX Navigation Handler for Persistent Chatbot
 * Prevents full page reloads while maintaining chatbot state and conversation
 */

(function() {
    'use strict';
    
    // Configuration
    const CONFIG = {
        contentSelector: 'body > *:not(#medical-chatbot-container)',
        chatbotSelector: '#medical-chatbot-container',
        excludeLinks: ['mailto:', 'tel:', 'http://', 'https://'],
        animationDuration: 200
    };
    
    // Track if we're currently loading
    let isLoading = false;
    
    // Store the original chatbot container
    let chatbotContainer = null;
    
    /**
     * Initialize the navigation handler
     */
    function init() {
        // Save reference to chatbot container
        chatbotContainer = document.querySelector(CONFIG.chatbotSelector);
        
        // Intercept all link clicks
        document.addEventListener('click', handleLinkClick, true);
        
        // Handle browser back/forward buttons
        window.addEventListener('popstate', handlePopState);
        
        console.log('✓ AJAX Navigation initialized - Chatbot will persist across pages');
    }
    
    /**
     * Handle link clicks
     */
    function handleLinkClick(e) {
        const link = e.target.closest('a');
        
        if (!link || !link.href) return;
        
        // Check if link should be handled by AJAX
        if (!shouldHandleLink(link)) return;
        
        // Prevent default navigation
        e.preventDefault();
        e.stopPropagation();
        
        // Navigate to the page
        navigateToPage(link.href);
    }
    
    /**
     * Check if link should be handled by AJAX navigation
     */
    function shouldHandleLink(link) {
        const href = link.getAttribute('href');
        
        if (!href) return false;
        
        // Don't handle external links
        if (CONFIG.excludeLinks.some(prefix => href.startsWith(prefix) && !href.startsWith(window.location.origin))) {
            return false;
        }
        
        // Don't handle hash links (anchors)
        if (href.startsWith('#')) {
            return false;
        }
        
        // Don't handle links with target="_blank"
        if (link.target === '_blank') {
            return false;
        }
        
        // Don't handle downloads
        if (link.hasAttribute('download')) {
            return false;
        }
        
        // Only handle same-origin links
        try {
            const linkUrl = new URL(href, window.location.origin);
            return linkUrl.origin === window.location.origin && href.endsWith('.html');
        } catch (e) {
            return false;
        }
    }
    
    /**
     * Navigate to a new page using AJAX
     */
    async function navigateToPage(url) {
        if (isLoading) return;
        
        isLoading = true;
        
        try {
            // Show loading state (optional)
            document.body.classList.add('page-loading');
            
            // Fetch the new page
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const html = await response.text();
            
            // Parse the HTML
            const parser = new DOMParser();
            const newDoc = parser.parseFromString(html, 'text/html');
            
            // Update the page
            updatePage(newDoc, url);
            
            // Update browser history
            window.history.pushState({ url: url }, '', url);
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
        } catch (error) {
            console.error('Navigation error:', error);
            // Fallback to normal navigation
            window.location.href = url;
        } finally {
            isLoading = false;
            document.body.classList.remove('page-loading');
        }
    }
    
    /**
     * Update page content without destroying chatbot
     */
    function updatePage(newDoc, url) {
        // Update title
        document.title = newDoc.title;
        
        // Update meta tags
        updateMetaTags(newDoc);
        
        // Save chatbot container reference
        const savedChatbot = chatbotContainer;
        
        // Get all body children except chatbot
        const currentContent = Array.from(document.body.children).filter(
            el => el.id !== 'medical-chatbot-container'
        );
        
        // Get new content (everything except chatbot)
        const newContent = Array.from(newDoc.body.children).filter(
            el => el.id !== 'medical-chatbot-container'
        );
        
        // Fade out current content
        currentContent.forEach(el => {
            el.style.opacity = '0';
            el.style.transition = `opacity ${CONFIG.animationDuration}ms`;
        });
        
        // Wait for fade out
        setTimeout(() => {
            // Remove old content
            currentContent.forEach(el => el.remove());
            
            // Add new content
            newContent.forEach(el => {
                const clone = el.cloneNode(true);
                document.body.insertBefore(clone, savedChatbot);
            });
            
            // Ensure chatbot is still at the end
            if (savedChatbot && !document.body.contains(savedChatbot)) {
                document.body.appendChild(savedChatbot);
            }
            
            // Reinitialize any scripts that need it
            reinitializeScripts();
            
            // Fade in new content
            setTimeout(() => {
                document.querySelectorAll('body > *:not(#medical-chatbot-container)').forEach(el => {
                    el.style.opacity = '1';
                });
            }, 50);
            
        }, CONFIG.animationDuration);
    }
    
    /**
     * Update meta tags
     */
    function updateMetaTags(newDoc) {
        // Update description
        const newDescription = newDoc.querySelector('meta[name="description"]');
        const oldDescription = document.querySelector('meta[name="description"]');
        if (newDescription && oldDescription) {
            oldDescription.setAttribute('content', newDescription.getAttribute('content'));
        }
        
        // Update keywords
        const newKeywords = newDoc.querySelector('meta[name="keywords"]');
        const oldKeywords = document.querySelector('meta[name="keywords"]');
        if (newKeywords && oldKeywords) {
            oldKeywords.setAttribute('content', newKeywords.getAttribute('content'));
        }
    }
    
    /**
     * Reinitialize scripts after content update
     */
    function reinitializeScripts() {
        // Reinitialize menu toggle if it exists
        if (typeof window.toggleMenu === 'function') {
            // Menu handler is already defined in script.js
        }
        
        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('pageContentUpdated'));
    }
    
    /**
     * Handle browser back/forward buttons
     */
    function handlePopState(e) {
        if (e.state && e.state.url) {
            navigateToPage(e.state.url);
        } else {
            // Fallback to current URL
            navigateToPage(window.location.href);
        }
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Store initial state
    window.history.replaceState({ url: window.location.href }, '', window.location.href);
    
})();
