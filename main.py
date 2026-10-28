import typer
import time
import sys

app = typer.Typer()


@app.command()
def timer(remaining: int):
    for remaining in range(10, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
        sys.stdout.flush()
        time.sleep(1)



if __name__ == "__main__":
    app()