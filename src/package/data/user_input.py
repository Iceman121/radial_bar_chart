# ==============================================================================
# Chapter 1: Importing Data Related Modules
# ==============================================================================
# For storing bar chart data
import pandas as po
# For gram and drug colors
import json
# For path details
import os


# ==============================================================================
# Defining Attributes and Methods for Use
# ==============================================================================
# Get Path
path = os.getcwd()


# Get Files List
def list_files():
    files_list = po.DataFrame(os.listdir(path+'/data/raw/'),
                              columns=['Files'])
    files_list = files_list.reset_index()
    files_list.columns = ['ID', 'Files']
    return files_list


# Import Data
def import_data():
    print('Available Files for import: ')
    files_list = list_files()
    print(files_list)
    print()
    # User Input for identifying which file to convert
    choice = int(input('Please enter the file ID you want to convert: '))
    file_name = str(files_list.ix[files_list['ID'] == choice,
                                  'Files'].values[0])
    print()
    print("Importing Raw Data...")
    data = po.read_csv(path + "/data/raw/"+file_name, header=0)
    print(data.head())
    print()
    return data


# Import Gram Color Data
def import_gram_colors():
    print("Importing Gram Color settings...")
    with open(path+'/data/external/gram_color.json') as gram_file:
        gram_colors = json.load(gram_file)
    return gram_colors


# Import Drug Color Data
def import_drug_colors():
    print("Importing Drug Color settings...")
    with open(path+'/data/external/drug_color.json') as drug_file:
        drug_colors = json.load(drug_file)
    return drug_colors
