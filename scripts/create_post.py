#!/usr/bin/env python3
"""Create WordPress post via REST API"""
import argparse, json, os, sys, urllib.request
from base64 import b64encode

def create_post(url, username, password, title, content, status='draft', **kwargs):
    api_url = f"{url.rstrip('/')}/wp-json/wp/v2/posts"
    credentials = f"{username}:{password}".encode('utf-8')
    auth_header = b64encode(credentials).decode('ascii')
    
    data = {'title': title, 'content': content, 'status': status}
    if 'featured_media' in kwargs and kwargs['featured_media']:
        data['featured_media'] = int(kwargs['featured_media'])
    
    request = urllib.request.Request(api_url, data=json.dumps(data).encode('utf-8'), method='POST')
    request.add_header('Authorization', f'Basic {auth_header}')
    request.add_header('Content-Type', 'application/json')
    
    try:
        with urllib.request.urlopen(request) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(json.dumps(result, indent=2))
            return result
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

parser = argparse.ArgumentParser(description='Create WordPress post')
parser.add_argument('--url', default=os.getenv('WP_URL'))
parser.add_argument('--username', default=os.getenv('WP_USERNAME'))
parser.add_argument('--app-password', default=os.getenv('WP_APP_PASSWORD'))
parser.add_argument('--title', required=True)
parser.add_argument('--content', required=True)
parser.add_argument('--status', default='draft', choices=['publish', 'draft', 'pending'])
parser.add_argument('--featured-media', type=int)

args = parser.parse_args()
if not all([args.url, args.username, args.app_password]):
    print(json.dumps({"error": "Missing required credentials"}), file=sys.stderr)
    sys.exit(1)

create_post(args.url, args.username, args.app_password, args.title, args.content, args.status, featured_media=args.featured_media)
