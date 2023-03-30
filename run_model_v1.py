import pandas as pd
import os
from PIL import Image
import sys
sys.path.insert(0, "C:\\Users\\lauren.allognon\\USHA-ML") #update pathname
from src.tf_loader2 import TFModel
import time

#set current directory as root
ROOT = os.path.dirname(__file__)

#function to open image and run model
#returns nested objects:
#single item dict w key 'predictions' and value:
#   list containing one dict per output label containing keys:
#       label, confidence
def run_model(image):
    if os.path.isfile(image):
        image = Image.open(image)
        outputs = model.predict(image)
        print(f"Predicted: {outputs}")
        return outputs
    else:
        print(f"Couldn't find image file {image}")

# run this
if __name__ == '__main__':
    #get inputs from user
    image_dir = input("What is the subfolder in images? ")
    csv_file = input("What is the name of the CSV file? ")
    col = input('What is the column name of image URLs? ')
    model_name = input("What model are you evaluating? (1) Superstructure (2) Interface (3) Presence of door ")

    #load selected model
    if int(model_name) == 1:
        model = TFModel(model_dir=os.path.join(ROOT,'models','structure'))
    elif int(model_name) == 2:
        model = TFModel(model_dir=os.path.join(ROOT,'models','slab'))
    elif int(model_name) == 3:
        model = TFModel(model_dir=os.path.join(ROOT,'models','door'))
    else:
        print('Invalid model')
        sys.exit()
    model.load()

    images = os.listdir(os.path.join(ROOT,'images',image_dir))
    results = pd.DataFrame()
    #run model and append results to dataframe
    for image in images:
        output = run_model(os.path.join(ROOT,'images',image_dir, image))
        result = pd.DataFrame(output['predictions']).set_index('label').T
        result['image'] = image
        results = results.append(result)
    results.reset_index(drop=True, inplace=True)
    
    cols = results.columns[:-1]
    results['max_conf'] = results[cols].max(axis=1)
    results['doubt'] = (results.loc[:, cols] > .25).sum(axis=1)
    results['accuracy'] = pd.cut(results.max_conf, bins=[0,.5,.85,.95,1], labels=['V Low', 'Low', 'Med', 'High'])
    results['model_output'] = results[cols].idxmax(axis=1)

    data = pd.read_csv(os.path.join(ROOT,'csv',csv_file),index_col='uuid')
    data['image'] = data[col].str[-17:]
    data = data.merge(results, how='left', on='image')

    #output to CSV
    fname = 'output-' + time.strftime('%d%m%Y-%H%M') + '.csv'
    data.to_csv(os.path.join(ROOT,'outputs',fname))
    print('Saved ' + fname)