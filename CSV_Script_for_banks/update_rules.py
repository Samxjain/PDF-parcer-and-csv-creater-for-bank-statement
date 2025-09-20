import json
import pandas as pd

rules_file = "rules.json"
uncategorized_file = "Script_Output/uncategorized.csv"

# Load current rules
with open(rules_file, "r") as f:
    rules = json.load(f)

# Load manually labeled data
df = pd.read_csv(uncategorized_file)

if "New_Category" not in df.columns:
    print("❌ Please add a column 'New_Category' to uncategorized.csv before running this.")
    exit()

for _, row in df.iterrows():
    desc = str(row["Description"]).lower()
    new_cat = row.get("New_Category")

    if pd.notna(new_cat):
        # For simplicity, just add whole description as a keyword
        rules.setdefault(new_cat, []).append(desc)
        print(f"Added '{desc}' -> {new_cat}")

# Save updated rules
with open(rules_file, "w") as f:
    json.dump(rules, f, indent=2)

print("\n✅ Rules updated successfully!")