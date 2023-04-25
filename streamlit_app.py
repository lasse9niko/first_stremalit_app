import streamlit
import pandas

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the table on the page.
streamlit.title('My place to eat')
streamlit.header('Breakfast favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice!')
#streamlit.text('What fruit would you like information about?')

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)

# new section to display fruityvice api response
import requests
fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{fruit_choice}")

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

fruit_to_list = streamlit.text_input('What fruit would you like to add to the list?', 'Kiwi')
streamlit.write('The user entered', fruit_to_list)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


