// Chatbot iframe resize handler
// This script handles postMessage communication from the chatbot iframe
// and dynamically resizes the iframe based on open/close state

(function() {
    'use strict';
    
    const iframe = document.getElementById('chatbot-iframe');
    if (!iframe) {
        console.warn('Chatbot iframe not found');
        return;
    }
    
    // Default sizes
    const CLOSED_HEIGHT = '100vh'; // Full height when closed (button only visible)
    const OPEN_HEIGHT = '690px'; // Height when chat widget is open (600px widget + 90px button offset)
    const CLOSED_WIDTH = '100vw'; // Full width when closed
    const OPEN_WIDTH = '420px'; // Width when open (380px widget + margins)
    
    // Listen for messages from the chatbot iframe
    window.addEventListener('message', function(event) {
        // Security: Verify message source (optional but recommended)
        // For now, we accept messages from any origin, but you can restrict to:
        // if (event.origin !== 'https://chatbotcarsten.live') return;
        
        // Check if message is from our chatbot
        if (event.data && event.data.source === 'carsten-chatbot') {
            const isOpen = event.data.type === 'open';
            
            // Resize iframe based on open/close state
            if (isOpen) {
                // Chat is open - resize to show the widget
                iframe.style.height = OPEN_HEIGHT;
                iframe.style.width = OPEN_WIDTH;
                iframe.style.maxWidth = 'calc(100vw - 40px)'; // Responsive on mobile
            } else {
                // Chat is closed - full viewport (only button visible)
                iframe.style.height = CLOSED_HEIGHT;
                iframe.style.width = CLOSED_WIDTH;
                iframe.style.maxWidth = 'none';
            }
            
            console.log('Chatbot state changed:', isOpen ? 'open' : 'closed');
        }
    });
    
    // Optional: Handle initial state
    // You might want to set initial size based on some condition
    // For now, we start with closed state (full viewport)
})();
