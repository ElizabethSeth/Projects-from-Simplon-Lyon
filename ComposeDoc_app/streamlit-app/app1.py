import os
import streamlit as st
from pymongo import MongoClient
import pandas as pd


mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client.db_listing
listings_collection = db.listing_sql

# Function to fetch data from MongoDB and convert it to a DataFrame


def get_data():
    listings = listings_collection.find()
    data = []
    for listing in listings:
        listing['_id'] = str(listing['_id'])  # Convert ObjectId to string
        # Convert Decimal128 fields to float
        if 'price' in listing and listing['price'] is not None:
            listing['price'] = float(listing['price'].to_decimal())
        if 'cleaning_fee' in listing and listing['cleaning_fee'] is not None:
            listing['cleaning_fee'] = float(
                listing['cleaning_fee'].to_decimal())
        if 'extra_people' in listing and listing['extra_people'] is not None:
            listing['extra_people'] = float(
                listing['extra_people'].to_decimal())
        if 'bathrooms' in listing and listing['bathrooms'] is not None:
            listing['bathrooms'] = float(listing['bathrooms'].to_decimal())
        if 'security_deposit' in listing and listing['security_deposit'] is not None:
            listing['security_deposit'] = float(
                listing['security_deposit'].to_decimal())  # Convert security_deposit
        data.append(listing)
    return pd.DataFrame(data)


st.title("Visualizing Airbnb Listings Data")
data = get_data()

# Show data table
st.subheader("Data Preview")
st.write(data.head())

# Histogram for prices
if 'price' in data.columns:
    st.subheader("Price Distribution")
    st.bar_chart(data['price'])

# Histogram for number of reviews
if 'number_of_reviews' in data.columns:
    st.subheader("Number of Reviews Distribution")
    st.bar_chart(data['number_of_reviews'])

# Histogram for number of bedrooms
if 'bedrooms' in data.columns:
    st.subheader("Distribution of Number of Bedrooms")
    st.bar_chart(data['bedrooms'])

# Histogram for number of bathrooms
if 'bathrooms' in data.columns:
    st.subheader("Distribution of Number of Bathrooms")
    st.bar_chart(data['bathrooms'])

# Histogram for accommodates
if 'accommodates' in data.columns:
    st.subheader("Accommodates")
    st.bar_chart(data['accommodates'])

# Filter listings by selected amenities
if 'amenities' in data.columns:
    all_amenities = data['amenities'].explode().unique().tolist()
    selected_amenities = st.multiselect(
        'Select Amenities to Filter', all_amenities)

    if selected_amenities:
        filtered_data = data[data['amenities'].apply(
            lambda x: any(item in x for item in selected_amenities))]
        st.subheader("Filtered Data by Amenities")
        st.write(filtered_data)
    else:
        st.write("Please select amenities to filter the data.")

# Statistics Section
st.subheader("Statistics")

# Average Price
if 'price' in data.columns:
    average_price = data['price'].mean()
    st.metric("Average Price", f"${average_price:.2f}")

# Average Number of Reviews
if 'number_of_reviews' in data.columns:
    average_reviews = data['number_of_reviews'].mean()
    st.metric("Average Number of Reviews", f"{average_reviews:.2f}")


# import streamlit as st
# from pymongo import MongoClient
# import pandas as pd
#
#
# client = MongoClient('mongodb://localhost:27017/')
# db = client.db_listing
# listings_collection = db.listing_sql
#
# # Функция для получения данных из MongoDB и преобразования их в DataFrame
# def get_data():
#     listings = listings_collection.find()
#     data = []
#     for listing in listings:
#         listing['_id'] = str(listing['_id'])  # Конвертация ObjectId в строку
#         # Преобразование Decimal128 в float
#         if 'price' in listing and listing['price'] is not None:
#             listing['price'] = float(listing['price'].to_decimal())
#         if 'cleaning_fee' in listing and listing['cleaning_fee'] is not None:
#             listing['cleaning_fee'] = float(listing['cleaning_fee'].to_decimal())
#         if 'extra_people' in listing and listing['extra_people'] is not None:
#             listing['extra_people'] = float(listing['extra_people'].to_decimal())
#         if 'bathrooms' in listing and listing['bathrooms'] is not None:
#             listing['bathrooms'] = float(listing['bathrooms'].to_decimal())
#         data.append(listing)
#     return pd.DataFrame(data)
#
#
# st.title("Les visualisations des données de Airbnb Listings")
#
#
# data = get_data()
# st.subheader("DAta")
# st.write(data.head())
#
# if 'amenities' in data.columns:
#     amenities = data['amenities'].explode().unique().tolist()
#     selected_amenities = st.multiselect('Make a chose', amenities)
#
#     if selected_amenities:
#         filtered_data = data[data['amenities'].apply(lambda x: any(item in x for item in selected_amenities))]
#         st.subheader("Filtered data")
#         st.write(filtered_data)
#     else:
#         st.write("Please, chose amenities for filter data")
#
# # Визуализация данных
# st.subheader("Statistic")
#
# # Средняя цена
# if 'price' in data.columns:
#     average_price = data['price'].mean()
#     st.metric("Average price", f"${average_price:.2f}")
#
# # Среднее количество отзывов
# if 'number_of_reviews' in data.columns:
#     average_reviews = data['number_of_reviews'].mean()
#     st.metric("Average nb of reviews", f"{average_reviews:.2f}")

# # Гистограмма цен
# if 'price' in data.columns:
#     st.subheader("Répartition des prix")
#     st.bar_chart(data['price'])
#
# # Гистограмма количества отзывов
# if 'number_of_reviews' in data.columns:
#     st.subheader("Répartition of nb reviews")
#     st.bar_chart(data['number_of_reviews'])
#
# # Гистограмма количества спален
# if 'bedrooms' in data.columns:
#     st.subheader("Distribution of the number of bedrooms")
#     st.bar_chart(data['bedrooms'])
#
# # Гистограмма количества ванных комнат
# if 'bathrooms' in data.columns:
#     st.subheader("Distribution of the number of bathrooms")
#     st.bar_chart(data['bathrooms'])
#
# # Гистограмма вместимости
# if 'accommodates' in data.columns:
#     st.subheader("Accommodates")
#     st.bar_chart(data['accommodates'])
