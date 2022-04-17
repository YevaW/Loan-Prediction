import streamlit as st
import pickle
import pandas as pd
from PIL import Image

st.set_page_config(page_title = 'CDC Finance',
                  layout = "wide", #wide
                  initial_sidebar_state = "expanded",
                  menu_items = {
                      'About' : ' Loan Calculator '
                  })
image = Image.open('carlos-muza-hpjSkU2UYSU-unsplash.jpg')
with open("full_pipe.pkl", "rb") as f:
    pipeline = pickle.load(f)

columns = ['Gender','Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
label = ['Y', 'N']

st.title("CDC Finance Loan Service")
st.image(image)

st.header("Loan Examiner")
'''write down all of the required categories and see if you fit our requirements to send out a loan request'''
Gender = st.selectbox("Gender", ['Male', 'Female'])
Married = st.selectbox("Married", ['Yes', 'No'])
Dependents = st.selectbox("Dependents", ['0', '1', '2', '3+'])
Education = st.selectbox("Education Level", ['Graduate', 'Not Graduate'])
Self_Employed = st.selectbox("Self Employment", ['No', 'Yes'])
ApplicantIncome = st.number_input("Applicant Income")
CoapplicantIncome = st.number_input("Co-Applicant Income")
LoanAmount = st.number_input("Loan Amount")
Loan_Amount_Term = st.number_input("Loan Term")
Credit_History = st.number_input("Credit History")
Property_Area = st.selectbox("Location", ['Urban', 'Rural', 'Semiurban'])

#inference
new_data = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]
new_data = pd.DataFrame([new_data], columns = columns)
res = pipeline.predict(new_data)

st.title('Result')
st.header([res[0]])
'''Explanation :
- 'Y' is equal as Yes, your loan is accepted by the bank as per your condition,
- 'N' is equal as No, your loan is not accepted by the bank as per your condition'''

info1 = st.selectbox("What to do?", ['Your Loan is Accepted', 'Your Loan is Rejected'])

if info1 == ('Your Loan is Accepted'):
    st.subheader('Information')
    '''You can call us at 220499 for further inquiries with our customer service'''
    '''or you can email us at cdcfinancesolution@whereyouare.com for your loan request. You can download the format from our website'''
    '''or you can directly go to our office/branch offices in your city, open every Mon-Fri from 09.00 am to 16 pm'''

elif info1==('Your Loan is Rejected'):
    st.subheader('Information')
    '''You can email us at cdcconsultfinance@whereyouare.com for your conditions and be in touch with our agents.'''
    '''or you can directly go to our office/branch offices in your city, open every Mon-Fri from 09.00 am to 16 pm'''

