import pandas as pd
import numpy as np
import pickle
import streamlit as st

car = pickle.load(open('C:/Users/bittu.p/Desktop/practice/Car Price Pridiction/car.pkl' , 'rb'))
reg = pickle.load(open('C:/Users/bittu.p/Desktop/practice/Car Price Pridiction/regressor.pkl' , 'rb'))

def car_price_prediction(name, company, year, kms_driven, fuel_type):
    L = []
    prediction = reg.predict(pd.DataFrame([[name, company, year, kms_driven, fuel_type]],
                                          columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    for i in prediction:
        L.append(prediction[0])
    return L   


    
def main():
    st.title('Car Price Prediction')
   
    name =  st.selectbox('Car Model Name', car.name.unique())
    company =  st.selectbox('Company/Brand Name', car.company.unique())
    year = st.text_input('Buying Year of Car')
    kms_driven = st.text_input('How Much Kilometer Car is Drived')
    fuel_type = st.selectbox('Type of Fuel used', ['Petrol', 'Diesel', 'LPG'])
    Price_Prediction = ''
    
    if st.button('Car Price Prediction'):
        Price_Prediction = car_price_prediction(name,  company, year, kms_driven, fuel_type)
        st.success(Price_Prediction)
        
if __name__ == '__main__':
    main()    