import tkinter as tk

# Premium calculation logic
# Replace this with your actual formula
def calculate_premium_logic(age, sum_assured):
    if age < 18:
        premium = sum_assured * 0.03
    elif age <= 50:
        premium = sum_assured * 0.05
    else:
        premium = sum_assured * 0.07
    return premium

# GUI Setup
root = tk.Tk()
root.title("Premium Calculator")
root.geometry("450x350")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Premium Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

# Age input
age_frame = tk.Frame(root, bg="#f0f0f0")
age_frame.pack(pady=5)
tk.Label(age_frame, text="Enter your age:", font=("Arial", 12), width=20, anchor="w", bg="#f0f0f0").pack(side="left")
age_entry = tk.Entry(age_frame, font=("Arial", 12))
age_entry.pack(side="left")

# Sum Assured input
sum_frame = tk.Frame(root, bg="#f0f0f0")
sum_frame.pack(pady=5)
tk.Label(sum_frame, text="Enter sum assured:", font=("Arial", 12), width=20, anchor="w", bg="#f0f0f0").pack(side="left")
sum_entry = tk.Entry(sum_frame, font=("Arial", 12))
sum_entry.pack(side="left")

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
result_label.pack(pady=20)

# Calculate button
def calculate_premium():
    age_text = age_entry.get()
    sum_text = sum_entry.get()
    
    # Input validation
    if not age_text.isdigit() or not sum_text.replace('.', '', 1).isdigit():
        result_label.config(text=" Please enter valid numbers")
        return

    age = int(age_text)
    sum_assured = float(sum_text)
    
    premium = calculate_premium_logic(age, sum_assured)
    result_label.config(text=f" Calculated Premium: ₹{premium:.2f}")

tk.Button(root, text="Calculate Premium", command=calculate_premium, font=("Arial", 12, "bold"),
          bg="#4CAF50", fg="white", width=20).pack(pady=10)

# Run GUI
root.mainloop()
