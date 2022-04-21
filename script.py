
import json

with open("mobility_exercises.json") as mobility_json:
  mobility_exercises = json.load(mobility_json)
  
print(mobility_exercises["Name"])
