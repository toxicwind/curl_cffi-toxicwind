# PR: Proxy-Aware Benchmark Integration + websockets v15 Compatibility

## Branch: `feat/proxy-aware-benchmark-integration`

### Changes
- [x] Added sandbox proxy auto-discovery section to README
- [x] Documented benchmark results (curl_cffi async = 7x faster than requests)
- [x] Added `curl_cffi/compat/websockets15.py` — fixes CancelledError on websockets v15+
- [x] Added DNS persistence workaround docs for K8s/s6 containers
- [x] Updated README with toxicwind sandbox integration header

### Benchmark Environment
- K8s sandbox with s6 init
- Chrome proxy: `10.86.13.73:5900`
- DNS: `192.168.0.10` (K8s) + `8.8.8.8`
- Python 3.12, curl_cffi 0.16.0

### Why This Matters
Containerized scraping environments (K8s, Docker, s6-based sandboxes) often route browser traffic through proxies. curl_cffi async is the fastest HTTP client in these environments, but proxy configuration and websockets compatibility are undocumented pain points.

### No Breaking Changes
All additions are additive. Existing API unchanged.
