# wordpress-api-pro

[![CI](https://github.com/Digitizers/wordpress-api-pro/actions/workflows/ci.yml/badge.svg)](https://github.com/Digitizers/wordpress-api-pro/actions/workflows/ci.yml)

OpenClaw WordPress API Pro skill repository. Manage WordPress posts, pages, media, WooCommerce, Elementor, SEO meta, ACF, and JetEngine fields programmatically — with explicit safety boundaries for agentic use.

## Features

- ✅ **Full CRUD** — create, read, update, and delete WordPress posts/pages.
- ✅ **Gutenberg support** — work with native block content safely.
- ✅ **Elementor content** — read and update Elementor `_elementor_data` content.
- ✅ **Media upload** — upload local media or explicitly approved HTTPS remote media.
- ✅ **WooCommerce products** — manage product data through the REST API.
- ✅ **Plugin fields** — ACF, JetEngine, Rank Math, and Yoast SEO helpers.
- ✅ **Multi-site workflows** — site config, groups, and wrapper commands via `wp.sh`.
- ✅ **Dry-run-first batch operations** — preview bulk changes before execution.
- ✅ **Safety gates** — protected local file reads, remote URL checks, and explicit live-write flags.
- ✅ **CI verified** — Python 3.11/3.12/3.13 smoke tests and package validation.

The actual skill payload lives in:

```text
wordpress-api-pro/
```

Repository-only files such as this README, changelog, license, CI, and package metadata intentionally stay outside the skill directory.

## Version

Current version: **3.4.0**

## Install

```bash
openclaw skills install wordpress-api-pro
```

Manual install from this repository:

```bash
cp -R wordpress-api-pro ~/.openclaw/workspace/skills/wordpress-api-pro
```

ClawHub package directory: `wordpress-api-pro/`.

## Security model

- Use a dedicated least-privilege WordPress API user.
- Prefer environment variables for credentials.
- Keep `config/sites.json` local, untracked, and `chmod 600`.
- Batch operations are dry-run by default and require `--execute` for live changes.
- Group operations through `wp.sh` require `--execute-group`.
- Targeting a group named `all` requires `--allow-all`.
- Local file reads are restricted to the current working directory by default. Use `WP_ALLOWED_FILE_ROOTS` to approve another directory.
- Remote media downloads require `--allow-remote-url` or `WP_ALLOW_REMOTE_URLS=1`, allow HTTPS only, and block private/local network hosts.

## Authentication

```bash
export WP_URL="https://example.com"
export WP_USERNAME="wp-api-user"
read -rs WP_APP_PASSWORD
export WP_APP_PASSWORD
```

## Quick examples

Read/list:

```bash
cd wordpress-api-pro
python3 scripts/get_post.py --post-id 123
python3 scripts/list_posts.py --per-page 10 --status publish
```

Create a draft:

```bash
cd wordpress-api-pro
python3 scripts/create_post.py \
  --title "Draft title" \
  --content "Draft content" \
  --status draft
```

Update a post after approval:

```bash
cd wordpress-api-pro
python3 scripts/update_post.py \
  --post-id 123 \
  --content "Approved content" \
  --status draft
```

Upload local media:

```bash
cd wordpress-api-pro
python3 scripts/upload_media.py --file ./media/image.jpg --title "Image title"
```

Upload remote media with explicit opt-in:

```bash
cd wordpress-api-pro
python3 scripts/upload_media.py \
  --file https://cdn.example.com/image.jpg \
  --allow-remote-url \
  --title "Image title"
```

## Multi-site setup

```bash
cd wordpress-api-pro
cp config/sites.example.json config/sites.json
chmod 600 config/sites.json
```

`config/sites.example.json` intentionally contains no credentials.

```bash
cd wordpress-api-pro
./wp.sh --list-sites
./wp.sh sample-site get-post --id 123
./wp.sh sample-site update-post --id 123 --status draft
```

Group operation:

```bash
cd wordpress-api-pro
./wp.sh sample --execute-group update-post --id 123 --status draft
```

All-sites group operation, only after explicit approval:

```bash
cd wordpress-api-pro
./wp.sh all --execute-group --allow-all update-post --id 123 --status draft
```

## Batch operations

Dry-run preview:

```bash
cd wordpress-api-pro
python3 scripts/batch_update.py \
  --group sample \
  --post-ids 123,456 \
  --status draft
```

Apply after review:

```bash
cd wordpress-api-pro
python3 scripts/batch_update.py \
  --group sample \
  --post-ids 123,456 \
  --status draft \
  --execute
```

## Scripts

- `update_post.py` — update an existing post.
- `create_post.py` — create a post/page.
- `get_post.py` — retrieve one post.
- `list_posts.py` — list/filter posts.
- `batch_update.py` — safe dry-run-first batch updates.
- `upload_media.py` — upload local or explicitly approved remote media.
- `detect_plugins.py` — detect supported WordPress plugins.
- `acf_fields.py` — read/write ACF fields.
- `seo_meta.py` — read/write Rank Math and Yoast SEO meta.
- `jetengine_fields.py` — read/write JetEngine custom fields.
- `elementor_content.py` — read/update Elementor content.
- `woo_products.py` — manage WooCommerce products.
- `security.py` — local file/remote URL safety helpers.

## Requirements

- Python 3.8+
- WordPress 5.6+ recommended for built-in Application Passwords
- `requests` for plugin integration scripts: `pip install requests`

## Links

- Repository: https://github.com/Digitizers/wordpress-api-pro
- ClawHub: https://clawhub.ai/benkalsky/wordpress-api-pro
- WordPress REST API: https://developer.wordpress.org/rest-api/
