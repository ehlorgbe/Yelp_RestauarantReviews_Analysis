import pandas as pd
import numpy as np
import os 

# Load the data
# Define the path to the raw data
raw_data = "/Users/3lliot/Downloads/Yelp JSON/yelp_dataset/yelp_academic_dataset_review.json"

# Read the JSON file into a DataFrame
restaurant_data = []
dtypes = {
    'review_id': 'string',
    'user_id': 'string',
    'business_id': 'string',
    'stars': 'float32',
    'date': 'string',
    'text': 'string',
    'useful': 'int32',
    'funny': 'int32',
    'cool': 'int32'
}

with open(raw_data, 'r') as file:
    reader = pd.read_json(file, orient="records", lines=True, dtype=dtypes, chunksize=1000)
    for chunk in reader:
        col_dropped = chunk.drop(columns=['review_id', 'user_id'])\
            .query("`date` >= '2022-01-01'")
        restaurant_data.append(col_dropped)

# Concatenate all chunks into a single DataFrame
restaurant_data = pd.concat(restaurant_data, ignore_index=True)

# Save the DataFrame to a CSV file in /Users/3lliot/Documents/GitHub/Yelp_RestauarantReviews_Analysis/Datasets
restaurant_data.to_csv('/Users/3lliot/Documents/GitHub/Yelp_RestauarantReviews_Analysis/Datasets/restaurant_data.csv', index=False)
