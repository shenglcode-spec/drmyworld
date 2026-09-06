from datetime import datetime

try:
    from zoneinfo import ZoneInfo  # Python 3.9+
except ImportError:
    from backports.zoneinfo import ZoneInfo  # Python 3.8

from skills import skill


@skill
def get_current_time(timezone: str = "Asia/Shanghai") -> dict:
    """获取指定时区的当前日期和时间

    Args:
        timezone: IANA 时区名称，默认 Asia/Shanghai
    """
    now = datetime.now(ZoneInfo(timezone))
    return {
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S"),
        "weekday": "一二三四五六日"[now.weekday()],
        "timezone": timezone,
    }
