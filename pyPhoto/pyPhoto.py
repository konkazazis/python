import customtkinter as ctk
from pyPhoto.image_widgets import *
from PIL import Image, ImageTk

class App(ctk.CTk):
    def __init__(self):

        super().__init__()
        ctk.set_appearance_mode('dark')
        self.title('pyPhoto')
        self.geometry("1000x600")
        self.minsize(800,500)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=6)

        self.image_import = ImageImport(self, self.import_image)

        self.mainloop()

    def import_image(self,path):
        self.image = Image.open(path)
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import .grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, close_func=self.close_edit)

    def close_edit(self):
        self.image_output.grid_forget()
        self.image_output.place_forget()
        self.image_import = ImageImport(self, self.import_image)
        
    def resize_image(self, event):

        canvas_ratio = event.width / event.height

        if canvas_ratio > self.image_ratio:
            image_height = int(event.height)
            image_width = int(image_height * self.image_ratio)
        else:
            image_width = int(event.width)
            image_height = int(image_width / self.image_ratio)


        self.image_output.delete("all")
        resized_image = self.image.resize((image_width,image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(event.width/2,event.height/2, image = self.image_tk)


App()