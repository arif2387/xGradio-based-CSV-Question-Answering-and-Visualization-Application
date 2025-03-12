import pandas as pd
import random

# Number of rows to generate
n_rows = 1000

# Define sample values for string-based columns
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
          'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
house_types = ['Detached', 'Semi-detached', 'Townhouse', 'Condo']

# Generate synthetic data
data = {
    "ID": range(1, n_rows + 1),
    "City": [random.choice(cities) for _ in range(n_rows)],
    "HouseType": [random.choice(house_types) for _ in range(n_rows)],
    "Price": [random.randint(100000, 1000000) for _ in range(n_rows)],    # Price in dollars
    "Area": [random.randint(500, 4000) for _ in range(n_rows)],             # Area in square feet
    "Bedrooms": [random.randint(1, 5) for _ in range(n_rows)],
    "Bathrooms": [round(random.uniform(1, 4), 1) for _ in range(n_rows)],    # Rounded to 1 decimal
    "YearBuilt": [random.randint(1900, 2022) for _ in range(n_rows)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("housing_data.csv", index=False)

print("CSV file 'housing_data.csv' with 1000 rows generated successfully!")
