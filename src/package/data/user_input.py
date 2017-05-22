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


# Import Data
def import_data():
    print("Importing Raw Data...")
    data = po.read_csv(path + "/data/raw/input.csv", header=0)
    print(data.head())
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
