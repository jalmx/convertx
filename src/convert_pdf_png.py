#!/usr/bin/python3
"""
Simple convert pdf to image
"""

from os import listdir, path
from pathlib import Path
from sys import argv, exit

try:
    from pdf2image import convert_from_path
except:
    try:
        from pip._internal import main as pip
        pip(['install', '--user', 'pdf2image'])
        from pdf2image import convert_from_path
    except:
        from pip._internal import main as pip
        pip(['install', 'pdf2image'])
        from pdf2image import convert_from_path

HELP = """
FOR THE MOMENTO JUST CONVERT TO PNG, A FILE OR FOLDER
Convert a pdf to img o you can give a folder to convert all pdf to img

-f [FORMAT TO CONVERT OUTPUT] `ppm`, `jpeg`, `png` and `tiff`. Default: png
-o [FILE NAME OUTPUT]. Default: Where to exec command. Default: Take same name from file

Example:

convert my_file.pdf # automatic to convert here with the same name in png, output file will be my_file.png
convert my_file.pdf -f tiff -o new_image # output file will be `new_image.tiff`
convert my_file.pdf -f jpeg # output file will be my_file.jpeg
convert /home/user/files # take a folder to convert all files pdf to image
convert /home/user/files -f jpeg # take a folder to convert all files to image in jpeg

Development by Josef Leyva (Xizuth) 
"""


def get_name_file(name, new_name='', count=0,format_file="png") -> Path:

    if count:
        count = f'_{count}'
    else:
        count = ''
    
    if not new_name:        
        return name.replace(f'.{format_file}', f'{count}.{format_file}')
        

    name = str(name).split("/")[-1:][0].split(".")[0]
    return Path(str(name).replace(name, f'{new_name}{count}.{format_file}'))


def convert_file(file, format_file="png", new_name="") -> None:
    """
    Function to convert pdf to image
    :param file: Name file pdf
    :param format_file: format to converter
    :param new_name: new name for the image
    :return: None
    """
    if file.endswith(".pdf"):
        name = file.replace("pdf", format_file.replace(".", ""))
        img = convert_from_path(file)
        
        for i, page in enumerate(img):
            if len(img) > 1:
                i += 1
        
            name_final = get_name_file(name, new_name=new_name, count=i, format_file=format_file)

            print(f"======== Converting {file} to {format_file} ==========")
            print(f"Save to: {name_final}")
            page.save(name_final, format_file.upper().replace(".", ""))
            print(f"========== Done ==========")


def convert_folder(folder="", format_file="png") -> None:
    """
    Convert all files pdf to img
    :param folder: name folder
    :param format_file: format image
    :return: None
    """
    directories = listdir(folder)
    for file in directories:
        convert_file(file, format_file=format_file)


def parse_args(args) -> dict:
    """
    Parse argv and retrieve the arguments and value of
    :param args: arguments for console
    :return dict: with -f format  and -o output name file
    """
    format_img = "png"
    output_name = ""

    for i, arg in enumerate(args):
        if arg == "-f":
            format_img = args[i + 1]
        if arg == "-o":
            output_name = args[i + 1]

    return {"f": format_img, "o": output_name}


def main() -> None:
    """
    Exec the main process to convert
    :return: None
    """
    # print(argv)

    if len(argv) < 2:
        print(HELP)
        exit(1)

    file_name = argv[1]

    format_file = parse_args(argv)["f"]
    output_name = parse_args(argv)["o"]

    if path.isdir(file_name):
        convert_folder(path.abspath(file_name), format_file=format_file)
    else:
        if not file_name.endswith(".pdf"):
            print(HELP)
            exit(1)
        convert_file(file_name, format_file=format_file, new_name=output_name)
    exit(0)


if __name__ == "__main__":
    main()
