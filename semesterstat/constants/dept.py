import json

dept_dict = {}

with open("Departments.json") as file:
    dept_dict = json.load(file)
