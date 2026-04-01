# WordPress API Pro - Claude Code Instructions

This is a WordPress REST API skill for managing posts, pages, media, and plugins on WordPress sites.
Originally an OpenClaw Skill, fully compatible with Claude Code (all scripts are standalone Python CLI tools with no OpenClaw runtime dependency).

## Prerequisites

- Python 3.6+
- WordPress 4.7+ with REST API enabled
- Application Password configured on the target WordPress site

## Authentication

Set environment variables before running scripts:

```bash
export WP_URL="https://example.com"
export WP_USERNAME="admin"
export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"
```

For WooCommerce operations, also set:

```bash
export WC_CONSUMER_KEY="ck_..."
export WC_CONSUMER_SECRET="cs_..."
```

## Available Scripts

All scripts are in `scripts/` and accept `--help` for full usage. Credentials can be passed via CLI args or environment variables.

| Script | Purpose | Key Arguments |
|---|---|---|
| `create_post.py` | Create a new post | `--title`, `--content`, `--status` |
| `update_post.py` | Update an existing post | `--post-id`, `--content`, `--title`, `--status` |
| `get_post.py` | Retrieve a single post | `--post-id` |
| `list_posts.py` | List/filter posts | `--per-page`, `--status`, `--author` |
| `upload_media.py` | Upload image/file to media library | `--file`, `--title`, `--alt-text`, `--set-featured` |
| `detect_plugins.py` | Detect installed WP plugins | `--verbose` |
| `acf_fields.py` | Read/write ACF custom fields | `--post-id`, `--field`, `--set`, `--value` |
| `seo_meta.py` | Read/write Rank Math / Yoast SEO meta | `--post-id`, `--plugin`, `--set`, `--detect` |
| `jetengine_fields.py` | Read/write JetEngine fields | `--post-id`, `--field`, `--set`, `--value` |
| `elementor_content.py` | Read/update Elementor page content | `--post-id`, `--action`, `--widget-id`, `--content` |
| `woo_products.py` | Manage WooCommerce products | `--action`, `--product-id`, `--title`, `--price` |
| `batch_update.py` | Batch operations across sites | `--group`, `--post-ids`, `--dry-run` |
| `wp_cli.py` | CLI wrapper for multi-site ops | (see `wp.sh`) |

## Multi-Site Setup

1. `cp config/sites.example.json config/sites.json`
2. Edit `config/sites.json` with site credentials
3. Use `./wp.sh <site-or-group> <command> [args]` or `batch_update.py`

## Usage Patterns

Run scripts with `python3 scripts/<script>.py [args]`. All output is JSON to stdout, errors to stderr. Exit code 0 = success, 1 = error.

## Security Rules

- Never hardcode credentials in scripts or commit them to git
- Always use HTTPS
- Prefer Application Passwords over Basic Auth
- Store credentials in environment variables only
- `config/sites.json` is gitignored - never commit it

## Reference Docs

- `references/api-reference.md` - WordPress REST API endpoints
- `references/gutenberg-blocks.md` - Gutenberg block format guide
- `SKILL.md` - Full skill documentation with all examples
