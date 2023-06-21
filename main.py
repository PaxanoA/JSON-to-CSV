import json 
import pandas as pd

keys = input("Enter the keys you want to extract separated by commas: ").split(',')
locationJSON = r'' #add the path of the JSON file between the single quotes
locationCSV = r'' #add the path for the CSV file between the single quotes
output = r''

keyss = []

def extract_keys(key):
    f = open(locationJSON, "r")
    for l in f:
        for k in key:
            if k in l: #check if the keys are in the document
                keyss.append(l) #add the whole line into the document
            else:
                pass #do nothing if the key is not found. Otherwise it will pop up multiple usless info

#function that converts the JSON file to CSV
def convert_json_to_csv(json_file, csv_file):
    # Read the JSON file into a Pandas DataFrame
    df = pd.read_json(json_file)
    
    # Convert the DataFrame to CSV format
    df.to_csv(csv_file, index=False)
    return "Converted succesfully"

#run the function
extract_keys(keys)
