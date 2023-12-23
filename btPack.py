# BT2: Tạo giao diện với method pack

import customtkinter

root = customtkinter.CTk()

root.title("BT Custom Tkinter Pack")
root.geometry("400x400")

frameTop = customtkinter.CTkFrame(master=root)
frameTop.pack(expand=True, fill="both")

frameBottom = customtkinter.CTkFrame(master=root)
frameBottom.pack(expand=True, fill="both")

frameYellow = customtkinter.CTkFrame(master=frameTop, fg_color="yellow")
frameYellow.pack(side="left", expand=True, fill="both")

frameRed = customtkinter.CTkFrame(master=frameTop, fg_color="red")
frameRed.pack(side="left", expand=True, fill="both")

frameGrey = customtkinter.CTkFrame(master=frameBottom, fg_color="grey")
frameGrey.pack(side="left", expand=True, fill="both")

frameBlue = customtkinter.CTkFrame(master=frameBottom, fg_color="blue")
frameBlue.pack(side="left", expand=True, fill="both")

root.resizable(width=False, height=False)

root.mainloop()