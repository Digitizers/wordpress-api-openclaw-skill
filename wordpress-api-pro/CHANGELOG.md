# Changelog

## 3.4.0 - 2026-05-05

Security and packaging cleanup for ClawHub publication.

- Moved the publishable skill into the internal `wordpress-api-pro/` directory.
- Added `scripts/security.py` with local file and remote URL safety boundaries.
- Restricted `update_post.py --content-file` to approved local roots.
- Restricted `upload_media.py` local reads to approved roots and made remote URL fetching explicit opt-in.
- Blocked HTTPS remote media URLs that resolve to private, loopback, link-local, multicast, reserved, or unspecified addresses.
- Made `batch_update.py` dry-run by default; live mutation now requires `--execute` and confirmation.
- Added `--allow-all` gate for targeting all configured sites.
- Added `--execute-group` / `--allow-all` gates to the multi-site wrapper.
- Removed admin-style credential examples and hardcoded-looking placeholders from docs/config examples.
- Updated metadata to include repository directory, homepage, and version `3.4.0`.

## 3.3.0 - 2026-05-01

- Previous ClawHub-published version.
- Included WordPress posts/pages/media/WooCommerce/Elementor helper scripts.

## Earlier versions

Earlier versions mixed packaging, documentation, and security changes. Use `git log` for detailed history.
