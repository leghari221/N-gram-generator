# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNjnyRfr713OfVdnuj5Msjh7N33tp-Mi
"""

# Import necessary libraries
import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Title of the web application
st.title('N-gram Generator')

# User input
user_input = st.text_input("Enter a text passage:")

# Slider for the user to select n-gram
n = st.slider('Select the n for n-gram:', min_value=1, max_value=15)

# Function to generate n-grams
def generate_ngrams(text, n):
    token = word_tokenize(text)
    n_grams = list(ngrams(token, n))
    return n_grams

# Generate and display n-grams
if st.button('Generate N-grams'):
    if user_input:
        n_grams = generate_ngrams(user_input, n)
        st.write(n_grams)
    else:
        st.write("Please enter a text passage.")