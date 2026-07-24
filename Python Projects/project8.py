from tkinter import Label, Tk
import time

# Create main window
app = Tk()
app.title("Digital Clock")
app.geometry("350x150")
app.configure(bg="black")

# Styling the clock label
clock_label = Label(app, font=('Arial', 50, 'bold'), background='black', foreground='cyan')
clock_label.pack(pady=30)

# Function to update time
def update_time():
    current_time = time.strftime('%H:%M:%S')  # Format: Hour:Minute:Second
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every 1000ms (1 second)

update_time()  # Call once to start
app.mainloop()