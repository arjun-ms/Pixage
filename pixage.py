import typer
from PIL import Image
import os
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
app = typer.Typer()


@app.command()
def topng(path: str):
    if(path.lower().endswith(('.jpg', '.jpeg'))):
        image = Image.open(path)
        file = os.path.splitext(path)[0]
        # print(file)
        image.save(f"{file}.png")
    else:
        typer.secho("Pass a JPEG or JPG file.", fg=typer.colors.RED)


@app.command()
def reduce(path: str, percent: int):
    image = Image.open(path)
    percent = percent/100
    resized_img = image.resize(
        (round(image.size[0]*percent), round(image.size[1]*percent)))
    file, ext = os.path.splitext(path)
    print(file, ext)
    resized_img.save(f"{file}_reduced{ext}")
    typer.secho("Image Size Reduction Has Done Successfully! 👍",
                fg=typer.colors.GREEN)


@app.command()
def enlarge(path: str, percent: int):
    image = Image.open(path)
    percent = percent/100
    resized_img = image.resize(
        (round(image.size[0]/percent), round(image.size[1]/percent)))
    file, ext = os.path.splitext(path)
    print(file, ext)
    resized_img.save(f"{file}_enlarged{ext}")
    typer.secho("Image Size Enlargment Has Done Successfully! 👍",
                fg=typer.colors.GREEN)

@app.command()
def help():
    typer.secho('''⓵ pixage.py topng [FILEPATH] - To Convert JPEG or JPG image to PNG format.
⓶ pixage.py tojpg [FILEPATH] - To Convert PNG image to JPEG or JPG format.
⓷ pixage.py reduce [FILEPATH] [PERCENTAGE] - To reduce/shrink the size of the image.
⓸ pixage.py enlarge [FILEPATH] [PERCENTAGE] - To enlarge/increase the size of the image.
⓹ pixage.py help - To guide you.
                ''',
                fg=typer.colors.GREEN)
    


def main():
    banner = '''
        ██████╗ ██╗██╗  ██╗ █████╗  ██████╗ ███████╗
        ██╔══██╗██║╚██╗██╔╝██╔══██╗██╔════╝ ██╔════╝
        ██████╔╝██║ ╚███╔╝ ███████║██║  ███╗█████╗  
        ██╔═══╝ ██║ ██╔██╗ ██╔══██║██║   ██║██╔══╝  
        ██║     ██║██╔╝ ██╗██║  ██║╚██████╔╝███████╗
        ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

        ████▓▒­░⡷⠂𝙰𝚞𝚝𝚑𝚘𝚛 : 𝙰𝚛𝚓𝚞𝚗 𝙼 𝚂 & 𝙸𝚗𝚊𝚖⠐⢾░▒▓████                                        
'''

    print(Fore.WHITE+Style.NORMAL+banner)
    typer.secho("Welcome to Pixage.", fg=typer.colors.BRIGHT_CYAN)
    print()

    typer.secho('''Select values :
                1 - JPEG TO PNG 
                2 - PNG TO JPEG
                3 - ENLARGE IMAGE SIZE
                4 - REDUCE IMAGE SIZE
                5 - HELP''', fg=typer.colors.BRIGHT_YELLOW, bold=True)
    select = input("➭")

    if(select == '1'):
        typer.secho("You have selected 1", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.RED+"Paste the file path here: ")
        topng(path)

    elif(select == '2'):
        typer.secho("You have selected 2", fg=typer.colors.BRIGHT_GREEN)

    elif(select == '3'):
        typer.secho("You have selected 3", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.RED+"Paste the file path here: ")
        percent = input(Fore.RED+"Paste the file path here: ")
        enlarge(path, percent)

    elif(select == '4'):
        typer.secho("You have selected 4", fg=typer.colors.BRIGHT_GREEN)
        path = input(Fore.RED+"Paste the file path here: ")
        percent = input(Fore.RED+"Paste the file path here: ")
        reduce(path, percent)
    
    elif(select == '5'):
        help()

    else:
        typer.secho("You have given an invalid input ❌",
                    fg=typer.colors.BRIGHT_RED, bold=True)


if __name__ == "__main__":
    main()
    app()

