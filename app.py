
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib.patches import ConnectionPatch
import plotly.express as px


data = pd.read_csv('https://raw.githubusercontent.com/Alphambarushimana/Grup_3/main/attacks.csv', encoding='iso8859-1')

data.isna().sum()

data.drop(['Case Number', 'Name', 'Injury', 'Time', 'Investigator or Source', 'pdata', 'href formula', 'href', 'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22', 'Unnamed: 23'], axis = 1, inplace = True)


# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Sex ':'Gender'})

# sort the unique values in column Gender into three categories: Female, Male and Unknown

data['Gender'] =  data['Gender'].replace(['M','M ', 'N'],'Male')
data['Gender'] =  data['Gender'].replace(['F'],'Female')
data['Gender'] =  data['Gender'].replace(['.','lli'],'Unknown')
data['Gender'] = data['Gender'].fillna('Unknown')


#from 1900 to 2018
sex_attacks = data.groupby('Gender')['Gender'].count()
sex_attacks = sex_attacks[(sex_attacks.index == 'Male') | (sex_attacks.index=='Female')|(sex_attacks.index=='Unknown')]

gender_fig = px.pie(sex_attacks, values=sex_attacks.values, names=sex_attacks.index, title='Shark Attacks by Gender')
gender_fig.update_layout(height=500, width=600)
gender_fig.show()

data = data[data['Year'] >= 1900]

# Test plot

byYear_attack = data.groupby('Year')['Date'].count().reset_index()
year_fig = px.line(byYear_attack,x='Year', y='Date', title='Shark Attack by Year')
year_fig.show()

## Activities

len(data["Activity"].unique())

# Here making only 1 type, ALlType, so not 9 different provoked unprovked ETC.

data.loc[(data['Type'] == 'Boating') | (data['Type'] == 'Boatomg') | (data['Type'] == 'Boat') | (data['Type'] == 'Questionable') | (data['Type'] == 'Sea Disaster') | (data['Type'] == 'Invalid') | (data['Type'] == 'Provoked') | (data['Type'] == 'Unprovoked'), "Type"] = "AllType"
byType_count = data['Type'].value_counts().reset_index().rename(columns={'Type':'Count','index':'Type'})

# Total amount of attacks based on activity

prov_activity = data[data.Type == 'AllType'].groupby('Activity')['Activity'].count().sort_values(ascending=False)[:10]

activity_fig = px.bar(prov_activity, x=prov_activity.values, y=prov_activity.index, orientation='h', labels={'index':'','x':'Attack Count'},
            title = 'Shark Attacks by Activity')
activity_fig.update_layout(height=600, width=900)
activity_fig.show()

# Fatality

# remove the space in the column name for better syntax and readability

data = data.rename(columns = {'Fatal (Y/N)':'Fatality'})

# sort the unique values in column Fatality into three categories: No, Yes and Unknown

data['Fatality'] =  data['Fatality'].replace(['N', ' N', 'N '],'No')
data['Fatality'] =  data['Fatality'].replace(['Y'],'Yes')
data['Fatality'] =  data['Fatality'].replace(['UNKNOWN', 'M', '2017'],'Unknown')
data['Fatality'] = data['Fatality'].fillna('Unknown')

Mydata = data.groupby(['Fatality', 'Gender'], as_index=False).size()
Mydata = Mydata.sort_values(by=['size'], ascending=False)
Mydata = Mydata[0:7]
Mydata.drop([5],inplace=True)

Mydata.drop([4],inplace=True)
Mydata.drop([6],inplace=True)

import plotly.express as px
mlabels=['Male Non Fatal', 'Male Fatal','Female Non Fatal','Female Fatal']
fatality_fig = px.pie(Mydata, names=mlabels,values='size',hole = 0.8)
fatality_fig.update_traces(textposition='outside', textinfo='percent+label')
fatality_fig.update_layout(
    annotations=[dict(text="comparison of accidents", x=0.5, y=0.5, font_size=20, showarrow=False)])
fatality_fig.update_layout(showlegend=False)
fatality_fig.update_layout(height=500, width=600)


# Location

# Attacks by country

attacks_by_country = data['Country'].value_counts().reset_index().rename(columns={'Country':'Count','index':'Country'})
attacks_by_country.head()

# World map of attacks by country
world_map = px.choropleth(attacks_by_country,
                    locations = 'Country',
                    color = 'Count',
                    color_continuous_scale='Plasma',
                    locationmode = 'country names',
                    scope = 'world',
                    title = 'Shark attacks around the World',
                    labels = {'Count':'Shark attacks'}
                    )

world_map.update_geos(fitbounds="locations", visible=False)
world_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

world_map.show()

st.set_page_config(page_title='Do sharks discriminate - Dashboard',
                    page_icon="????",
                    layout='wide')

st.title('???? SHARK ATTACKZ ????')


tab1, tab2, tab3, tab4, tab5 = st.tabs(["Pie", "Map", "Line", "Sharks", "Test"])

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaper.dog/large/5478970.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

with tab1:
   st.header("Two Pie Charts")
   st.plotly_chart(gender_fig, use_container_width=True)
   st.plotly_chart(fatality_fig, use_container_width=True)


with st.sidebar:
    add_radio = st.radio(
        "Choose a shark attack",
        ("Standard (non-fatal)", "Extreme (fatal)")
    )
    "Done by Group 3"
    "Nadia"
    "Fredrik"
    "Jakob"
    "Alpha"
    "Sadishka"
    "Jannatul"


with tab2:
    st.header("A Map")
    st.plotly_chart(world_map, use_container_width=True)

with tab3:
    st.header("Two Line Charts")
    st.plotly_chart(activity_fig, use_container_width=True)
    st.plotly_chart(year_fig, use_container_width=True)
    x = st.slider("Year 1950-2018", value=50)
    st.write("Slider year:", x)

with tab4:
    st.header("Sharks In Action")
    st.image("https://www.gannett-cdn.com/presto/2021/07/14/NPOH/32c7c45d-5abc-49e5-aa81-71633454f748-greatwhiteshark.jpg?crop=4551,2560,x0,y421&width=3200&height=1801&format=pjpg&auto=webp")
    #def carousel_shark():

        #imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

        #imageUrls = [
            #"https://www.gannett-cdn.com/presto/2021/07/14/NPOH/32c7c45d-5abc-49e5-aa81-71633454f748-greatwhiteshark.jpg?crop=4551,2560,x0,y421&width=3200&height=1801&format=pjpg&auto=webp"
            #"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTFdM8Gq3PfOkhgEZGu9m9R0gCa261_6iYW7w&usqp=CAU"
            #"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvWAl8W2rjbKryJHxFhaWLfZeGC9J0Uk8U3g&usqp=CAU" 
            #"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR9XBB2Zl23vJaOl3PebyKJB-symuQWplEPQ&usqp=CAU"           
            #"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTte-ZrZNkQg67-MVu8Zl8CBM8JlI6zCB0Wpw&usqp=CAU"
            #"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0SHI_1j4zF3OpDr9f9WXGzEhAEo5TEHWfog&usqp=CAU"
       # ]
        #selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)
        #i#f selectedImageUrl is not None:
            #st.image(selectedImageUrl)

    #if __name__ == "__carousel_shark__":
        #carousel_shark()

    st.video("https://www.youtube.com/watch?v=Jo4CLJZwS94&ab_channel=FreeDocumentary-Animals")

with tab5:
    st.header("HEYY")

#byYear_attack = data.groupby('Year')['Date'].count().reset_index()
#year_fig = px.line(byYear_attack,x='Year', y='Date', title='Shark Attack by Year')
#year_fig.show()
   
  