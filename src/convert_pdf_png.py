#!/usr/bin/python3
"""
Simple convert pdf to image
"""

from os import listdir, path
from pdf2image import convert_from_path
from sys import argv, exit
from pathlib import Path

HELP = """
FOR THE MOMENTO JUST CONVERT TO PNG, A FILE OR FOLDER
Convert a pdf to img o you can give a folder to convert all pdf to img

-f [FORMAT TO CONVERT OUTPUT] `ppm`, `jpeg`, `png` and `tiff`. Default: png
-o [FILE NAME OUTPUT]. Default: Where to exec command

Example:

convert my_file.pdf # automatic to convert here with the same name in png, output file will be my_file.png
convert my_file.pdf -f tiff -o new_image # output file will be `image.tiff`
convert my_file.pdf -f jpeg # output file will be my_file.jpeg
convert /home/user/files # take a folder to convert all files to image
convert /home/user/files -f jpeg # take a folder to convert all files to image in jpeg
"""


def get_name_file(path_file, new_name) -> Path:
    if not new_name:
        return Path(path_file)

    name = path_file.split("/")[-1:][0].split(".")[0]
    return Path(path_file.replace(name, new_name))


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
        img = img[0] # here can add to convert all pages, a just want the first
        name = get_name_file(name, new_name)

        print(f"======== Converting {file} to {format_file} ==========")
        print(f"Save to: {name}")
        img.save(name, format_file.upper().replace(".", ""))
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


if __name__ == "__main__":
    main()
