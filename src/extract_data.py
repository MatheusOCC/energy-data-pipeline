import requests
import pandas as pd
import os

# Resource id found at Dados Abertos URL
resource_id = '8c42c510-6549-4285-817c-58738914be19'

# Query data limitation
limit_data = 100
limit_text = f'&limit={limit_data}'

# API URL base
url = f'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search?resource_id={resource_id}{limit_text}'

# Requesting
response = requests.get(url)
data = response.json()

# Creating Pandas DataFrame
records = data['result']['records']
df = pd.DataFrame(records)

# Saving data on relative path
os.makedirs('../data/raw', exist_ok=True)
df.to_csv('../data/raw/complaints.csv', index=False)
print(f'Saved {len(df)} records.')