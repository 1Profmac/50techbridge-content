# Credential Rotation Checklist
## Deadline: 2026-04-10 (Friday)

Credentials were exposed in lmt-claude-brain git history.
History was scrubbed on 2026-04-03, but old clones may still have them.

---

### 1. WordPress Password
- [ ] Log in at learnmoretechnologies.com/wp-admin
- [ ] Go to Users > Profile > Set New Password
- [ ] Generate a strong password
- [ ] Save new password in RoboForm

### 2. GitHub Personal Access Token
- [ ] Go to GitHub > Settings > Developer settings > Personal access tokens
- [ ] Revoke the old token
- [ ] Generate a new token with same scopes
- [ ] Save new token in RoboForm

### 3. Mailchimp API Key
- [ ] Go to Mailchimp > Account > Extras > API keys
- [ ] Disable the old key
- [ ] Create a new key
- [ ] Save new key in RoboForm

### 4. Update Local Environment
- [ ] Open C:\Users\USER\Documents\lmt-claude-brain\.env
- [ ] Replace old WordPress password
- [ ] Replace old GitHub token
- [ ] Replace old Mailchimp API key
- [ ] Verify .env is in .gitignore (never commit it)

### 5. Verify
- [ ] Test WordPress login with new password
- [ ] Test git push with new token
- [ ] Test Mailchimp integration with new key
- [ ] Confirm no credentials in any tracked files
