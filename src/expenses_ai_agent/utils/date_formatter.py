from datetime import datetime
from zoneinfo import ZoneInfo


def format_datetime(datetime_str: str, timezone_str: str | None = None) -> str:
    try:
        parsed_datetime = datetime.fromisoformat(datetime_str)
    except ValueError:
        raise ValueError(f"Could not parse {datetime_str}")
    if timezone_str is not None:
        tz = ZoneInfo(timezone_str)
        converted_parsed_datetime = parsed_datetime.astimezone(tz)
        return str(converted_parsed_datetime)
    
    return str(parsed_datetime)
