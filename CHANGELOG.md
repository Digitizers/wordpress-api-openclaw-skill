# Changelog

## [3.2.0] - 2026-03-28

### Added
- **Elementor content support** - `scripts/elementor_content.py`
  - Get Elementor page data via `_elementor_data` meta field
  - Update Elementor widgets (headings, text, buttons)
  - Recursive widget search by ID
  - Supports nested element structures
- **Media upload** - `scripts/upload_media.py`
  - Upload images from local files or URLs
  - Set title, alt text, and caption
  - Auto-detect MIME types
  - Set as featured image with `--set-featured`
  - Multipart form-data upload support
- **WooCommerce products** - `scripts/woo_products.py`
  - List, get, create, and update WooCommerce products
  - Consumer Key/Secret authentication
  - Support for price, status, SKU, stock management
  - WooCommerce REST API v3 integration

### Documentation
- Added Elementor, Media Upload, and WooCommerce sections to SKILL.md
- Documented all authentication methods and environment variables
- Added usage examples for all new features

## [3.1.0] - 2026-03-05

### Added
- **Plugin support:** ACF, JetEngine, Rank Math SEO, Yoast SEO
- `scripts/detect_plugins.py` - Auto-detect installed WordPress plugins
- `scripts/acf_fields.py` - Read/write ACF (Advanced Custom Fields) with REST API + postmeta fallback
- `scripts/seo_meta.py` - Read/write Rank Math and Yoast SEO meta fields with auto-detection
- `scripts/jetengine_fields.py` - Read/write JetEngine custom fields via postmeta
- Support for both `WP_SITE_URL` and `WP_URL` environment variables (backward compatible)
- Support for both `WP_USER` and `WP_USERNAME` environment variables

### Changed
- All new scripts use `requests` library for better error handling and cleaner code
- Improved error messages with structured JSON output
- Enhanced documentation in SKILL.md with plugin integration examples

## [3.0.0] - 2026-03-02

### Security
- **BREAKING:** Fixed credential exposure vulnerability
- CLI wrapper now passes credentials via environment variables instead of command-line arguments
- Credentials no longer visible in `ps` output
- Added SECURITY.md documentation

### Added
- Direct env var mode: use WP_URL/WP_USERNAME/WP_APP_PASSWORD without config file
- Environment-based credential passing (subprocess env parameter)

### Changed
- `wp_cli.py` refactored to prioritize env vars over config file
- Config file now optional (fallback for multi-site management)
- Backward compatible with existing config files

## [2.0.1] - 2026-03-02

### Changed
- Renamed slug to `wordpress-api-pro` (cleaner, follows package manager conventions)
- Updated all documentation to use shorter slug
- Updated GitHub repository URL

## [2.0.0] - 2026-03-02

### Added
- **Multi-site management system**
  - `config/sites.json` - Centralized site configuration
  - `./wp` CLI wrapper - Easy site switching
  - `scripts/wp_cli.py` - Multi-site command router
  - `scripts/batch_update.py` - Batch operations across sites
  - Site groups (e.g., "all", "digitizer")
  - Dry-run mode for safe testing
- `EXAMPLES.md` - Comprehensive usage examples
- `CHANGELOG.md` - This file

### Changed
- Updated `SKILL.md` with multi-site documentation
- Updated `README.md` with multi-site quick start
- Updated `.gitignore` to exclude `config/sites.json`

### Security
- Config file with credentials excluded from git by default
- Template file (`sites.example.json`) provided instead

## [1.0.0] - 2026-03-02

### Added
- Initial release
- WordPress REST API integration
- 4 core scripts:
  - `update_post.py` - Update existing posts
  - `create_post.py` - Create new posts
  - `get_post.py` - Retrieve post data
  - `list_posts.py` - List and filter posts
- Gutenberg block format support
- Application Password authentication
- Reference documentation:
  - `references/api-reference.md`
  - `references/gutenberg-blocks.md`
- `SKILL.md` - Skill definition
- `README.md` - GitHub documentation
- `LICENSE` - MIT License
- `package.json` - ClawHub metadata
- `.gitignore` - Security rules
