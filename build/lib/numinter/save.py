import numpy as np

def save(input_data):
#    input_data
    np.savetext("data.csv", input_data, delimiter="\t")
