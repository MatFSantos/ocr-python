import re

def match(regex, str, dotAll: bool = False) -> str | None:
    if regex:
        is_match = re.search(regex, str, re.DOTALL) if dotAll else re.search(regex, str)
        if is_match:
            return is_match.group(1)
    return None