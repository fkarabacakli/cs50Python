import sys
from PIL import Image, ImageOps

def main():
    
    length = len(sys.argv)
    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    elif check_valid(sys.argv[1]) != True or check_valid(sys.argv[2]) != True:
        sys.exit("Invalid file type...")
    elif sys.argv[1][-4:]!=sys.argv[2][-4:]:
        sys.exit("Output file must be same file type as Input file...")
    else:
        mask(sys.argv[1],sys.argv[2])


def mask(input_im,output_im):
    try:
        with Image.open("shirt.png") as shirt:
            size = shirt.size
            with Image.open(input_im) as file:
                cropped = ImageOps.fit(file,size)
                Image.Image.paste(cropped, shirt,mask=shirt)
                cropped.save(f"{output_im}",format=None)
    except FileNotFoundError:
        sys.exit("Input file could not found...")


def check_valid(file):
    valid_files_4=[".png",".jpg"]
    valid_files__5=[".jpeg"]
    for i in range(len(valid_files_4)):
        if file[-4:] == valid_files_4[i]:
            return True
    for i in range(len(valid_files__5)):
        if file[-5:] == valid_files__5[i]:
            return True
    return False

main()