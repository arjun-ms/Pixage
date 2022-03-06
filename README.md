# Pixage
⚒️ A Command Line Tool to resize and change formats of Images

## Team members
1. Muhammed Ajmal M [https://github.com/ajmalmohad]
2. Arjun M S [https://github.com/arjun-ms]

## Team Id
Team id here

## Link to product walkthrough
[link to video]

## How it Works ?
1. It converts .jpg to .png and .png to .jpg by file naming
2. It enlarges and reduces images by multiplying dimensions

## Libraries used
- Pillow - 9.0.1
- typer - 0.4.0

## How to configure
1. Clone the Repository
```console
    git clone https://github.com/arjun-ms/Pixage.git
```
2. Change directory
```console
    cd Pixage
```
3. Create a Venv (Optional)
```console
    virtualenv venv
```
4. Activate Venv (Optional)
```console
    .\venv\Scripts\activate
```
5. Install Required Packages
```console
    pip install -r requirements.txt
```
6. Run Pixage and Enjoy
```console
    python pixage.py
```

## How to Run
- Run (Menu Driven)
```console
    python pixage.py
```

- Run (Direct CLI Commands)

1. JPG to PNG
``` console
    pixage.py topng [FILEPATH]
```
2. PNG to JPG
``` console
    pixage.py tojpg [FILEPATH]
```
3. Reduce
``` console
    pixage.py reduce [FILEPATH] [FACTOR]
```
4. Enlarge
``` console
    pixage.py enlarge [FILEPATH] [FACTOR]
```
5. Help
```console
    pixage.py help
```