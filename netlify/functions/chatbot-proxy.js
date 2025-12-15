/**
 * Netlify Function als Proxy für das Chatbot-Backend
 * 
 * Diese Function leitet Anfragen von HTTPS (Netlify) zu HTTP (Backend) weiter
 */

exports.handler = async (event, context) => {
    // CORS Headers für alle Anfragen
    const headers = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': 'Content-Type, X-API-Key',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Content-Type': 'application/json'
    };
  
    // Handle OPTIONS (Preflight)
    if (event.httpMethod === 'OPTIONS') {
      return {
        statusCode: 200,
        headers,
        body: ''
      };
    }
  
    try {
      // Backend URL
      const backendUrl = 'http://37.27.12.97:8000';
      
      // Pfad aus der Anfrage extrahieren
      // Netlify Functions haben den Pfad: /.netlify/functions/function-name
      // Wir entfernen das und behalten nur den API-Pfad
      let path = event.path;
      
      // Entferne Function-Pfad
      path = path.replace('/.netlify/functions/chatbot-proxy', '');
      
      // Falls leer, verwende den Query-Parameter 'path'
      if (!path || path === '/') {
        path = event.queryStringParameters?.path || '/api';
      }
      
      // Stelle sicher, dass /api am Anfang steht
      if (!path.startsWith('/api')) {
        path = '/api' + (path.startsWith('/') ? path : '/' + path);
      }
      
      const fullUrl = `${backendUrl}${path}${event.queryStringParameters && Object.keys(event.queryStringParameters).filter(k => k !== 'path').length > 0 ? '?' + new URLSearchParams(Object.fromEntries(Object.entries(event.queryStringParameters).filter(([k]) => k !== 'path'))).toString() : ''}`;
  
      // Headers für Backend-Anfrage
      const requestHeaders = {
        'Content-Type': 'application/json'
      };
  
      // API-Key aus Header oder Query-Parameter
      const apiKey = event.headers['x-api-key'] || event.queryStringParameters?.api_key || '12345';
      requestHeaders['X-API-Key'] = apiKey;
  
      // Body parsen
      let body = null;
      if (event.body) {
        try {
          body = JSON.parse(event.body);
        } catch (e) {
          body = event.body;
        }
      }
  
      // Anfrage an Backend senden
      const response = await fetch(fullUrl, {
        method: event.httpMethod,
        headers: requestHeaders,
        body: body ? JSON.stringify(body) : undefined
      });
  
      const data = await response.json();
  
      return {
        statusCode: response.status,
        headers,
        body: JSON.stringify(data)
      };
    } catch (error) {
      console.error('Proxy Error:', error);
      return {
        statusCode: 500,
        headers,
        body: JSON.stringify({ 
          error: 'Proxy-Fehler',
          message: error.message 
        })
      };
    }
  };
  
  