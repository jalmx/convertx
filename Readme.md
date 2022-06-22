# Script to convert pdf to image

Just exec the script inside the folder and get all pdf to convert in png

Supported values are `ppm`, `jpeg`, `png` and `tiff`.

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