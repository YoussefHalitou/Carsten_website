# Testing Guide for Chatbot Persistence

## 🧪 How to Test

### Step 1: Open Your Website

1. **Open the website** in your browser
   - If testing locally: Open `index.html` in your browser
   - If on a server: Navigate to your website URL

### Step 2: Open Browser Console

2. **Open Developer Tools**
   - **Chrome/Edge**: Press `F12` or `Cmd+Option+I` (Mac) / `Ctrl+Shift+I` (Windows)
   - **Firefox**: Press `F12` or `Cmd+Option+K` (Mac) / `Ctrl+Shift+K` (Windows)
   - **Safari**: Press `Cmd+Option+C` (Mac)

3. **Go to Console tab**

### Step 3: Check Initialization

You should see this message in the console:
```
✓ AJAX Navigation initialized - Chatbot will persist across pages
```

**If you DON'T see this message:**
- ❌ The navigation handler is not loading
- Check if `navigation-handler.js` file exists
- Check if it's included in your HTML before `</body>`
- Check for JavaScript errors

### Step 4: Test Navigation

4. **Click any internal link** (like "Team" or "Aktuelles")

You should see **detailed logging** in the console:
```
🖱️ Link clicked: team.html
🔍 Checking link: team.html
Link analysis: {...}
✅ Will handle with AJAX
🚀 Starting AJAX navigation to: team.html
📡 Fetching page: team.html
✅ Page fetched, length: 12345
📄 Page parsed, title: Unser Team
🔄 Updating page content...
📝 Title updated: Unser Team
💬 Chatbot container saved: Yes
🗑️ Removing elements: 5
➕ Adding elements: 5
💬 Chatbot still in DOM
✨ Content faded in
✨ Navigation complete!
```

**If you see `❌` messages:**
- Check what the specific error is
- The logs will tell you why the link wasn't handled

### Step 5: Test Chatbot Persistence

5. **Open the chatbot** (click the chatbot button)
6. **Send a message**
7. **Click a link** to navigate to another page
8. **Check if:**
   - ✅ The chatbot is still open
   - ✅ Your conversation is still there
   - ✅ The page content changed
   - ✅ URL updated in address bar

## 🐛 Common Issues & Solutions

### Issue 1: "✓ AJAX Navigation initialized" doesn't appear

**Problem:** Script not loading

**Solutions:**
1. Check file path is correct: `<script src="navigation-handler.js"></script>`
2. Verify file exists in same directory as HTML
3. Check for typos in filename
4. Clear browser cache (Cmd+Shift+R / Ctrl+F5)

### Issue 2: Links still reload the page

**Problem:** Links not being intercepted

**Check the console logs:**

If you see:
```
❌ Hash link
```
- This is an anchor link (#something), normal behavior

If you see:
```
❌ External or non-HTML
```
- The link goes to external site or non-HTML page

If you see:
```
⏭️ Allowing default navigation
```
- The script decided not to handle this link

**If you DON'T see any logs when clicking:**
- The event listener isn't working
- Check if script loaded after DOM
- Try hard refresh

### Issue 3: Chatbot still reloads

**Problem:** Chatbot container not persisting

**Check console for:**
```
💬 Chatbot container saved: No
```

**Solutions:**
1. Verify chatbot has `id="medical-chatbot-container"`
2. Check if chatbot is loaded when script runs
3. Make sure chatbot is in `<body>`, not in a wrapper

### Issue 4: Page content doesn't update

**Problem:** Content update failing

**Check console for errors after:**
```
📡 Fetching page: ...
```

**Common causes:**
1. Network error (check Network tab)
2. CORS issue (if loading from file://)
3. Parse error (check HTML validity)

### Issue 5: Works on some pages but not others

**Problem:** Inconsistent HTML structure

**Check:**
1. All pages have same basic structure
2. All pages have `id="medical-chatbot-container"` on chatbot
3. All pages include both `script.js` and `navigation-handler.js`

## 📊 What to Look For

### ✅ Good Signs (Working):
- Console shows navigation logs with emojis
- Page content changes without full reload
- URL updates in address bar
- Chatbot stays in bottom right
- No page flash/white screen
- Smooth fade transitions

### ❌ Bad Signs (Not Working):
- No console logs when clicking links
- Page does full reload (white flash)
- Chatbot disappears/reloads
- Console errors in red
- URL doesn't update
- Browser shows loading spinner

## 🔧 Advanced Debugging

### Test Individual Functions

Open console and test:

```javascript
// Check if navigation handler loaded
console.log('Navigation handler loaded:', 
  window.history.state && window.history.state.url);

// Check if chatbot exists
console.log('Chatbot:', 
  document.querySelector('#medical-chatbot-container'));

// Simulate navigation
window.dispatchEvent(new CustomEvent('pageContentUpdated'));
```

### Monitor Network Requests

1. Go to **Network** tab in DevTools
2. Click a link
3. You should see **only one** request for the new HTML
4. No full page reload
5. Chatbot iframe should NOT reload

### Check Chatbot iframe

```javascript
// Get chatbot iframe
const iframe = document.querySelector('#chatbot-iframe');
console.log('Iframe URL:', iframe?.src);
console.log('Iframe still in DOM:', 
  document.body.contains(iframe));
```

## 📝 Expected Behavior

### ✅ What SHOULD Happen:

1. **Click Link** → No white flash, smooth fade
2. **Content Changes** → Header, main content updates
3. **Chatbot Persists** → Stays visible, conversation intact
4. **URL Updates** → Address bar shows new URL
5. **Back Button** → Goes back with AJAX (no reload)
6. **Forward Button** → Goes forward with AJAX

### ❌ What should NOT happen:

1. Page flashes white
2. Chatbot button disappears/reappears
3. Conversation resets
4. Browser loading spinner
5. Page scrolls unexpectedly

## 💡 Pro Tips

1. **Use Chrome DevTools** - Best debugging experience
2. **Keep console open** - See real-time logs
3. **Test in incognito** - No cache/extension interference
4. **Test different links** - Some might behave differently
5. **Test back/forward** - Should work seamlessly

## 🆘 Still Not Working?

If after all this it still doesn't work:

### Provide this info:

1. **Browser & Version**: Chrome 120, Firefox 121, etc.
2. **Console Logs**: Copy all logs from clicking a link
3. **Console Errors**: Any red error messages
4. **Behavior**: Exactly what happens vs. what should happen
5. **URL**: Are you testing locally (file://) or on server (http://)?

### File:// Protocol Issue

⚠️ **Important**: If testing locally with `file://` protocol:
- AJAX requests might be blocked
- **Solution**: Use a local server instead

**Quick Local Server:**

```bash
# Python 3
cd /path/to/website
python3 -m http.server 8000

# Then open: http://localhost:8000
```

---

## ✅ Success Checklist

- [ ] Console shows "✓ AJAX Navigation initialized"
- [ ] Clicking links shows detailed logs
- [ ] Page content changes without reload
- [ ] URL updates in address bar
- [ ] Chatbot stays visible
- [ ] Conversation persists
- [ ] Back/forward buttons work
- [ ] No JavaScript errors

If all checked ✅ → **It's working perfectly!** 🎉
