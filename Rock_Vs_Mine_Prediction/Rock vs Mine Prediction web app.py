# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:08:41 2024

@author: Manjusha
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('F:/ML_Projects/Rock_Vs_Mine_Prediction/sonar_model.sav','rb'))

# creating a function for prediction

def rockMinePrediction(input_data):
    
    #changing the input array to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    #reshape the numpy array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]=='R'):
      return 'The Object is a Rock'
    else:
      return 'The Object is a Mine'
  
    
def main():
    
    st.title('Rock vs Mine Prediction Web App')
    
    # getting the input data from the user
    
    i1 = st.text_input('input1')
    i2 = st.text_input('input2')
    i3 = st.text_input('input3')
    i4 = st.text_input('input4')
    i5 = st.text_input('input5')
    i6 = st.text_input('input6')
    i7 = st.text_input('input7')
    i8 = st.text_input('input8')
    i9 = st.text_input('input9')
    i10 = st.text_input('input10')
    i11 = st.text_input('input11')
    i12 = st.text_input('input12')
    i13 = st.text_input('input13')
    i14 = st.text_input('input14')
    i15 = st.text_input('input15')
    i16= st.text_input('input16')
    i17= st.text_input('input17')
    i18= st.text_input('input18')
    i19= st.text_input('input19')
    i20= st.text_input('input20')
    i21= st.text_input('input21')
    i22= st.text_input('input22')
    i23 = st.text_input('input23')
    i24 = st.text_input('input24')
    i25 = st.text_input('input25')
    i26 = st.text_input('input26')
    i27= st.text_input('input27')
    i28= st.text_input('input28')
    i29= st.text_input('input29')
    i30= st.text_input('input30')
    i31= st.text_input('input31')
    i32= st.text_input('input32')
    i33= st.text_input('input33')
    i34= st.text_input('input34')
    i35= st.text_input('input35')
    i36 = st.text_input('input36')
    i37 = st.text_input('input37')
    i38 = st.text_input('input38')
    i39 = st.text_input('input39')
    i40= st.text_input('input40')
    i41= st.text_input('input41')
    i42= st.text_input('input42')
    i43= st.text_input('input43')
    i44= st.text_input('input44')
    i45= st.text_input('input45')
    i46= st.text_input('input46')
    i47= st.text_input('input47')
    i48= st.text_input('input48')
    i49 = st.text_input('input49')
    i50 = st.text_input('input50')
    i51 = st.text_input('input51')
    i52 = st.text_input('input52')
    i53= st.text_input('input53')
    i54= st.text_input('input54')
    i55= st.text_input('input55')
    i56= st.text_input('input56')
    i57 = st.text_input('input57')
    i58 = st.text_input('input58')
    i59 = st.text_input('input59')
    i60 = st.text_input('input60')
    
    # code for prediction
    result = ''
    
    #creating button for prediction
    
    if st.button('Rock or Mine'):
        result = rockMinePrediction([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20, i21, i22, i23, i24, i25, i26, i27, i28, i29, i30, i31, i32, i33, i34, i35, i36, i37, i38, i39, i40, i41, i42, i43, i44, i45, i46, i47, i48, i49, i50, i51, i52, i53, i54, i55, i56, i57, i58, i59, i60])
    
    st.success(result)
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    