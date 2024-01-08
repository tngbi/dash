# Importing necessary libraries
import streamlit as st
import pandas as pd

# Function to load data
def load_data():
    # Loading a dataset (Ensure the path and file name are correct)
    data = pd.read_csv('data.csv')
    return data

def main():
    # App title
    st.title('Basic Streamlit App')

    # Load data
    data = load_data()

    # Displaying the DataFrame
    st.write("Here's our first attempt at using data to create a table:")
    st.write(data)

    # You can also use the more interactive table display
    st.table(data.head())  # Display the first 5 rows

if __name__ == '__main__':
    main()

