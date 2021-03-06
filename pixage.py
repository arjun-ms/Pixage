import typer
from PIL import Image
import os
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
app = typer.Typer()
argumentList = sys.argv


@app.command()
def topng(path: str):
    if(path.lower().endswith(('.jpg', '.jpeg'))):
        image = Image.open(path)
        file = os.path.splitext(path)[0]
        # print(file)
        image.save(f"{file}.png")
        typer.secho("Image Converted to PNG and Saved! 👍", fg=typer.colors.GREEN)
    else:
        typer.secho("Pass a JPEG or JPG file.", fg=typer.colors.RED,bold=True)
        options()
    exit()


@app.command()
def tojpg(path: str):
    if(path.lower().endswith(('.png'))):
        image = Image.open(path)
        file = os.path.splitext(path)[0]
        # print(file)
        image.save(f"{file}.jpg")
        typer.secho("Image Converted to JPG and Saved! 👍", fg=typer.colors.GREEN)
    else:
        typer.secho("Pass a PNG file.", fg=typer.colors.RED,bold=True)
        options()
    exit()


@app.command()
def reduce(path: str, factor: int):
    image = Image.open(path)
    resized_img = image.resize((round(image.size[0]/factor), round(image.size[1]/factor)))
    file, ext = os.path.splitext(path)
    print(file, ext)
    resized_img.save(f"{file}_reduced{ext}")
    typer.secho("Image Size Reduction Has Done Successfully! 👍", fg=typer.colors.GREEN)
    exit()


@app.command()
def enlarge(path: str, factor: int):
    image = Image.open(path)
    resized_img = image.resize((round(image.size[0]*factor), round(image.size[1]*factor)))
    file, ext = os.path.splitext(path)
    print(file, ext)
    resized_img.save(f"{file}_enlarged{ext}")
    typer.secho("Image Size Enlargment Has Done Successfully! 👍", fg=typer.colors.GREEN)
    exit()


@app.command()
def help():
    typer.secho('''⓵ python pixage.py topng [FILEPATH] - To Convert JPEG or JPG image to PNG format.

⓶ python pixage.py tojpg [FILEPATH] - To Convert PNG image to JPEG or JPG format.

⓷ python pixage.py reduce [FILEPATH] [FACTOR] - To reduce/shrink the size of the image by a factor. 
    Eg : pixage reduce /home/abc/efg/pic.jpeg 2 ➭ reduces the image size by half.

⓸ python pixage.py enlarge [FILEPATH] [FACTOR] - To enlarge/increase the size of the image by a factor.
    Eg : pixage enlarge /home/abc/efg/pic.jpeg 2 ➭ enlarges the image size by 2x.

⓹ python pixage.py help - To guide you.''',
    fg=typer.colors.BRIGHT_BLUE,bold=True)



def options():
    print()

    typer.secho('''Select any value :
                1 - JPEG TO PNG 
                2 - PNG TO JPEG
                3 - ENLARGE IMAGE SIZE
                4 - REDUCE IMAGE SIZE
                5 - HELP
                6 - EXIT''', fg=typer.colors.BRIGHT_YELLOW, bold=True)
    select = input("➤")

    if(select == '1'):
        typer.secho("You have selected 1", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.YELLOW+"Paste the file path here (without quotes): ")
        topng(path)

    elif(select == '2'):
        typer.secho("You have selected 2", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.YELLOW+"Paste the file path here (without quotes): ")
        tojpg(path)

    elif(select == '3'):
        typer.secho("You have selected 3", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.YELLOW+"Paste the file path here: ")
        if(path.lower().endswith(('.png','.jpg', '.jpeg'))):
            pass
        else:
            typer.secho("Pass a PNG or JPEG or JPG file.", fg=typer.colors.RED,bold=True)
            options()
        try:
            percent = int(input(Fore.YELLOW+"By how much times you want to enlarge: "))
        except Exception:
            typer.secho("Pass an Integer value.", fg=typer.colors.RED,bold=True)
            options()
        enlarge(path, percent)

    elif(select == '4'):
        typer.secho("You have selected 4", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.YELLOW+"Paste the file path here: ")
        if(path.lower().endswith(('.png','.jpg', '.jpeg'))):
            pass
        else:
            typer.secho("Pass a PNG or JPEG or JPG file.", fg=typer.colors.RED,bold=True)
            options()
        try:
            percent = int(input(Fore.YELLOW+"By how much times you want to reduce: "))
        except Exception:
            typer.secho("Pass an Integer value.", fg=typer.colors.RED,bold=True)
            options()
        reduce(path, percent)
    
    elif(select == '5'):
        help()
        options()

    elif(select == '6'):
        exit()

    else:
        typer.secho("You have given an invalid input ❌", fg=typer.colors.BRIGHT_RED, bold=True)
        options()



def main():
    banner = '''
        ██████╗ ██╗██╗  ██╗ █████╗  ██████╗ ███████╗
        ██╔══██╗██║╚██╗██╔╝██╔══██╗██╔════╝ ██╔════╝
        ██████╔╝██║ ╚███╔╝ ███████║██║  ███╗█████╗  
        ██╔═══╝ ██║ ██╔██╗ ██╔══██║██║   ██║██╔══╝  
        ██║     ██║██╔╝ ██╗██║  ██║╚██████╔╝███████╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

    ███▓▒­░⡷⠂𝙰𝚞𝚝𝚑𝚘𝚛 : 𝓐𝓻𝓳𝓾𝓷 𝓜 𝓢 & 𝓜𝓾𝓱𝓪𝓶𝓶𝓮𝓭 𝓐𝓳𝓶𝓪𝓵 𝓜 ⠐⢾░▒▓██                                
    '''
    print(Fore.WHITE+Style.NORMAL+banner)
    typer.secho("Welcome to Pixage.", fg=typer.colors.BRIGHT_CYAN)
    options()

if __name__ == "__main__":
    if(len(argumentList) <= 1):
        main()
    app()

