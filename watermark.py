############################################################################################
# All code here is free to play with and modify.
# My personal reccoemndation is to use either the IDLE IDE that comes with Python when you 
# install it, or Visual Studio Code. There are also other IDEs avalible like Atom or Pycharm  
# This was written by StandingPad Animations
############################################################################################
############################################################################################
# Explination of some of the Python code:
# input("question asked"): Asks for a string input
# int("varible of a sting"): Converts a string(anything with "" around it) to a 
# integer(number without the "") so it can be used by the code
# varible = input("question asked"): Example of a variable. Makes it easier to code some aspects 
############################################################################################
############################################################################################
# Cool things to try:
# Making it loop
# Allowing the user to choose the position 
# Making a thing where the user can say a color(ex. blue) and it sets the RGBA values to it 
############################################################################################

# Imports from the Pillow Python Library 
from PIL import Image, ImageDraw, ImageFont

# All prompts asked for watermark creation 
watimg = input("Enter PNG Image File Path(can be a relative file path(ex. Watermark Adder/image.png)): ")
watermark = input("Enter Watermark: ")
font_file = input("Enter Font File Path(can be a relative file path(ex. Watermark Adder/BOLD.ttf)): ")
font_size = input("Enter Font Size: ")
r = input("Enter R(red) value for color: ")
g = input("Enter G(green) value for color: ")
b = input("Enter B(blue) value for color: ")
a = input("Enter A(alpha which is transparancy) value for color: ")
margin = input("Enter a margin value(when in doubt, use 5): ")
output_img = input("Enter the File Path for the Outputed PNG Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

# Converts numbers from a string to a integer(number) the program can use without having a error 
Font_Size = int(font_size)
R = int(r)
B = int(b)
G = int(g)
A = int(a)
Margin = int(margin)


# Converts image to rgba 
img = Image.open(watimg).convert("RGBA")
width, height = img.size

# Creates a new image for text 
txt = Image.new("RGBA", img.size, (225,225,225,0))

# Font and text settings 
font = ImageFont.truetype(font_file, Font_Size)
draw = ImageDraw.Draw(txt)
text = watermark
textwidth, textheight = draw.textsize(text, font)

# Calculates the position for the watermark(bottom right hand corner) 
margin = Margin 
x = width - textwidth - margin
y = height - textheight - margin

# Fill(r, g, b, a)                 V Grabs vaules from the RGBA questions 
draw.text((x, y), text, font=font, fill=(R, G, B, A))

# Combines the 2 images 
comp = Image.alpha_composite(img, txt)

# Shows the image 
comp.show()

# Image saved as what was the specified file name in the file path specified 
comp.save(output_img)
