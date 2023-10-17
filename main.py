import tkinter as tk
# Create object  
root = tk.Tk()

# Adjust size  
root.geometry("800x706") #image size
root.resizable(0, 0)  #Don't allow resizing in the x or y direction

# Add image file 
bg = tk.PhotoImage(file="images/main_background.png")

back_ground = tk.Label(root, image=bg)
back_ground.place(x=0, y=0)

R1 = tk.Radiobutton(root, text="singapore", value=1)
R1.place(x=480, y=610)

# Add buttons
R2 = tk.Radiobutton(root, text="China", value=2)
R2.place(x = 450, y = 320)

button3 = tk.Button(root, text="Korea")
button3.place(x = 590, y = 270)

button4 = tk.Button(root, text="Thailand")
button4.place(x = 460, y = 500)

button5 = tk.Button(root, text="Japan")
button5.place(x = 650, y = 300)

# Execute tkinter 
root.mainloop()