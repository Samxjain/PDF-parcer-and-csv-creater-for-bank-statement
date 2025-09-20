# categories.py
from collections import defaultdict

# Track match counts (for analysis later)
category_counts = defaultdict(int)

def categorize(desc: str) -> str:
    desc = str(desc).lower()

    rules = {
        "Shopping": ["amazon", "flipkart", "dmart", "market99"],
        "Food & Groceries": ["zomato", "swiggy", "zepto", "blinkit", "grocer", "sabzi", "milk", "pizza", "cake", "food", "momo", "ghee", "paneer", "tamatar"],
        "Transport": ["uber", "ola", "rapido", "metro", "fuel", "petrol", "diesel", "bike", "car", "taxi"],
        "Entertainment": ["netflix", "spotify", "prime", "hotstar", "zee5", "sony", "disney"],
        "Income": ["salary", "payroll", "credit salary", "tata cons", "larsen and toubro", "cms/ salary"],
        "Rent/Loan": ["loan", "emi", "house rent", "rentomojo"],
        "Bills & Utilities": ["airtel", "jio", "vodafone", "vi ", "electric", "bijli", "gas", "water", "dth", "broadband"],
        "Healthcare": ["doctor", "hospital", "pharmacy", "lab", "medicine", "apollo", "practo"],
        "Investment/Savings": ["mutual fund", "nifty", "hdfc bank ltd", "wipro", "coal india", "dividend", "reliance industries", "embassy reit", "bharti airtel ltd", "investment", "savings"],
        "Refund/Cashback": ["refund", "cashfree", "cashback"]
    }

    for category, keywords in rules.items():
        if any(k in desc for k in keywords):
            category_counts[category] += 1
            return category

    category_counts["Other"] += 1
    return "Other"


def show_category_stats():
    """Print a summary of how many transactions matched each category."""
    print("\nCategory usage so far:")
    for cat, count in category_counts.items():
        print(f"{cat}: {count}")
