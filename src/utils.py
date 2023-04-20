import os
import sys
import numpy as np
import pandas as pd
import pickle # for creating a pickel file from the mōdel
 
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    try:
        dir_path =os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=False)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("error in save object")
        raise CustomException(e,sys)
    


