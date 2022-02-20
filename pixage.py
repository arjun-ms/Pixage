import typer


def main():
    
    typer.secho("Welcome to Pixage.", fg=typer.colors.MAGENTA)
    typer.secho("Select values : ", fg=typer.colors.MAGENTA)
    select = input()

    if(select == '0'):
        typer.secho("You have selected 0", fg=typer.colors.BRIGHT_GREEN)
    if(select == '1'):
        typer.secho("You have selected 1", fg=typer.colors.RED)
    if(select == '2'):
        typer.secho("You have selected 2", fg=typer.colors.YELLOW)    

if __name__ == "__main__":
    typer.run(main)
