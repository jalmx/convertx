# Script to convert pdf to image

Just exec the script inside the folder and get all pdf to convert in png

Supported values are `ppm`, `jpeg`, `png` and `tiff`.

## Usage

```
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
```
## Requirements

For release

```bash
pip install pdf2image
```
## Generate build

For build install

```bash
pip install python-minifier
```

then exec:

```bash
sudo chmod +x ./build.sh # is necessary
./build
```

[Download release](https://raw.githubusercontent.com/jalmx/convert_pdf_img/master/bin/convertx)

Save in your path `$HOME/.local/bin`


## Change permission

change permissions and move to `.local/bin/` or in your PATH

```bash
sudo chmod +x ./bin/convertx
mv bin/convertx $HOME/.local/bin/
```

## Todo

- add to `pypi`
- Read all files from route and colocate in new path