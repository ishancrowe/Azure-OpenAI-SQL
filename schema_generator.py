import json

def json_to_schema_dict(json_data):
  """
  Converts the given JSON data into a dictionary where 
  keys are table names and values are dictionaries 
  containing column details.

  Args:
    json_data: The JSON data representing the table schema.

  Returns:
    dict: A dictionary where keys are table names 
          and values are dictionaries of column details.
  """
  schema_dict = {}
  for table_data in json_data:
    table_name = f"{table_data.get('Schema', '')}.{table_data.get('Entity', '')}"
    schema_dict[table_name] = {
        "Definition": table_data.get("Definition", ""),  # Add schema definition
        "Columns": {} 
    }
    for column in table_data.get('Columns', []):
      schema_dict[table_name]["Columns"][column['Name']] = {
          'DataType': column['DataType'],
          'Definition': column['Definition'],
          'SampleValues': column['SampleValues']
      }
  return schema_dict
    # schema_dict[table_name] = {}
    # for column in table_data.get('Columns', []):
    #   schema_dict[table_name][column['Name']] = {
    #       'DataType': column['DataType'],
    #       'Definition': column['Definition'],
    #       'SampleValues': column['SampleValues']
    #   }
  return schema_dict

# Load the JSON data (replace with your actual loading method)
with open('test_data_dict.json', 'r') as f:
  json_data = json.load(f)

# Convert the JSON data to the desired dictionary format
schema_dict = json_to_schema_dict(json_data)
print(schema_dict)

# Print the schema for the first table (example)
