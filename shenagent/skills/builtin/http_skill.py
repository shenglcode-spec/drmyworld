import httpx

from skills import skill


@skill
def http_get(url: str, timeout: float = 10.0) -> dict:
    """向指定 URL 发送 GET 请求并返回响应内容

    Args:
        url: 完整的 HTTP 或 HTTPS 地址
        timeout: 请求超时秒数，默认 10
    """
    with httpx.Client(timeout=timeout, follow_redirects=True) as client:
        resp = client.get(url)
    content_type = resp.headers.get("content-type", "")
    if "json" in content_type:
        body = resp.json()
    else:
        body = resp.text[:2000]
    return {"status": resp.status_code, "content_type": content_type, "body": body}
