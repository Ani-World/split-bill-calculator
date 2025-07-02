from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("550x400")
window.title("Split Bills")

# Load background image
bg_image = Image.open("img.png")  # Replace with your actual image
bg_image = bg_image.resize((550, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create Canvas and set image
canvas = Canvas(window, width=550, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create overlay frame centered on canvas
overlay = Frame(canvas, bg="#ffffff", bd=0)
canvas.create_window(280, 200, window=overlay)  # 550/2, 400/2

# All widgets inside overlay
title = Label(overlay, text="Welcome to the tip calculator!", font=("Helvetica", 18, "bold"), bg="#ffffff")
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

bill = Label(overlay, text="What was the total bill? $", font=("Helvetica", 10), bg="#ffffff")
bill.grid(row=1, column=0, pady=(0, 10), sticky="w")
bill_inp = Entry(overlay, width=10)
bill_inp.grid(row=1, column=1, pady=(0, 10))

tip = Label(overlay, text="What percentage tip would you like to give? 10 12 15", font=("Helvetica", 10), bg="#ffffff")
tip.grid(row=2, column=0, pady=(0, 10), sticky="w")
tip_inp = Entry(overlay, width=10)
tip_inp.grid(row=2, column=1, pady=(0, 10))

people = Label(overlay, text="How many people to split the bill? ", font=("Helvetica", 10), bg="#ffffff")
people.grid(row=3, column=0, pady=(0, 10), sticky="w")
people_inp = Entry(overlay, width=10)
people_inp.grid(row=3, column=1, pady=(0, 10))

calculate_button = Button(overlay, text="Calculate", command=lambda: calculate(), font=("Helvetica", 10, "bold"))
calculate_button.grid(row=4, column=0, columnspan=2, pady=(10, 10))

result_label = Label(overlay, text="", font=("Helvetica", 12, "bold"), bg="#ffffff", fg="green")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Logic
def calculate():
    try:
        bill_amt = float(bill_inp.get())
        tip_percent = int(tip_inp.get())
        num_people = int(people_inp.get())
        total_tip = bill_amt * (tip_percent / 100)
        total_bill = bill_amt + total_tip
        per_person = round(total_bill / num_people, 2)
        result_label.config(text=f"Each person should pay: ${per_person}", fg="green")
    except:
        result_label.config(text="Please enter valid inputs", fg="red")

window.mainloop()
