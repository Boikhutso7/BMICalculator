import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert cm to meters
        
        # Input validation
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid input", "Weight and height must be positive numbers.")
            return
        
        if weight > 1000 or height > 3:  # Reasonable upper limits
            messagebox.showerror("Invalid input", "Please enter realistic values for weight and height.")
            return
        
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
            color = "#3498db"  # Blue
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "#2ecc71"  # Green
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "#f39c12"  # Orange
        else:
            category = "Obese"
            color = "#e74c3c"  # Red
        
        result_label.config(text=f"BMI: {bmi}\nCategory: {category}", fg=color)
        
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")
    except ZeroDivisionError:
        messagebox.showerror("Invalid input", "Height cannot be zero.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def clear_fields():
    """Clear all input fields and result"""
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="", fg="black")

def on_enter_key(event):
    """Allow Enter key to calculate BMI"""
    calculate_bmi()

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.config(bg="#f0f0f0")
root.resizable(False, False)

# Title
label_title = tk.Label(root, text="BMI Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="#2c3e50")
label_title.pack(pady=15)

# Weight input
label_weight = tk.Label(root, text="Enter weight (kg):", font=("Arial", 11), bg="#f0f0f0", fg="#34495e")
label_weight.pack()
entry_weight = tk.Entry(root, font=("Arial", 11), width=20, justify='center')
entry_weight.pack(pady=5)
entry_weight.bind('<Return>', on_enter_key)  # Bind Enter key

# Height input
label_height = tk.Label(root, text="Enter height (cm):", font=("Arial", 11), bg="#f0f0f0", fg="#34495e")
label_height.pack(pady=(10, 0))
entry_height = tk.Entry(root, font=("Arial", 11), width=20, justify='center')
entry_height.pack(pady=5)
entry_height.bind('<Return>', on_enter_key)  # Bind Enter key

# Buttons frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

# Calculate button
btn_calculate = tk.Button(button_frame, text="Calculate BMI", command=calculate_bmi, 
                         bg="#4CAF50", fg="white", font=("Arial", 11, "bold"),
                         width=12, height=1, cursor="hand2")
btn_calculate.pack(side=tk.LEFT, padx=5)

# Clear button
btn_clear = tk.Button(button_frame, text="Clear", command=clear_fields,
                     bg="#95a5a6", fg="white", font=("Arial", 11, "bold"),
                     width=8, height=1, cursor="hand2")
btn_clear.pack(side=tk.LEFT, padx=5)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"), bg="#f0f0f0", 
                        wraplength=300, justify="center",
                       width=35, height=22, relief="solid", borderwidth=1)
result_label.pack(pady=15, padx=10, fill= "x")

# BMI Categories reference
info_text = ("BMI Categories:\n"
             "Underweight: < 18.5  |  Normal: 18.5-24.9\n"
             "Overweight: 25-29.9  |  Obese: ≥ 30")
info_label = tk.Label(root, text=info_text, font=("Arial", 8), bg="#f0f0f0", fg="#7f8c8d")
info_label.pack(pady=(0, 10))

# Focus on weight entry when program starts
entry_weight.focus()

# Start the GUI
root.mainloop()