# Patient Data Processing

This repository contains a Python script that reads patient data from an NDJSON file, flattens the JSON objects, and converts them into a Pandas DataFrame. The DataFrame is then saved as a CSV file with UTF-8 encoding.

## Dependencies

- pandas
- json

To install the dependencies, run:

```bash
pip install pandas
```

## Usage

1. Place your NDJSON file named `patient.ndjson` in the same directory as the script.
2. Run the script:

```bash
python flatten-ndjson.py
```

3. The output will be saved as `output.csv` in the same directory.

## Code Overview

The script performs the following steps:

1. Read the NDJSON file line by line:

```python
with open('patient.ndjson', 'r') as file:
    ndjson_data = [json.loads(line) for line in file]
```

2. Define the `flatten_json` function to flatten nested JSON objects:

```python
def flatten_json(y):
    # ...
```

3. Apply the `flatten_json` function to each JSON object in the list:

```python
flattened_data = [flatten_json(obj) for obj in ndjson_data]
```

4. Convert the flattened data to a Pandas DataFrame:

```python
df = pd.DataFrame(flattened_data)
```

5. Save the DataFrame to a CSV file with UTF-8 encoding:

```python
df.to_csv('output.csv', index=False, encoding='utf-8')
```

That's it! You now have a CSV file containing the flattened patient data.
