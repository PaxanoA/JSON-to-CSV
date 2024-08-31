import json 
import pandas as pd

keys_to_search = str(input("Enter the keys you want to extract separated by commas: ").split(','))
locationJSON = r'C:\Users\andre\OneDrive\Escritorio\ANDRES PACHANO\Projects\JSON-to-CSV\jsonDemoFile.json' #add the path of the JSON file between the single quotes
locationCSV = r'C:\Users\andre\OneDrive\Escritorio\ANDRES PACHANO\Projects\JSON-to-CSV\jsonOutputFile.csv' #add the path for the CSV file between the single quotes
output = r''

keys = []

def extract_keys(key):
    f = open(locationJSON, "r")
    for l in f:
        for k in key:
            if k in l: #check if the keys are in the document
                keys.append(l) #add the whole line into the document
            else:
                pass #do nothing if the key is not found. Otherwise it will pop up multiple usless info

#function that converts the JSON file to CSV
def convert_json_to_csv(json_file, csv_file):
    try:
        # Read the JSON file into a Pandas DataFrame
        df = pd.read_json(json_file)
    
        # Convert the DataFrame to CSV format
        df.to_csv(csv_file, index=False)
        print("Converted succesfully") 
    except:
        return("something went wrong")
    else:
        extract_keys(keys)
