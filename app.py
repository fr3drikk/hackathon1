
import streamlit as st
import numpy as np # Basic library for all kind of numerical operations
import pandas as pd # Basic library for data manipulation in dataframes
import matplotlib.pyplot as plt # comand for ploting
import seaborn as sns; sns.set() # this is a data visualization library built on top of matplotlib
from matplotlib.patches import ConnectionPatch # using this for later when zooming
import plotly.express as px # Plotly plots

data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')
data #showing the data



st.title('Shark attacks - GROUP 3 BABY')
