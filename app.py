import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to load data
def load_data():
    # Loading the dataset
    data = pd.read_csv('data.csv')
    return data

def plot_department_distribution(data):
    # Counting the frequency of employees in each department
    department_count = data['Department'].value_counts()
    # Creating a bar chart
    fig, ax = plt.subplots()
    department_count.plot(kind='bar', ax=ax)
    ax.set_title("Number of Employees by Department")
    ax.set_xlabel("Department")
    ax.set_ylabel("Number of Employees")
    return fig

def main():
    # App title
    st.title('Basic Streamlit App with Data Visualization')

    # Load data
    data = load_data()

    # Displaying the DataFrame as a table
    st.write("Displaying data:")
    st.table(data.head())  # Display the first 5 rows

    # Plotting and displaying the bar chart
    st.write("Bar chart of number of employees in each department:")
    fig = plot_department_distribution(data)
    st.pyplot(fig)

if __name__ == '__main__':
    main()
