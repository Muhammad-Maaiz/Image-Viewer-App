# Image Viewer App  

# Import Necessray Libraries
from tkinter import *
from PIL import Image, ImageTk

# Function to navigate between images
def forward_and_back(image_number, direction):
    global my_label
    global forward_button
    global back_button

    # Hide the current image label
    my_label.grid_forget()

    # Update the image label based on the direction
    if direction == "forward":
        image_number += 1
    elif direction == "back":
        image_number -= 1

    # Create new image label with the updated image
    my_label = Label(center_frame, image=img_list[image_number - 1])

    # Update forward and backward buttons
    forward_button = Button(center_frame, text=">>", command=lambda: forward_and_back(image_number, "forward"), bg="#4CAF50", fg="black", width=5)
    back_button = Button(center_frame, text="<<", command=lambda: forward_and_back(image_number, "back"), bg="#4CAF50", fg="black", width=5)
    status_bar = Label(center_frame, text=f"Image {str(image_number)} of {str(len(img_list))}", bd=1, anchor="e", relief="sunken", bg="grey", width=8)

    # Disable forward button if reaching the last image
    if image_number == 5:
        forward_button = Button(center_frame, text=">>", state=DISABLED, bg="#aaa", width=5)

    # Disable back button if reaching the first image
    if image_number == 1:
        back_button = Button(center_frame, text="<<", state=DISABLED, bg="#aaa", width=5)

    # Display the updated image label and buttons
    my_label.grid(row=1, column=0, columnspan=3)
    back_button.grid(row=2, column=0, sticky="w", padx=5)
    forward_button.grid(row=2, column=2, sticky="e", padx=5)
    status_bar.grid(row=3,column=1,sticky="ew")

# Creating tkinter GUI
colour = "light green"
root = Tk()
root.title("Image Viewer App")
root.geometry("350x430")
root.resizable(width=False,height=False)
root.configure(bg=colour)

# Create a frame to hold label, buttons, images, and status bar
center_frame = Frame(root, bg=colour)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# Label for the title
books_label = Label(center_frame, text="𝓟𝔂𝓽𝓱𝓸𝓷 𝓑𝓸𝓸𝓴𝓼\n𝓘𝓶𝓪𝓰𝓮𝓼", bg=colour, font=("bold",20))
books_label.grid(row=0, column=0, columnspan=3)

# Load images
my_img_1 = ImageTk.PhotoImage(Image.open("Image-Viewer-App/Images/image1.jpeg"))
my_img_2 = ImageTk.PhotoImage(Image.open("Image-Viewer-App/Images/image2.jpeg"))
my_img_3 = ImageTk.PhotoImage(Image.open("Image-Viewer-App/Images/image3.jpeg"))
my_img_4 = ImageTk.PhotoImage(Image.open("Image-Viewer-App/Images/image4.jpeg"))
my_img_5 = ImageTk.PhotoImage(Image.open("Image-Viewer-App/Images/image5.jpeg"))

img_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

# Create a status bar
status_bar = Label(center_frame, text=f"Image 1 of {str(len(img_list))}", bd=1, anchor="e", relief="sunken", bg="grey", width=8)

# Set the initial image
my_label = Label(center_frame, image=my_img_1)
my_label.grid(row=1, column=0, columnspan=3)

# Create buttons for navigation and exit
back_button = Button(center_frame, text="<<", command=lambda: forward_and_back(1, "back"), bg="#4CAF50", fg="black", width=5, state=DISABLED)
exit_button = Button(center_frame, text="EXIT", command=root.quit, bg="#f44336", fg="black", width=5)
forward_button = Button(center_frame, text=">>", command=lambda: forward_and_back(2, "forward"), bg="#4CAF50", fg="black", width=5)

# Display buttons
back_button.grid(row=2, column=0, sticky="w", padx=5, pady=5)
exit_button.grid(row=2, column=1, padx=5, pady=5)
forward_button.grid(row=2, column=2, sticky="e", padx=5, pady=5)
status_bar.grid(row=3, column=1, sticky="ew")

# Run the GUI application
root.mainloop()
