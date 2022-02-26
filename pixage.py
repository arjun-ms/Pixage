import typer
from PIL import Image
import os

app = typer.Typer()

@app.command()
def topng(path: str):
    if(path.lower().endswith(('.jpg','.jpeg'))):
        image = Image.open(path)
        file = os.path.splitext(path)[0]
        print(file)
        image.save(f"{file}.png")
    else:
        typer.secho("Pass a JPEG or JPG file.", fg=typer.colors.RED)
# def main():
    
#     typer.secho("Welcome to Pixage.", fg=typer.colors.MAGENTA)
#     typer.secho("Select values : ", fg=typer.colors.MAGENTA)
#     select = input()

#     if(select == '0'):
#         typer.secho("You have selected 0", fg=typer.colors.BRIGHT_GREEN)
#     if(select == '1'):
#         typer.secho("You have selected 1", fg=typer.colors.RED)
#     if(select == '2'):
#         typer.secho("You have selected 2", fg=typer.colors.YELLOW)    

if __name__ == "__main__":
    # typer.run(main)
    app()