"""
LMT Site Health Check — Run daily to catch problems before they cost you traffic.
Usage: python site-health-check.py
"""

import urllib.request
import urllib.error
import ssl
import socket
import json
import datetime
import sys

DOMAIN = "learnmoretechnologies.com"
URLS_TO_CHECK = [
    f"https://{DOMAIN}",
    f"https://{DOMAIN}/courses/50techbridge/",
    f"https://{DOMAIN}/startfreetoday",
    f"https://{DOMAIN}/train",
    f"https://{DOMAIN}/workforce",
    f"https://{DOMAIN}/speak",
    f"https://{DOMAIN}/contact-us",
]

MAILCHIMP_API_KEY_ENV = "MAILCHIMP_API_KEY"  # set in tools/.env or environment
MAILCHIMP_SERVER = "us21"  # update to match your Mailchimp server prefix

def check_ssl():
    """Check SSL certificate validity and expiration."""
    print("\n== SSL CERTIFICATE ==")
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=DOMAIN) as s:
            s.settimeout(10)
            s.connect((DOMAIN, 443))
            cert = s.getpeercert()
            expires = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            days_left = (expires - datetime.datetime.utcnow()).days
            print(f"  VALID — expires {expires.strftime('%Y-%m-%d')} ({days_left} days left)")
            if days_left < 14:
                print(f"  *** WARNING: SSL expires in {days_left} days! Renew NOW. ***")
            return True
    except ssl.SSLError as e:
        print(f"  BROKEN — {e}")
        return False
    except Exception as e:
        print(f"  ERROR — {e}")
        return False

def check_urls():
    """Check each critical URL for status code and redirects."""
    print("\n== PAGE STATUS ==")
    results = []
    for url in URLS_TO_CHECK:
        try:
            req = urllib.request.Request(url, method='GET')
            req.add_header('User-Agent', 'LMT-HealthCheck/1.0')
            resp = urllib.request.urlopen(req, timeout=15)
            status = resp.getcode()
            final_url = resp.geturl()
            redirected = " (redirected)" if final_url != url else ""
            print(f"  {status} OK — {url}{redirected}")
            results.append((url, status, True))
        except urllib.error.HTTPError as e:
            print(f"  {e.code} FAIL — {url}")
            results.append((url, e.code, False))
        except urllib.error.URLError as e:
            print(f"  DOWN — {url} — {e.reason}")
            results.append((url, 0, False))
        except Exception as e:
            print(f"  ERROR — {url} — {e}")
            results.append((url, 0, False))
    return results

def check_mailchimp():
    """Ping Mailchimp API to verify key is valid."""
    print("\n== MAILCHIMP API ==")
    import os
    api_key = os.environ.get(MAILCHIMP_API_KEY_ENV, "")

    # Try loading from tools/.env if not in environment
    if not api_key:
        env_path = os.path.join(os.path.dirname(__file__), '..', 'tools', '.env')
        if os.path.exists(env_path):
            with open(env_path) as f:
                for line in f:
                    if line.strip().startswith('MAILCHIMP_API_KEY='):
                        api_key = line.strip().split('=', 1)[1].strip().strip('"').strip("'")

    if not api_key:
        print("  SKIP — No Mailchimp API key found in environment or tools/.env")
        return None

    server = api_key.split('-')[-1] if '-' in api_key else MAILCHIMP_SERVER
    url = f"https://{server}.api.mailchimp.com/3.0/ping"
    try:
        req = urllib.request.Request(url)
        credentials = f"anystring:{api_key}"
        import base64
        encoded = base64.b64encode(credentials.encode()).decode()
        req.add_header('Authorization', f'Basic {encoded}')
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        if data.get('health_status'):
            print(f"  VALID — {data['health_status']}")
            return True
        else:
            print(f"  UNKNOWN — {data}")
            return False
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  FAIL ({e.code}) — {body[:200]}")
        return False
    except Exception as e:
        print(f"  ERROR — {e}")
        return False

def check_wp_rest_api():
    """Verify WordPress REST API is responding."""
    print("\n== WORDPRESS REST API ==")
    url = f"https://{DOMAIN}/wp-json/wp/v2/posts?per_page=1"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'LMT-HealthCheck/1.0')
        resp = urllib.request.urlopen(req, timeout=15)
        data = json.loads(resp.read())
        if isinstance(data, list) and len(data) > 0:
            title = data[0].get('title', {}).get('rendered', 'Unknown')
            print(f"  VALID — Latest post: {title[:60]}")
            return True
        else:
            print(f"  WARNING — API responded but no posts found")
            return False
    except Exception as e:
        print(f"  FAIL — {e}")
        return False

def summary(ssl_ok, url_results, mc_ok):
    """Print summary with action items."""
    print("\n" + "=" * 50)
    print("HEALTH CHECK SUMMARY — " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    print("=" * 50)

    issues = []
    if not ssl_ok:
        issues.append("SSL certificate is BROKEN — site is down for all visitors")
    failed_urls = [u for u, s, ok in url_results if not ok]
    if failed_urls:
        issues.append(f"{len(failed_urls)} page(s) returning errors: {', '.join(failed_urls)}")
    if mc_ok is False:
        issues.append("Mailchimp API key is INVALID — new signups not syncing to email list")

    if issues:
        print("\nACTION REQUIRED:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    else:
        print("\n  All systems healthy.")

    print()

def main():
    print(f"LMT Site Health Check — {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Domain: {DOMAIN}")

    ssl_ok = check_ssl()
    url_results = check_urls()
    mc_ok = check_mailchimp()
    check_wp_rest_api()
    summary(ssl_ok, url_results, mc_ok)

if __name__ == "__main__":
    main()
