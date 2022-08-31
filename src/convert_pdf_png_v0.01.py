from os import listdir
from pdf2image import convert_from_path

def main():
    directories = listdir(".")
    for file in directories:
        if file.endswith(".pdf"):
            format_img = "png"
            name = file.replace("pdf", format_img)
            img = convert_from_path(file)
            img = img[0]
            print(f"======== Converting {file} to png ==========")
            img.save(name, format_img.upper())
            print(f"========== Done ==========")
    
if __name__ == "__main__":
    main()