# USHA_ML
USHA-ML-LatrineClassification - See Learning Brief for more detail

<br>

Guidance on Using Python Scripts

Programming projects require consistent and structured files and folders to decrease error rates and improve efficiency when using the model and associated outputs. The following instructions are important to ensure these models run successfully.   

<br>
File and Folder Structure  

Create a permanent folder on your hard drive which will serve as your base folder for the model, add the following subfolders and scripts to this base folder: 

csv - to store the CSV exports from Ona 

images – subfolders for each region can be created under this folder; this is where the model will store downloaded images 

models – stores the Lobe models 

outputs – model outputs are placed here (CSV format) 

src – extra code files 

image_downloader.py – this script will download batches of images from Ona, and shrink/resize them for the model 

run_model.py – this script runs on a folder of images for the selected model (door, floor, structure), leverages the TensorFlow model, and outputs classifications 

<br>

Download images 

Export a CSV file from Ona, save it in the csv folder, and make note of which column has the images you want to classify. The columns have links to the Ona survey folder. Suggest renamed the columns to single words like ‘superstructure’ and ‘interface’ just so you do not have to write out ‘q13b etc etc etc’ 

Make a subfolder inside the images folder to store the downloaded images and point the Python Script to that folder for where to save the images 

Open up command prompt. Two ways to do this: 

Hold down shift and right click, then choose Open command window here 

Run Command Prompt from the start menu and then navigate to your folder by typing cd your/folder/path/here 


In the command prompt type python image_downloader.py 
It will ask you for the name of the CSV file, the column with the image URLs in it from 2a above, and which subfolder you want to store in 
It will start downloading images and saving to the subfolder. When it stops, it’s done! 


<br>  

To run the model 

Open a command prompt as above and type python run_model.py 

It will ask you for the folder the images are in, and which model you want to run by choosing 1, 2 or 3. You can also provide the CSV file again and the column name with the URLs in that file, to be merged with the final output. 

Once you hit enter, you’ll see outputs running very quickly. Once it’s stopped, it’s done. 

It will save a file called output-ddmmYYYY-HHMM.csv where those are the date and time stamp. This file will contain all the info to evaluate the prediction on the 
images given, and if the user provides the original CSV, the prediction evaluation information will be appended to that CSV and saved in the above format.  

<br>  

TensorFlow Model

The TensorFlow models for the Floor, Superstructure, and Door will be made publicly available on the USHA Google Drive and the code is available on this repository on GitHub. Machine learning models require extensive adjustments to avoid things like overfitting and poor accuracy. The iterations on this model and the overall approach to the classification of latrine floors, structure, and door presence are captured in Appendix 1 (Workflow Design). Appendix 2 describes how to run the Python Scripts. 
