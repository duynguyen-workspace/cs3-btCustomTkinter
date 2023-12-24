import customtkinter
import os
import json
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

# Product Frame class
class ProductFrame(customtkinter.CTkFrame):
    def __init__(self, master, product):
        super().__init__(master=master, fg_color="black", corner_radius=15)
        
        top_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        top_frame.pack(expand=True, fill="y", anchor="center")
        
        bottom_frame = customtkinter.CTkFrame(master=self, fg_color="black", corner_radius=15)
        bottom_frame.pack(expand=True, fill="y", anchor="center")
        
        # Setup image frame
        image_path = os.path.join("img","product1.png")
        image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(180, 180))
        img_frame = customtkinter.CTkLabel(master=top_frame, image=image, text="")
        img_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Setup information frame
        info_frame = customtkinter.CTkFrame(master=bottom_frame, fg_color="black")
        info_frame.pack(expand=True, fill="both", anchor="center", pady=(0, 20))
        
        product_name = customtkinter.CTkLabel(info_frame, text=product["name"])
        product_price = customtkinter.CTkLabel(info_frame, text="$ {}".format(product["price"]))
        button = customtkinter.CTkButton(info_frame, text="Buy Now", fg_color="blue", width=120)
        
        product_name.pack()
        product_price.pack()
        button.pack(pady=(10, 0))
        
        # Setup image
        rounded_image = add_border_radius(image_path, 10)
        image = customtkinter.CTkImage(light_image=rounded_image, dark_image=rounded_image, size=(20, 20))
        # label = customtkinter.CTkLabel(master=frame, image=image)
        # label.pack(expand=True, fill="both")


# Initialise Product List class
class ProductListScrollBar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, product_list):
        super().__init__(master=master, fg_color="white")
        
        # Iterate through product_list and create product frames according to data
        for i in range(len(product_list)):
            product_frame = ProductFrame(self, product=product_list[i])
            product_frame.grid(column=i % 4, row=i // 4, sticky="nesw", padx=5, pady=5)
                

# Initialise App class
class App(customtkinter.CTk):
    def __init__(self, product_list):
        super().__init__()
        
        # Configure title and window size
        self.title("Phone Shop")
        self.geometry("1024x700")
        
        # Configure grid columns and rows template
        self.columnconfigure((0), weight=1)
        self.rowconfigure((0), weight=1)
        
        # Configure window resizable status
        self.resizable(width=True, height=False)
        
        # Initialise scroll bar frame as the main frame 
        frameScrollBar = ProductListScrollBar(self, product_list=product_list)
        frameScrollBar.grid_columnconfigure((0, 1, 2, 3), weight=1)
        frameScrollBar.grid(column=0, row=0, sticky="nesw", columnspan=4)

# -----MAIN PROGRAM-----        

# Get product data
products = []
with open(os.path.join("data", "product_data.json"), "r", encoding="utf-8") as file:
    products = json.load(file)
    
    for product in products:
        print(product)

# Create app instance
app = App(product_list=products)
app.mainloop()