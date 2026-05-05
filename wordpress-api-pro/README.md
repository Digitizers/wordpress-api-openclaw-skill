# WordPress API Pro - OpenClaw Skill

WordPress REST API integration skill for OpenClaw. It manages posts, pages, media, WooCommerce products, Elementor content, SEO metadata, ACF, and JetEngine fields with explicit safety boundaries for agentic use.

## Version

Current version: **3.4.0**

## Install

```bash
openclaw skills install wordpress-api-pro
```

Manual install from this repository:

```bash
cd ~/.openclaw/workspace/skills/
git clone https://github.com/Digitizers/wordpress-api-pro.git wordpress-api-pro-repo
cp -R wordpress-api-pro-repo/wordpress-api-pro ./wordpress-api-pro
```

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
python3 scripts/get_post.py --post-id 123
python3 scripts/list_posts.py --per-page 10 --status publish
```

Create a draft:

```bash
python3 scripts/create_post.py \
  --title "Draft title" \
  --content "Draft content" \
  --status draft
```

Update a post after approval:

```bash
python3 scripts/update_post.py \
  --post-id 123 \
  --content "Approved content" \
  --status draft
```

Upload local media:

```bash
python3 scripts/upload_media.py --file ./media/image.jpg --title "Image title"
```

Upload remote media with explicit opt-in:

```bash
python3 scripts/upload_media.py \
  --file https://cdn.example.com/image.jpg \
  --allow-remote-url \
  --title "Image title"
```

## Multi-site setup

```bash
cp config/sites.example.json config/sites.json
chmod 600 config/sites.json
```

`config/sites.example.json` intentionally contains no credentials.

```bash
./wp.sh --list-sites
./wp.sh sample-site get-post --id 123
./wp.sh sample-site update-post --id 123 --status draft
```

Group operation:

```bash
./wp.sh sample --execute-group update-post --id 123 --status draft
```

All-sites group operation, only after explicit approval:

```bash
./wp.sh all --execute-group --allow-all update-post --id 123 --status draft
```

## Batch operations

Dry-run preview:

```bash
python3 scripts/batch_update.py \
  --group sample \
  --post-ids 123,456 \
  --status draft
```

Apply after review:

```bash
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
