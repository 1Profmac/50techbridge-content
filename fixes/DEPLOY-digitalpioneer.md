# Deploy Process — digitalpioneer.ai
**Last Updated:** 2026-08-11

## How to push any change live to digitalpioneer.ai

1. Edit the file locally:
   `Desktop/LMT/BRAND/web/digitalpioneer-index.html`

2. Copy to the deploy repo:
   `cp "/c/Users/USER/Desktop/LMT/BRAND/web/digitalpioneer-index.html" "/c/Users/USER/Documents/digitalpioneer-pages/index.html"`

3. Commit and push:
   ```
   cd /c/Users/USER/Documents/digitalpioneer-pages
   git add index.html
   git commit -m "description of change"
   git push origin master
   ```

4. Deploy via Bluehost:
   - Bluehost cPanel → Git Version Control → **digitalpioneer-pages** → Manage
   - Click **Pull or Deploy** tab
   - Click **Update from Remote**
   - Click **Deploy HEAD Commit**

5. Verify live at digitalpioneer.ai

---

## Repos Involved
| Repo | Purpose | Location |
|---|---|---|
| `50techbridge-content` | Source/editing | `Desktop/LMT/` |
| `digitalpioneer-pages` | Deploy to server | `Documents/digitalpioneer-pages/` |
| Bluehost Git | Live server | `/home1/ghosnhmy/repos/digitalpioneer` |

---

## Credentials
- MailerLite API Key: stored in `Desktop/LMT/tools/.env`
- MailerLite Group: Agentic50+ (ID: 191122765174015605)
- Bluehost account: brian@learnmo.com
