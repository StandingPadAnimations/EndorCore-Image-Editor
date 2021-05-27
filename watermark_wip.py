import tkinter as tk
from tkinter import Button, StringVar, colorchooser, filedialog

from PIL import Image, ImageDraw, ImageFont, ImageTk

root = tk.Tk()
root.geometry('1000x500')
root.title("WaterMark Adder")

file = None 
save_file = None 

alpha = 0 
color = None 
hex_color = None 

custom_font = None 
font_size = None 
watermark_text = None 
font_file = None 

class Selection(tk.Frame):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        
        self.img_file_button = tk.Button(text="Choose File", command=self.img_browse_button)
        self.img_file_button.pack()
        
        self.watimg = tk.Entry(root, width=150)
        self.watimg.pack()
        
        self.watermark = tk.Entry(root, width=150)
        self.watermark.pack()
        self.watermark.insert(0, "Enter Watermark:")
        
        self.check_font = tk.StringVar()
        self.c_font = tk.Checkbutton(root, text= "Do you want a custom font?", variable=self.check_font, onvalue="yes", offvalue="no", command=self.activateCheckFont)
        self.c_font.deselect()
        self.c_font.pack()
        
        self.font_file_button = tk.Button(text="Choose Font File", command=self.font_browse_button)
        self.font_file_button.pack()
        self.font_file_button.config(state=tk.DISABLED)
        
        self.font_file = tk.Entry(root, width=150)
        self.font_file.pack()
        self.font_file.config(state=tk.DISABLED)
        
        self.font_size = tk.Entry(root, width=150)
        self.font_size.pack()
        self.font_size.insert(0, "Enter Font Size: ")
        
        self.choose_color = Button(root, text= "Choose Color", command=self.ask_color, padx=10, pady=10)
        self.choose_color.pack()
        
        self.no_alpha_var = tk.IntVar(value=0)
        self.no_alpha = tk.Checkbutton(root, text= "Not Transparent", variable=self.no_alpha_var, command=self.set_alpha)
        self.no_alpha.deselect()
        self.no_alpha.pack()
        
        self.half_alpha_var = tk.IntVar(value=0)
        self.half_alpha = tk.Checkbutton(root, text= "Half Transparent", variable=self.half_alpha_var, command=self.set_alpha)
        self.half_alpha.deselect()
        self.half_alpha.pack()
        
        self.custom_alpha_var = tk.StringVar()
        self.custom_alpha = tk.Checkbutton(root, text= "Custom", variable=self.custom_alpha_var, onvalue="yes", offvalue="no", command=self.set_alpha)
        self.custom_alpha.deselect()
        self.custom_alpha.pack()
        
        self.a = tk.Entry(root, width=150)
        self.a.pack()
        self.a.insert(0, "Enter alpha value for color(0-255):")
        self.a.config(state=tk.DISABLED)
        
        self.dont_overide_button = tk.Button(text="Save File", command=self.overide_browse_button)
        self.dont_overide_button.pack()
        
        self.save_filepath = StringVar()
        self.save_file = tk.Entry(root, width=150, textvariable=self.save_filepath)
        self.save_file.pack()
        self.save_file.config(state=tk.NORMAL)
        
        self.watimg_sub = tk.Button(text="Next Step", command=self.switch_window)
        self.watimg_sub.pack()
        
    def switch_window(self):
        global color 
        global custom_font
        global font_size
        global watermark_text
        global font_file
        global alpha
        global hex_color
        
        PictureWindow(root)
        custom_font = self.check_font.get()
        font_size = self.font_size.get()
        watermark_text = self.watermark.get()
        font_file = self.font_file.get()
        
        if color == None:
            color = 255, 355, 255
            
        if hex_color == None:
                hex_color = '#ffffff'
            
        if self.custom_alpha_var.get() == "yes":
            alpha = int(self.a.get())
            
        if self.half_alpha_var.get() == 0:
            alpha = 225
        
    def set_alpha(self):  
        global alpha 
        
        if self.half_alpha_var.get() == 0:
            alpha = 225
    
        elif self.half_alpha_var.get() == 1:
            alpha = 128
            
        if self.no_alpha_var.get() == 1:
            alpha = 225
            
        if self.custom_alpha_var.get() == "yes":
            self.a.config(state=tk.NORMAL)
            
        elif self.custom_alpha_var.get() == "no":
            self.a.config(state=tk.DISABLED)
            
    def ask_color(self):
        global color 
        global hex_color
        self.choose_color = colorchooser.askcolor()
        color = self.choose_color[0]
        hex_color = self.choose_color[1]
        
    def img_browse_button(self):
        global file 
        self.watimg_filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png*")])
        self.watimg.delete(0, tk.END)
        self.watimg.insert(0, self.watimg_filename)
        file = self.watimg.get()
        
    def font_browse_button(self):
        self.font_filename = filedialog.askopenfilename(filetypes=[("Font Files", "*.ttf*")])
        self.font_file.insert(0, self.font_filename)
        
    def overide_browse_button(self):
        global save_file
        self.save_filename = filedialog.asksaveasfilename(defaultextension='*.png*')
        self.save_file.delete(0, tk.END)
        self.save_file.insert(0, self.save_filename)
        save_file = self.save_file.get()
        
    def activateCheckFont(self):
        if self.check_font.get() == "yes":
            self.font_file.config(state=tk.NORMAL)
            self.font_file_button.config(state=tk.NORMAL)
            
        if self.check_font.get() == "no":
            self.font_file.config(state=tk.DISABLED)
            self.font_file_button.config(state=tk.DISABLED)
            
    def activateCheckPos(self):
        if self.check_pos.get() == "yes":
            self.x_pos.config(state=tk.NORMAL)
            self.y_pos.config(state=tk.NORMAL)
            self.margin.config(state=tk.DISABLED)
            
        if self.check_pos.get() == "no":
            self.x_pos.config(state=tk.DISABLED)
            self.y_pos.config(state=tk.DISABLED)
            self.margin.config(state=tk.NORMAL)
            
    def activateCheckColor(self):
        if self.check_color.get() == "yes":
            self.r.config(state=tk.NORMAL)
            self.g.config(state=tk.NORMAL)
            self.b.config(state=tk.NORMAL)
            
        if self.check_color.get() == "no":
            self.r.config(state=tk.DISABLED)
            self.g.config(state=tk.DISABLED)
            self.b.config(state=tk.DISABLED)
            
class PictureWindow(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.parent = parent
        self.x = self.y = 0
        self.rect = None
        self.tex = None
        self.start_x = None
        self.start_y = None
        
        image = Image.open(file)
        smaller_image = image.resize((round(image.size[0]/2), round(image.size[1]/2)))
        img = ImageTk.PhotoImage(smaller_image)
        
        self.canvas = tk.Canvas(self, width=img.width(), height=img.height())
        self.canvas.img = img 
        self.canvas.create_image(0, 0, image=img, anchor=tk.NW)
        self.canvas.pack(expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        self.finished = tk.Button(self, text="Add Watermark", command=self.Watermark)
        self.finished.pack()
        
        self.go_back = tk.Button(self, text="Go back to change settings", command=self.go_away)
        self.go_back.pack()
        
    def _from_rgb(self, rgb):
        r, g, b = rgb
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def go_away(self):
        self.withdraw()
        
    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        
        self.canvas.delete(self.tex)
        self.tex = None 
        
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, fill=self._from_rgb((249, 0, 0)), stipple='gray12')
            
    def on_move_press(self, event):
        self.curX = self.canvas.canvasx(event.x)
        self.curY = self.canvas.canvasy(event.y)
        self.text_x = ((self.start_x + self.curX) / 2)
        self.text_y = ((self.start_y + self.curY) / 2)
        
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)
        
    def on_button_release(self, event):
        font_preview_size = int(font_size)
        font_preview_almost = int(font_preview_size)
        font_preview = int(font_preview_almost)
        
        if not self.tex:
            self.tex = self.canvas.create_text((self.text_x, self.text_y), text=watermark_text, font=('Gotham Medium', font_preview), fill=hex_color)
            
    def Watermark(self): 
        self.font_size_var = font_size
        Font_Size = int(self.font_size_var)+4
        A = alpha 
        R = int(color[0])
        B = int(color[1])
        G = int(color[2])
        
        img = Image.open(file).convert("RGBA")
        img_down = img.resize((int(img.width/2), int(img.height/2)), resample=Image.NEAREST)
        img_down.x, img_down.y = img_down.size 
        
        txt = Image.new('RGBA', img_down.size, (225,225,225,0))
        
        if custom_font == "yes":
            font = ImageFont.truetype(font_file, Font_Size)
            draw = ImageDraw.Draw(txt)
            text = watermark_text
            
        if custom_font == "no": 
            font = ImageFont.truetype("arial.ttf", Font_Size)
            draw = ImageDraw.Draw(txt)
            text = watermark_text
            
        self.final_x = self.canvas.canvasx(self.text_x)
        self.final_y = self.canvas.canvasy(self.text_y)
        
        draw.text((self.final_x-15, self.final_y), text, font=font, fill=(R, G, B, A), anchor= "mm")
        
        comp = Image.alpha_composite(img_down, txt)
        img_up = comp.resize((int(comp.width*2), int(comp.height*2)), resample=Image.NEAREST)
        img_up.save(save_file)
        img_up.show()

if __name__ == "__main__":
    app = Selection(root)
    app.mainloop()