import requests
import pandas as pd

# Resource id found at Dados Abertos URL
resource_id = '8c42c510-6549-4285-817c-58738914be19'

# API URL base
url = f'https://dadosabertos.aneel.gov.br/api/3/action/datastore_search?resource_id={resource_id}&limit=5'

# Requesting
response = requests.get(url)
data = response.json()

# Creating Pandas DataFrame
records = data['result']['records']
df = pd.DataFrame(records)

print(df.head())