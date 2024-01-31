import streamlit
streamlit.title('my parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 avocado Toast')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.AP_SOUTHEAST_2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
