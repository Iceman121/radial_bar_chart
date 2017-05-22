import pandas as po
import json
from ..global_variables import global_var

path = global_var.path


def import_data():
    data = po.read_csv(path + "/data/raw/input.csv", header=0)
    print(data.head())
    return data


def import_gram_colors():
    with open(path+'/data/external/gram_color.json') as gram_file:
        gram_colors = json.load(gram_file)
    return gram_colors


def import_drug_colors():
    with open(path+'/data/external/drug_color.json') as drug_file:
        drug_colors = json.load(drug_file)
    return drug_colors
