import json

def parse_and_check(json_str):
    data = json.loads(json_str)
    
    if 'name' in data and 'age' in data:
        print("Keys 'name' and 'age' are present.")
    else:
        print("One or both of the keys 'name' and 'age' are missing.")
    
    new_json_str = json.dumps(data)
    
    return data, new_json_str

json_str = '{"name": "Alice", "age": 25}'

parsed_dict, new_json_str = parse_and_check(json_str)

print("Parsed Dictionary:", parsed_dict)
print("New JSON String:", new_json_str)
