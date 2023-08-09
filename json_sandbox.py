import json

file = open('default_json.txt', 'r')
file_contents = json.load(file)

file.close()

print(file_contents)