# Security Considerations - wordpress-api skill

## ⚠️ Credential Exposure Risk

This skill stores WordPress application passwords in plaintext configuration files and may expose them via command-line arguments.

### Known Issues:

1. **Process List Exposure**
   - The CLI wrapper (`wp_cli.py`) passes `--app-password` as command-line arguments
   - This is visible in `ps` output to all users on the system
   - **Impact:** On shared systems, other users can see your credentials

2. **Config File Storage**
   - Credentials stored in `config/sites.json` (plaintext)
   - **Mitigation:** File permissions set to `600` (owner-only)
   - **Risk:** Still readable if attacker gains your user access

3. **Subprocess Calls**
   - Python scripts spawn subprocesses with credentials in arguments
   - Visible momentarily in process tree

---

## Mitigations Applied:

✅ `config/sites.json` permissions: `600` (owner read/write only)  
✅ User-invocable only (not forced-always, no elevated persistence)  
✅ No external network calls beyond WordPress API endpoints  

---

## Recommendations:

### For Production Use:

1. **Use Environment Variables**
   ```bash
   # Instead of config/sites.json, use:
   export WP_URL="https://site.com"
   export WP_USERNAME="admin"
   export WP_APP_PASSWORD="xxxx xxxx xxxx"
   
   # Call scripts directly (not via wp_cli.py wrapper):
   python3 scripts/update_post.py --post-id 123 --title "..."
   ```

2. **Restrict File Permissions**
   ```bash
   chmod 600 config/sites.json
   ```

3. **Audit Before Production**
   - Review `config/sites.json` and scripts before use on shared systems
   - Test on staging with `-dry-run` first
   - Remove credentials from config after use

4. **Avoid Wrapper on Shared Systems**
   - Don't use `wp_cli.py` on multi-user machines
   - Call Python scripts directly with env vars

---

## For Single-User VPS (Your Case):

✅ **You're fine** - you're the only user, so process exposure isn't a risk  
✅ **Still recommended:** `chmod 600 config/sites.json`  
✅ **Optional:** Switch to env vars for better practice  

---

## Planned Fixes (Future Versions):

- [ ] Add metadata declaration for required env vars/config
- [ ] Modify CLI wrapper to read from stdin or secure store
- [ ] Add option for encrypted config file
- [ ] Add `--from-env` flag to skip command-line password passing

---

## When NOT to Use:

❌ Shared hosting with multiple user accounts  
❌ Systems where you don't trust other users  
❌ If you can't audit the code yourself  

---

**Bottom Line:** This skill is **safe for your single-user VPS**, but has real security concerns for shared environments. Use with caution and follow mitigations above.
