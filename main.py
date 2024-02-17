import streamlit as st
from joblib import load

# Define the input fields
age = st.number_input('Age')
gender = st.selectbox('Gender', ['Male', 'Female'])
location = st.selectbox('Location', ['Rural', 'Urban'])
cellphone_access = st.selectbox('Cellphone Access', ['Yes', 'No'])
household_size = st.number_input('Household Size')
education_level = st.selectbox('Education Level', ['No Education', 'Primary', 'Secondary', 'Tertiary'])

# Create the validation button
if st.button('Validate'):
    # Load the ML model
    model = load('Financial_Inclusion_in_Africa.joblib')

    # Preprocess the data
    data = [[age, gender, location, cellphone_access, household_size, education_level]]

    # Make predictions
    prediction = model.predict(data)[0]

    # Display the prediction
    st.write('Prediction:', prediction)
