import os
import numpy as np
import pandas as pd


class DataImport:

    def __init__(self) -> None:
        pass

    def load_data(self, base_path):
        base_path = "/content/drive/MyDrive/data/img"
        word_folders = [i for i in os.listdir(base_path) if not i == '.DS_Store']
        # word_folders.remove('.DS_Store')
        print(f"num folders: {len(word_folders)}")
        img_paths = []

        # print(f"base_path: {base_path}")

        # Populate list of image filepaths

        for folder in word_folders:  
            path = os.path.join(base_path,folder)
            word_subfolders = [i for i in os.listdir(path) if not i == '.DS_Store']
            # print(f"folder: {folder}")
            # print(f"path: {path}") 
            for subfolder in word_subfolders:
                newpath = os.path.join(path, subfolder)
                # print(f"subfolder: {subfolder}")
                # print(f"newpath: {newpath}")
                for img in os.listdir(newpath):
                    # print(f"img: {img}")
                    # print(path+"/"+folder+"/"+img)
                    img_path = newpath + "/" + img
                    img_paths.append(img_path)
                    
        print(f"num images: {len(img_paths)}")
        # print(img_paths[444])
