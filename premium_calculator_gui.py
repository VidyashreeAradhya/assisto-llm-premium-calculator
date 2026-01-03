import tkinter as tk
from premium_calculator import premiumCalculator

# ------------------ TABLES USED BY LOGIC ------------------

ratesTable = {
    "Bangalore": {"baseRate": 3.5},
    "Mumbai": {"baseRate": 4.0}
}

riskTable = {
    30: {"riskMultiplier": 1.2},
    40: {"riskMultiplier": 1.3},
    45: {"riskMultiplier": 1.5}
}

# ------------------ GUI SETUP ------------------

root = tk.Tk()
root.title("Premium Calculator")
root.geometry("450x300")
root.resizable(False, False)

tk.Label(
    root,
    text="Premium Calculator",
    font=("Arial", 18, "bold")
).pack(pady=15)

# Age input
age_frame = tk.Frame(root)
age_frame.pack(pady=5)

tk.Label(age_frame, text="Enter your age:", width=20, anchor="w").pack(side="left")
age_entry = tk.Entry(age_frame)
age_entry.pack(side="left")

# Coverage input
cov_frame = tk.Frame(root)
cov_frame.pack(pady=5)

tk.Label(cov_frame, text="Enter coverage amount:", width=20, anchor="w").pack(side="left")
coverage_entry = tk.Entry(cov_frame)
coverage_entry.pack(side="left")

# Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.pack(pady=20)

# ------------------ BUTTON ACTION ------------------

def calculate_premium_gui():
    age_text = age_entry.get()
    coverage_text = coverage_entry.get()

    if not age_text.isdigit() or not coverage_text.isdigit():
        result_label.config(text="Please enter valid numbers")
        return

    age = int(age_text)

    # Pick nearest risk age if exact age not present
    closest_age = min(riskTable.keys(), key=lambda x: abs(x - age))

    user_profile = {
        "age": closest_age,
        "location": "Bangalore",
        "coverage": int(coverage_text)
    }

    premium = premiumCalculator(user_profile, ratesTable, riskTable)
    result_label.config(text=f"Calculated Premium: ₹{premium:.2f}")

# Button
tk.Button(
    root,
    text="Calculate Premium",
    command=calculate_premium_gui,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
).pack(pady=10)

root.mainloop()
