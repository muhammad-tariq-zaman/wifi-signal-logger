import re
def parse_proc_wireless(text):
    """Parse /proc/net/wireless-style text into {interface: signal_dbm}."""
    out = {}
    for line in text.splitlines():
        m = re.match(r"\s*(\w+):\s+\d+\s+[\d.]+\s+(-?\d+)\.", line)
        if m: out[m.group(1)] = int(m.group(2))
    return out
def current():
    try:
        return parse_proc_wireless(open("/proc/net/wireless").read())
    except OSError:
        return {}
if __name__ == "__main__":
    sig = current()
    print(sig if sig else "No wireless interfaces found (or not on Linux).")
