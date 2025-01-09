## DATA SCIENCE
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


## FILE PATHS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the PROJECT_PATH variable
project_path = os.getenv("PROJECT_PATH")