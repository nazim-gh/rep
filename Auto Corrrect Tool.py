import customtkinter
from PIL import Image
import os
from textblob import TextBlob
from autocorrect import Speller

current_path = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Auto-Correct")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure((0,1,2,3), weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_frame.grid_rowconfigure(0, weight=2)
        self.sidebar_frame.grid_rowconfigure(1, weight=1)
        self.sidebar_frame.grid_rowconfigure(2, weight=1)
        self.sidebar_frame.grid_rowconfigure(3, weight=1)
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # self.sidebar_frame.grid_rowconfigure(5, weight=1)

        #HOUSE IMAGE
        img = customtkinter.CTkImage(Image.open(current_path + "/cutee.jpg"),size=(150,150))

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,image=img, text="")
        self.logo_label.grid(row=0, column=0, padx=5, pady=(20, 20), sticky='n')

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Clear",command=self.clearr)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=0, sticky='n')

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Made By-",font=customtkinter.CTkFont(weight="bold"),corner_radius=20, hover_color="#54b038", command= self.made_by)
        self.sidebar_button_3.grid(row=2, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=3, column=0, padx=20)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=3, column=0, padx=20, pady=(30, 30),sticky='s')
        self.appearance_mode_optionemenu.set("Dark")
        

        #HEAD
        #self.head = customtkinter.CTkFrame(self)  
        self.heading = customtkinter.CTkLabel(self, text="Auto Correction Tool",font=customtkinter.CTkFont(family = "Agency FB",size=40, weight="bold"), width=712)
        self.heading.grid(row=0, column=1, columnspan=2,pady= (20,10), sticky="n") 

        self.heading2 = customtkinter.CTkLabel(self, text="Get started by Entering Text Below!",font=customtkinter.CTkFont(family = "Century Gothic",size=20))
        self.heading2.grid(row=0, column=1, columnspan=2,padx=180,pady= (80,10), sticky="nw")     
        self.heading.grid_columnconfigure(0, weight=2)
           

        self.frame = customtkinter.CTkFrame(self, width = 640, height=350,corner_radius=30, border_width=1, border_color="#38393b", fg_color="transparent")
        self.frame.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

    

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Text", width=500, height=80)
        self.entry.place(x = 250, y = 200)

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent",command=self.Correct, border_width=2, text_color=("gray10", "#DCE4EE"), text="Correct!!")
        self.main_button_1.place(x = 250, y = 300)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=500, height=150)
        self.textbox.place(x = 250, y = 350)
   

    #Dark Theme Switch
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode) 

    def made_by(self):
        dialog = customtkinter.CTkInputDialog(text="Made By:  Nazim\nnazimkhan9182@gmail.com", title="NAZIM")

    def clearr(self):
        self.textbox.delete("0.0", "end")
        self.entry.delete(0, "end")

    def Correct(self):
        spell=Speller()
        a = self.entry.get()
        c = spell(a)
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", c)
if __name__ == "__main__":
    app = App()
    app.mainloop()