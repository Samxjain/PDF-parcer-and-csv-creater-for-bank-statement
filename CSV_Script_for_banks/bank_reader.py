import pandas as pd
import os
from categories import categorize

# ===== CONFIG =====
base_path = "/Users/sameerjain/Desktop/python_projects/CSV_Script_for_banks"
folder_path = os.path.join(base_path, "Script_Input")   # Input folder with bank CSVs
output_file = os.path.join(base_path, "Script_Output", "categorized_bank.csv")
uncategorized_file = os.path.join(base_path, "Script_Output", "uncategorized.csv")

csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
all_data = []

for csv_file in csv_files:
    path = os.path.join(folder_path, csv_file)
    try:
        # Find header row
        with open(path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if 'Transaction Remarks' in line:
                    header_row = i
                    break
            else:
                print(f"No valid header in {csv_file}, skipping.")
                continue

        df = pd.read_csv(path, header=header_row)
        df.columns = df.columns.str.strip()

        # Rename columns
        df.rename(columns={
            'Transaction Date': 'Date',
            'Transaction Remarks': 'Description',
            'Withdrawal Amount (INR )': 'Withdrawal',
            'Deposit Amount (INR )': 'Deposit'
        }, inplace=True)

        df['Withdrawal'] = pd.to_numeric(df['Withdrawal'], errors='coerce').fillna(0)
        df['Deposit'] = pd.to_numeric(df['Deposit'], errors='coerce').fillna(0)
        df['Amount'] = df['Deposit'] - df['Withdrawal']

        df['Category'] = df['Description'].apply(categorize)
        df = df[['Date', 'Description', 'Amount', 'Category']]

        all_data.append(df)
        print(f"Processed: {csv_file}")

    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# ===== COMBINE AND SAVE =====
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv(output_file, index=False)

    print(f"\nAll bank CSVs combined and saved to {output_file}")

    # Save uncategorized
    others_df = combined_df[combined_df["Category"] == "Other"]
    if not others_df.empty:
        others_df.to_csv(uncategorized_file, index=False)
        print(f"\nUncategorized transactions saved to {uncategorized_file}")

    # Show totals
    print("\nCategory totals:")
    print(combined_df.groupby("Category")["Amount"].sum())
else:
    print("No CSV files processed.")
