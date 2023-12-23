import customtkinter
import os
from PIL import Image, ImageOps, ImageDraw

# Add border radius image function
def add_border_radius(image_path, radius):
    image = Image.open(image_path)
    mask = Image.new('L', image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)
    result = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result

class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="black", corner_radius=15)
        
        top_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        top_frame.pack(expand=True, fill="y", padx=20, anchor="center")
        
        bottom_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        bottom_frame.pack(expand=True, fill="y", padx=20, anchor="center")
        
        # Setup image path
        image_path = os.path.join("img","product1.png")
        image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
        
        img_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
        img_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
        info_frame.pack(expand=True, fill="both", anchor="center", pady=(0, 20))
        
        product_name = customtkinter.CTkLabel(info_frame, text="Iphone 14 Pro Max")
        product_price = customtkinter.CTkLabel(info_frame, text="$145")
        button = customtkinter.CTkButton(info_frame, text="Buy Now", fg_color="blue", width=120)
        
        product_name.pack()
        product_price.pack()
        button.pack(pady=(10, 0))
        
        # Setup image
        rounded_image = add_border_radius(image_path, 10)
        image = customtkinter.CTkImage(light_image=rounded_image, dark_image=rounded_image, size=(20, 20))
        # label = customtkinter.CTkLabel(master=frame, image=image)
        # label.pack(expand=True, fill="both")
        

# Initialise ScrollBar class
class FrameScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color="white")
        
        # main_frame = customtkinter.CTkFrame(master=self, fg_color="white")
        # main_frame.grid(column=0, row=0, sticky="nesw")
        # main_frame.grid_columnconfigure(0, weight=1)
        # main_frame.grid_rowconfigure(0, weight=1)
        
        
        for i in range(0, 30, 4):
            for j in range(0, 4):
                product = ProductFrame(self)
                product.grid(column=int(j % 4), row=int(i / 4), sticky="nesw", padx=5, pady=5)
                
                # frame = customtkinter.CTkFrame(master=self, fg_color="red", corner_radius=20)
                # frame.grid(column=int(i / 3), row=int(j % 3), sticky="nesw", padx=10, pady=10)

                

# Initialise App class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Phone Shop")
        self.geometry("1024x700")
        
        # Configure grid columns and rows template
        self.columnconfigure((0, 1, 2, 3), weight=1)
        
        self.resizable(width=True, height=False)
        
        frameScrollBar = FrameScrollBar(self)
        frameScrollBar.pack(expand=True, fill="both", anchor="center")

# -----MAIN PROGRAM-----        
app = App()
app.mainloop()