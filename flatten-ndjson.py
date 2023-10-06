import pandas as pd
import json

# Read the NDJSON file line by line
with open('patient.ndjson', 'r') as file:
    ndjson_data = [json.loads(line) for line in file]

# Define the flatten_json function as you did before
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Apply the flatten_json function to each JSON object in the list
flattened_data = [flatten_json(obj) for obj in ndjson_data]

# Convert the flattened data to a Pandas DataFrame
df = pd.DataFrame(flattened_data)

# Save the DataFrame to a CSV file with UTF-8 encoding
df.to_csv('output.csv', index=False, encoding='utf-8')