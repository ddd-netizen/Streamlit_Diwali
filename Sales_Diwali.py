import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("Diwali Sales Data Dashboard")

df=pd.read_csv(r'C:\Users\LOLT\OneDrive\Desktop\Streamlit\Diwali Sales Data.csv', encoding='unicode_escape')



#drop unused columns
columns_to_drop = ['Status', 'unnamed1']
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)



col1,col2=st.columns((2))


#select Zone
zone=st.sidebar.multiselect("Select Zone:",df['Zone'].unique())
if not zone:
    df2=df.copy()
else:
    df2=df[df['Zone'].isin(zone)]

#select State

state=st.sidebar.multiselect("Select State:",df2['State'].unique())
filtered_df = df

if not zone and not state:
    filtered_df = df

elif zone and state:
    filtered_df = df2[(df2['Zone'].isin(zone)) & (df2['State'].isin(state))]


total_students = len(df)
st.sidebar.write("Total Students:", total_students)

gender_count = filtered_df['Gender'].value_counts()

gender_counts = filtered_df.groupby(['State','Gender']).size().reset_index(name='Count')
category_df = filtered_df.groupby(by = ["Product_Category"], as_index = False)["Orders"].sum()

col1,col2=st.columns((2))
with col1:
    st.subheader("Gender count")
    fig = px.bar(gender_counts, 
             x='State',
             y='Count',
             color='Gender', 
             barmode='group', 
             title='Gender Distribution Across State',
             template='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 100)

    with col2:
        st.subheader("Product category")
        fig=px.pie(category_df,values="Orders", names="Product_Category", hole=0.5)
        fig. update_traces(text=filtered_df["State"], textposition="inside")
        st.plotly_chart(fig,use_container_width=True)

st.write("Age group Distribution")     
cl1,cl2=st.columns((2))

age_group = filtered_df['Age Group'].value_counts()
age_group = filtered_df.groupby(['Age Group']).size().reset_index(name='Count')


with cl1:

    fig = px.bar(age_group, 
             x='Age Group',
             y='Count',
             color='Age Group', 
             barmode='group', 
             title='Age Group Distribution ',
             template='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 100)

with cl2:

    fig = px.bar(filtered_df, 
             x='Age Group',
             y='Amount',
             barmode='group', 
             title='Amount Distribution ',
             template='seaborn')
    st.plotly_chart(fig,use_container_width=True, height = 100)

chart1,chart2=st.columns((2))
with chart1:
    fig=px.bar(filtered_df,
           x='State',
           y='Orders',
            barmode='group',
            title='State by Order',
            template='seaborn')
    st.plotly_chart(fig, use_container_width=True, height=100)

with chart2:
        st.subheader("Product category")
        fig=px.pie(filtered_df,values="Amount", names="Product_ID", hole=0.5)
        fig. update_traces(text=filtered_df["State"], textposition="inside")
        st.plotly_chart(fig,use_container_width=True)