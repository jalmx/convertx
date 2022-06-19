#!/usr/bin/python3

from os import listdir, path
from pdf2image import convert_from_path
from sys import argv, exit
import os

HELP = """
FOR THE MOMENTO JUST CONVERT TO PNG, A FILE OR FOLDER
Convert a pdf to img o you can give a folder to convert all pdf to img

-d [PATH FOLDER] get all files pdf to convert in image
-f [FORMAT TO CONVERT OUTPUT] `ppm`, `jpeg`, `png` and `tiff`. Default: png
-o [FILE NAME OUTPUT]. Default: Where to exec command

Example:

convert my_file.pdf # automatic to convert here with the same name in png, output file will be my_file.png
convert my_file.pdf -f tiff -o img # output file will be img.tiff
convert my_file.pdf -f jpeg # output file will be my_file.jpeg
"""


def convert_file(file, format_file="png"):
    if file.endswith(".pdf"):
        name = file.replace("pdf", format_file)
        img = convert_from_path(file)
        img = img[0]
        print(f"======== Converting {file} to png ==========")
        img.save(name, format_file.upper())
        print(f"========== Done ==========")


def convert_folder(folder="", format_file="png"):
    directories = listdir(folder)
    for file in directories:
        convert_file(file, format_file=format_file)


def main():
    print(argv)

    if len(argv) < 2:
        print(HELP)
        exit(1)

    file_name = argv[1]
    print(file_name)

    if path.isdir(file_name):
        convert_folder(path.abspath(file_name))
    else:
        if not file_name.endswith(".pdf"):
            print(HELP)
            exit(1)
        convert_file(file_name)

if __name__ == "__main__":
    main()
