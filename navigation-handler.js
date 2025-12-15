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
        
        console.log('🖱️ Link clicked:', link.href);
        
        // Check if link should be handled by AJAX
        if (!shouldHandleLink(link)) {
            console.log('⏭️ Allowing default navigation');
            return;
        }
        
        // Prevent default navigation
        e.preventDefault();
        e.stopPropagation();
        
        console.log('🚀 Starting AJAX navigation to:', link.href);
        
        // Navigate to the page
        navigateToPage(link.href);
    }
    
    /**
     * Check if link should be handled by AJAX navigation
     */
    function shouldHandleLink(link) {
        const href = link.getAttribute('href');
        
        console.log('🔍 Checking link:', href);
        
        if (!href) {
            console.log('❌ No href');
            return false;
        }
        
        // Don't handle hash links (anchors)
        if (href.startsWith('#')) {
            console.log('❌ Hash link');
            return false;
        }
        
        // Don't handle links with target="_blank"
        if (link.target === '_blank') {
            console.log('❌ Target blank');
            return false;
        }
        
        // Don't handle downloads
        if (link.hasAttribute('download')) {
            console.log('❌ Download link');
            return false;
        }
        
        // Don't handle mailto: and tel: links
        if (href.startsWith('mailto:') || href.startsWith('tel:')) {
            console.log('❌ Mailto/tel link');
            return false;
        }
        
        // Only handle same-origin links that are HTML pages
        try {
            const linkUrl = new URL(href, window.location.href);
            const isHtmlPage = linkUrl.pathname.endsWith('.html') || linkUrl.pathname === '/' || linkUrl.pathname === '';
            const isSameOrigin = linkUrl.origin === window.location.origin;
            
            console.log('Link analysis:', {
                url: linkUrl.href,
                pathname: linkUrl.pathname,
                isHtmlPage,
                isSameOrigin
            });
            
            if (isSameOrigin && isHtmlPage) {
                console.log('✅ Will handle with AJAX');
                return true;
            } else {
                console.log('❌ External or non-HTML');
                return false;
            }
        } catch (e) {
            console.log('❌ URL parse error:', e);
            return false;
        }
    }
    
    /**
     * Navigate to a new page using AJAX
     */
    async function navigateToPage(url) {
        if (isLoading) {
            console.log('⏸️ Already loading, skipping');
            return;
        }
        
        isLoading = true;
        console.log('📡 Fetching page:', url);
        
        try {
            // Show loading state (optional)
            document.body.classList.add('page-loading');
            
            // Fetch the new page
            const response = await fetch(url);
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const html = await response.text();
            console.log('✅ Page fetched, length:', html.length);
            
            // Parse the HTML
            const parser = new DOMParser();
            const newDoc = parser.parseFromString(html, 'text/html');
            console.log('📄 Page parsed, title:', newDoc.title);
            
            // Update the page
            updatePage(newDoc, url);
            
            // Update browser history
            window.history.pushState({ url: url }, '', url);
            console.log('🔄 History updated');
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            console.log('✨ Navigation complete!');
            
        } catch (error) {
            console.error('❌ Navigation error:', error);
            console.log('↩️ Falling back to normal navigation');
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
        console.log('🔄 Updating page content...');
        
        // Update title
        document.title = newDoc.title;
        console.log('📝 Title updated:', newDoc.title);
        
        // Update meta tags
        updateMetaTags(newDoc);
        
        // Save chatbot container reference
        const savedChatbot = chatbotContainer;
        console.log('💬 Chatbot container saved:', savedChatbot ? 'Yes' : 'No');
        
        // Get all body children except chatbot and scripts
        const currentContent = Array.from(document.body.children).filter(
            el => el.id !== 'medical-chatbot-container' && el.tagName !== 'SCRIPT'
        );
        console.log('🗑️ Removing elements:', currentContent.length);
        
        // Get new content (everything except chatbot and scripts that will be reloaded)
        const newContent = Array.from(newDoc.body.children).filter(
            el => el.id !== 'medical-chatbot-container' && 
                  !(el.tagName === 'SCRIPT' && (
                      el.src.includes('navigation-handler.js') || 
                      el.src.includes('script.js')
                  ))
        );
        console.log('➕ Adding elements:', newContent.length);
        
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
                console.log('💬 Chatbot re-appended to body');
            } else {
                console.log('💬 Chatbot still in DOM');
            }
            
            // Reinitialize any scripts that need it
            reinitializeScripts();
            
            // Fade in new content
            setTimeout(() => {
                document.querySelectorAll('body > *:not(#medical-chatbot-container)').forEach(el => {
                    el.style.opacity = '1';
                });
                console.log('✨ Content faded in');
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
        // Don't handle hash changes
        if (window.location.hash) {
            console.log('⚓ Hash change detected, allowing normal scroll');
            return;
        }
        
        if (e.state && e.state.url) {
            navigateToPage(e.state.url);
        } else {
            // Fallback to current URL (but not for hash-only changes)
            const currentUrl = window.location.href.split('#')[0];
            if (e.state || currentUrl !== window.location.href) {
                navigateToPage(currentUrl);
            }
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
