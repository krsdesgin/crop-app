from PIL import Image
import pathlib


box = (10, 610, 1080, 1690) #/ / height/width/ the first two numbers define the top-left coordinates of the outtake (x,y), while the last two define the right-bottom coordinates of the outtake.


for input_img_path in pathlib.Path("input folder").iterdir(): # need to figure out how to ignore .Ds_store

    output_img_path = str(input_img_path).replace("input folder","output folder")
    with Image.open(input_img_path) as im:
        im = im.crop(box) # need to figure out why this is not implementing
        im.save(output_img_path, "png",) # need to figure out why this is not implementing
        print(f"processing file {input_img_path} done...")
