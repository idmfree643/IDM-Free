"""Small allow-list helper for links presented as official IDM resources."""

from urllib.parse import urlparse


OFFICIAL_HOSTS = frozenset({
    "internetdownloadmanager.com",
    "www.internetdownloadmanager.com",
})


def normalized_host(url: str) -> str:
    """Return a normalized hostname or an empty string for malformed input."""
    try:
        return (urlparse(url.strip()).hostname or "").lower().rstrip(".")
    except (AttributeError, ValueError):
        return ""


def is_official_idm_url(url: str) -> bool:
    """Accept HTTPS pages hosted directly by the official IDM domain."""
    try:
        parsed = urlparse(url.strip())
    except (AttributeError, ValueError):
        return False
    return parsed.scheme == "https" and normalized_host(url) in OFFICIAL_HOSTS
