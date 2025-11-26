import json

# Correct path to the JSON file
with open("JSON/library.json", "r") as file:
    data = json.load(file)

# Print books list
print(data["books"])
print(json.dumps(data, indent=4))

