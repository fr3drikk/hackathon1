

import streamlit as st
import numpy as np # Basic library for all kind of numerical operations
import pandas as pd # Basic library for data manipulation in dataframes
import matplotlib.pyplot as plt # comand for ploting
import seaborn as sns; sns.set() # this is a data visualization library built on top of matplotlib
from matplotlib.patches import ConnectionPatch # using this for later when zooming
import plotly.express as px # Plotly plots

st.title('Shark attacks - GROUP 3 BABY')


data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')


ata.info()

data.isna().sum()

data.drop(['Case Number', 'Name', 'Injury', 'Time', 'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis = 1, inplace = True)

data.info()

data.columns

# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Sex ':'Gender'})

data.Gender.unique()

# sort the unique values in column Gender into three categories: Female, Male and Unknown

data['Gender'] =  data['Gender'].replace(['M','M ', 'N'],'Male')
data['Gender'] =  data['Gender'].replace(['F'],'Female')
data['Gender'] =  data['Gender'].replace(['.','lli'],'Unknown')
data['Gender'] = data['Gender'].fillna('Unknown')

data.Gender.value_counts()

#from 1900 to 2018
sex_attacks = data.groupby('Gender')['Gender'].count()
sex_attacks = sex_attacks[(sex_attacks.index == 'Male') | (sex_attacks.index=='Female')|(sex_attacks.index=='Unknown')]
sex_attacks

fig = px.pie(sex_attacks, values=sex_attacks.values, names=sex_attacks.index, title='Shark Attacks by Gender')
fig.update_layout(height=500, width=600)
st.plotly_chart(fig, use_container_width=True)


#from 2010 - 2018 
sex_attacks_2010_2018 = data[data.Year >= 2010].groupby('Gender')['Gender'].count()
sex_attacks_2010_2018 = sex_attacks_2010_2018[(sex_attacks_2010_2018.index == 'Male') | (sex_attacks_2010_2018.index =='Female')| (sex_attacks_2010_2018.index=='Unknown')]
sex_attacks

fig = px.pie(sex_attacks_2010_2018, values=sex_attacks_2010_2018.values, names=sex_attacks_2010_2018.index, 
             title='Shark Attacks by Gender - Between 2010-2018')
fig.update_layout(height=500, width=600)
fig.show()

data.Year.unique()

data = data[data['Year'] >= 1900]

data.Year.unique()

# Test plot

byYear_attack = data.groupby('Year')['Date'].count().reset_index()
fig = px.line(byYear_attack,x='Year', y='Date', title='Shark Attack by Year')
fig.show()



## Activities

data.Activity.unique()

len(data["Activity"].unique())

data.Activity.value_counts().head(10)

## TYPE
data.Type.unique()

# Here making only 1 type, ALlType, so not 9 different provoked unprovked ETC.

data.loc[(data['Type'] == 'Boating') | (data['Type'] == 'Boatomg') | (data['Type'] == 'Boat') | (data['Type'] == 'Questionable') | (data['Type'] == 'Sea Disaster') | (data['Type'] == 'Invalid') | (data['Type'] == 'Provoked') | (data['Type'] == 'Unprovoked'), "Type"] = "AllType"
byType_count = data['Type'].value_counts().reset_index().rename(columns={'Type':'Count','index':'Type'})
byType_count

# Total amount of attacks based on activity

prov_activity = data[data.Type == 'AllType'].groupby('Activity')['Activity'].count().sort_values(ascending=False)[:10]

fig = px.bar(prov_activity, x=prov_activity.values, y=prov_activity.index, orientation='h', labels={'index':'','x':'Attack Count'},
            title = 'Shark Attacks by Activity')
fig.update_layout(height=600, width=900)
fig.show()

# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Fatal (Y/N)':'Fatality'})

data.Fatality.unique()

# sort the unique values in column Fatality into three categories: No, Yes and Unknown

data['Fatality'] =  data['Fatality'].replace(['N', ' N', 'N '],'No')
data['Fatality'] =  data['Fatality'].replace(['Y'],'Yes')
data['Fatality'] =  data['Fatality'].replace(['UNKNOWN', 'M', '2017'],'Unknown')
data['Fatality'] = data['Fatality'].fillna('Unknown')

data.Fatality.value_counts()
