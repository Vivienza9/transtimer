import math
import re
import sys
import time

import typer


def parse_time(time: str):
    secs = 0.0
    conversions = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    matches = re.findall("(\\d*\\.?\\d*)([dhms])", time.lower())
    for match in matches:
        secs += float(match[0]) * conversions[match[1]]
    return math.floor(secs)

app = typer.Typer()


@app.command()
def timer(duration: str):
    secs = parse_time(duration)
    for remaining in range(secs, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining:2d} seconds remaining.") 
        sys.stdout.flush()
        time.sleep(1)



if __name__ == "__main__":
    app()
