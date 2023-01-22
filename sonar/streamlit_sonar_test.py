

import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd 
from sklearn.preprocessing import LabelEncoder, StandardScaler


st.set_option('deprecation.showfileUploaderEncoding',False)

#Title of the page
st.title("Sonar Classification")  
st.text("Provide sonar data")

# To reduce the loading model every time
@st.cache(allow_output_mutation=True)


#load model
def load_model():
    model=tf.keras.models.load_model("sonar_NEW_data.h5")
    return model

#Model is loading into the memory
with st.spinner('Loding model into memory'):
        model=load_model()


#Providing Title to the side Bar
st.sidebar.title("Myelin Foundry")

#the file which needs to be get uploaded
data_file=st.sidebar.file_uploader("Select File",type=['csv'])


if data_file is not None:

    #Uploaded data variable should be passed to read in Dataframe
    data = pd.read_csv(data_file,header=None)

    #Dataframe displayed  in UI
    st.dataframe(data)
    

    #for selecting rows we are providing the len of data 
    row=st.sidebar.slider("select_row", 0, len(data[0]))
    
    # droping the column name 60 which has Ground truth
    x = data.drop(columns = [60])
    
    # Making a copy of the variable in x1
    x1=x

    #passing  x through Standard Scaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(x)

    #Again passing the variable to dataframe
    convert_2_dataframe=pd.DataFrame(X_scaled)

    #taking the copy of the data x1 for predicting rows and plotting graph
    y1=x1.iloc[row]
    
    #to get the particular row of data to be processed
    rows_needs_to_be_selected=convert_2_dataframe.iloc[row]
    
    #converting to np.asarray for the purpose of model input
    array_converting=np.asarray(rows_needs_to_be_selected)

    #Reshaping the array for the model acceptance shape
    reshaping=array_converting.reshape(1,60)


    #plotting the chart in UI
    st.line_chart(y1)


    
    with st.spinner("classifying...."):

        #predicting the model
        label=model.predict(reshaping)
        
        #classifing the output based on threshold
        if label >= 0.5:
            original_title = '<p style="font-family:Courier; color:Green; font-size: 40px;"><b>Predicted Class: Rock</b></p>'
            st.markdown(original_title,unsafe_allow_html=True)
            #st.header("Predicted Class: ROCK")
            
        else:
            original_title = '<p style="font-family:Courier; color:Red; font-size: 40px;"><b> Predicted Class: Mine</b></p>'
            st.markdown(original_title,unsafe_allow_html=True)
            

        #showing the Precision and recall
        st.sidebar.header("Classfication Rate : 74%")
        
else:
    st.write("Waiting for Data")
