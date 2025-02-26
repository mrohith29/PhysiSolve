import json

# Open and load the JSON file
with open("dataset/high_school_physics.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Print the total number of records
print(len(data))

ans = 0
for record in data:
    ans += record["id"]

print(ans)