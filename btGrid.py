# BT3: Tạo giao diện với method grid

import customtkinter

# Initialise Tkinter
root = customtkinter.CTk()

# Application Title
root.title("BT Custom Tkinter Grid")

# Setup width and height for application
root.geometry("600x400")

# Setup parent grid column and row templates
root.columnconfigure((0, 1), weight=1)
root.rowconfigure((0, 1), weight=1)

# Setup theme and default color
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

frameYellow = customtkinter.CTkFrame(root, fg_color="yellow")
frameYellow.grid(column="0", row="0", sticky="nswe")

frameRed = customtkinter.CTkFrame(root, fg_color="red")
frameRed.grid(column="1", row="0", sticky="nswe")

frameGrey = customtkinter.CTkFrame(root, fg_color="grey")
frameGrey.grid(column="0", row="1", sticky="nswe")

frameBlue = customtkinter.CTkFrame(root, fg_color="blue")
frameBlue.grid(column="1", row="1", sticky="nswe")

root.resizable(width=False, height=False)
root.mainloop()