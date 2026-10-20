import os
import re
import base64
import requests
from urllib.parse import urlparse, unquote

PAGE_URL = "https://www.deanspencerart.com/blackwhite"
OUTDIR = "images"
os.makedirs(OUTDIR, exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0 Safari/537.36",
    "Referer": PAGE_URL,
}

print(f"→ Fetching {PAGE_URL}")
resp = requests.get(PAGE_URL, headers=HEADERS, timeout=30)
resp.raise_for_status()
html = resp.text
print(f"  got {len(html):,} chars of HTML\n")

# ---------- map <img src> → data-filename so we get nice filenames ----------
img_tag_re = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
attr_re = re.compile(r'([\w:-]+)\s*=\s*"([^"]*)"')

filename_by_url = {}
for tag in img_tag_re.findall(html):
    attrs = dict(attr_re.findall(tag))
    fn = attrs.get("data-filename")
    for key in ("src", "ng-src", "data-src"):
        u = attrs.get(key)
        if fn and u and u.startswith("http"):
            filename_by_url[u] = fn

# ---------- collect image URLs ----------
url_re = re.compile(
    r'https?://[^"\'\s>)]+?\.(?:jpe?g|png|gif|webp)(?:\?[^"\'\s>)]*)?',
    re.IGNORECASE,
)

urls = []
seen = set()
for m in url_re.finditer(html):
    u = m.group(0).rstrip(".,;")
    # skip obvious non-artwork assets
    low = u.lower()
    if any(s in low for s in ("/logo", "favicon", "/icon", "sprite",
                              "placeholder", "no_pic", "nopic")):
        continue
    if u not in seen:
        seen.add(u)
        urls.append(u)

print(f"Found {len(urls)} candidate image URLs")
for u in urls[:5]:
    print(f"  • {u}")
if len(urls) > 5:
    print(f"  … and {len(urls) - 5} more\n")

if not urls:
    print("No image URLs in the raw HTML — the gallery is JS-rendered.")
    print("Use the browser-console script below instead.")
    raise SystemExit

# ---------- try to fetch a higher-res version ----------
SIZE_ORDER = ["h2400", "h1600", "h1200", "h800"]

def best_size(url):
    if not re.search(r'/h\d+-', url):
        return url
    for size in SIZE_ORDER:
        cand = re.sub(r'/h\d+-', f'/{size}-', url)
        try:
            r = requests.head(cand, headers=HEADERS, timeout=10,
                              allow_redirects=True)
            if r.status_code == 200 and r.headers.get(
                    "Content-Type", "").startswith("image/"):
                return cand
        except requests.RequestException:
            continue
    return url

def safe_name(name):
    name = unquote(name)
    name = re.sub(r'[^\w.\-]+', '_', name)
    return name or "image.jpg"

# ---------- download ----------
n = 0
for i, url in enumerate(urls, 1):
    target = best_size(url)
    try:
        r = requests.get(target, headers=HEADERS, timeout=60)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"  ✗ {target}  ({e})")
        continue

    # prefer data-filename, else derive from URL
    name = filename_by_url.get(url)
    if not name:
        path = urlparse(target).path
        name = os.path.basename(path) or f"image_{i:03d}.jpg"
    name = safe_name(name)

    n += 1
    fname = f"{n:03d}_{name}"
    out = os.path.join(OUTDIR, fname)
    with open(out, "wb") as f:
        f.write(r.content)

    h = re.search(r'/h(\d+)-', target)
    tag = f"h{h.group(1)}" if h else "orig"
    print(f"  ✓ {fname}  ({len(r.content):,} B, {tag})")

print(f"\nDone — {n} files written to ./{OUTDIR}/")