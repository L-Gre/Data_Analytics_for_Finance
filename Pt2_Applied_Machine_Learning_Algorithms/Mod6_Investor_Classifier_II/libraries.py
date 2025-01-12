## data science

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

from sklearn.pipeline import make_pipeline # to set up the steps you follow with each model
from sklearn.preprocessing import StandardScaler # to undo the influence of magnitude of large values

from sklearn.linear_model import LogisticRegression # L1 and L2
from sklearn.ensemble import RandomForestClassifier # rf
from sklearn.ensemble import GradientBoostingClassifier # gb

## functions

import pickle

def save_to_pickle(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_from_pickle(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# # Example usage
# my_dict = {"key1": "value1"}
# save_to_pickle(my_dict, "my_dict.pkl")
# loaded_dict = load_from_pickle("my_dict.pkl")


## file path vars

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the PROJECT_PATH variable
project_path = os.getenv("PROJECT_PATH")