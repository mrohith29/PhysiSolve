import pickle
import os
import json

# Replace 'path_to_your_file.pkl' with the actual path to your PKL file
file_path = 'test dataset/data_12_preprocessed.pkl'
# file_path = 'dataset/data_preprocessed.pkl'

# Open the file in binary mode and load the data
with open(file_path, 'rb') as file:
    data = pickle.load(file)

dest_path = 'extracted data/data_12_preprocessed.txt'
# dest_path = 'extracted data/data_preprocessed.txt'

with open(dest_path, 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=4))
