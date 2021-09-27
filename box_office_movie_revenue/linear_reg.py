"""

"""
# Importing Libraries
import pandas as pd
import warnings

warnings.simplefilter('ignore')

# Importing the dataset from file
path = './data/cost_revenue_dirty.csv'
dataset = pd.read_csv(filepath_or_buffer=path, index_col='Rank')
movie_dataset = dataset.copy()

####### Preprocessing Data

# Printing a sample of the data
print(movie_dataset.sample(10))

# Displaying Column in the dataset
print(movie_dataset.columns)

"""
# Dropping Columns

the following columns will be dropped from the dataset because they are not needed in thw implementation of the model
1. Rank - The movie ranking 
2. Release Date - When the movie was or will be released
3. Movie Title -  The movie title
4. Domestic Gross -  The Income generated by the movie after release data.
"""
movie_dataset.drop(labels=['Release Date', 'Movie Title', 'Domestic Gross ($)'], axis=1, inplace=True)
print('Columns left after removing unwanted columns: ', movie_dataset.columns[0], 'and', movie_dataset.columns[1])

"""
# Renaming Columns and removing special

Renaming the colunm names from what is provided in the dataset to easy to understand names:
1. Production Budget ($) ----> production_budget_usd
2. Worldwide Gross ($) ----> worldwide_gross_usd

Removing Special Characters from values provided for specific all rows
eg:
$11,000,000 ---.  11000000

"""
movie_dataset['production_budget_usd'] = movie_dataset['Production Budget ($)'].str.replace('\W', '')  # Important Concept
movie_dataset['worldwide_gross_usd'] = movie_dataset['Worldwide Gross ($)'].str.replace('\W', '')  # Important Concept
print(movie_dataset.sample(1))
# Dropping old columns names
movie_dataset.drop(labels=['Worldwide Gross ($)', 'Production Budget ($)'], axis=1, inplace=True)

"""
# Removing Zeros

Removing all the rows with zero in worldwide_gross_usd:
a zero in this column may indicate:
1. The movie was never produced
2. The movie has not been released
3. This information in not available in the public domain
"""
print('Rows before dropping zero: ', movie_dataset.shape[0])
movie_dataset.drop(movie_dataset[movie_dataset['worldwide_gross_usd'] == '0'].index, inplace=True)  # Important Concept
print('Rows after dropping zero: ', movie_dataset.shape[0])

"""The dataset after preprocessing will look like: """
print(movie_dataset.sample(4))


