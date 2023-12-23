import customtkinter

# Scrollbar class
class FrameScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="black")
        
        for i in range(0, 1000):
            button = customtkinter.CTkButton(master=self, fg_color="green", width=300, height=40, text="Button {}".format(str(i + 1)), command=lambda index = i: self.getNumber(index + 1))
            button.pack(pady=5)
    
    def getNumber(self, id):
        print(id)

# Initialise App class to configure customtkinter
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("App")
        self.geometry("600x400")
        
        frameScrollBar = FrameScrollBar(self)
        frameScrollBar.pack(expand=True, fill="both")
        
app = App()
app.mainloop()