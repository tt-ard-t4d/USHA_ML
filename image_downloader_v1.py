import requests
from PIL import Image
import pandas as pd
import os
import certifi
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ROOT = os.path.dirname(__file__)

def fetch_images(url_list, dest_folder):
    for url in url_list:
        img_name=url[-17:]
        img_path = os.path.join(ROOT,'images',dest_folder,img_name)
        if not os.path.exists(img_path):
            print('Downloading ' + img_name)
            try:
                image = Image.open(requests.get(url, stream=True, verify=False).raw)
                image = resize(image)
                image.save(img_path)
            except Exception as e:
                print('Error on ' + img_name)
                print(e)
                pass
        else:
            print('Skipping ' + img_name)

def resize(image):
    width, height = image.size
    if width != height:
        square_size = min(width, height)
        left = (width - square_size) / 2
        top = (height - square_size) / 2
        right = (width + square_size) / 2
        bottom = (height + square_size) / 2
        image = image.crop((left, top, right, bottom))
    image_sm = image.resize((512,512))
    return image_sm



if __name__ == '__main__':
    csv_file = input("What is the name of the CSV file, in the CSV folder? ")
    col = input('What is the column name of image URLs? ')
    dest_folder = input("Where would you like to put the images (inside the images folder)? ")

    df = pd.read_csv(os.path.join(ROOT,'csv',csv_file))
    df.dropna(axis=0, subset=[col], inplace=True)
    urls = list(df[df[col].str.contains('http')][col])
    fetch_images(urls, dest_folder)