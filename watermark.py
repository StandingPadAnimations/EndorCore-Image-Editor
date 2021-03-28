# Imports from the Pillow Python Library 
from PIL import Image, ImageDraw, ImageFont

class Watermark(): 
    # Image, text, and font Questions  
    watimg = input("Enter PNG Image File Path(can be a relative file path(ex. Watermark Adder/image.png)): ")
    watermark = input("Enter Watermark: ")

    # Font Question 
    c_font = input("Do you want a custom font(yes/no)?: ")
    if c_font == "yes":
        font_file = input("Enter Font File Path(can be a relative file path(ex. Watermark Adder/BOLD.ttf)): ")
        font_size = input("Enter Font Size: ")
        
    if c_font == "no":
        font_size = input("Enter Font Size: ")
        
    # Color Question 
    color = input("Do you want a custom color(yes or no)?: ")

    # If someone said yes to the Color Question 
    if color == "yes":
        
        hex_code = input("Do you have a hex code(yes/no)?: ")
        if hex_code == "yes":
            Hex_Code = input("Hex Code: ")
            
            def hex_to_rgb(value):
                value = value.lstrip('#')
                return list(int(value[i:i+2], 16) for i in (0, 2, 4))
            
            print(f"RGB Value: {hex_to_rgb(Hex_Code)}")
            pass 
        # RGBA Questions 
        r = input("Enter R(red) value for color: ")
        g = input("Enter G(green) value for color: ")
        b = input("Enter B(blue) value for color: ")
        a = input("Enter A(alpha which is transparancy) value for color: ")

        # Position Question 
        pos = input("Do you want to choose your watermark position(yes or no)?: ") 

        # If someone said yes to the Position Question 
        if pos == "yes": 
            x_pos = input("Enter X Position: ")
            y_pos = input("Enter Y Position: ")
            dont_overide = input("Do you want to make the image a seperate file(yes/no)?: ")
            if dont_overide == "yes":
                output_img = input("Enter the File Path for the Outputed PNG Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

        # If someone said no to the Position Question 
        if pos == "no": 
            margin = input("Enter a margin value(when in doubt, use 5): ")
            
            dont_overide = input("Do you want to make the image a seperate file(yes/no)?: ")
            if dont_overide == "yes":
                output_img = input("Enter the File Path for the Outputed PNG Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

    # If someone said no to the Color Question 
    if color == "no": 

        # Transparency Question 
        a = input("Enter transparancy value for color(225 is none, 128 is half): ")

        # Position Question 
        pos = input("Do you want to choose your watermark position(yes or no)?: ") 

        # If someone said yes to the Position Question 
        if pos == "yes": 
            x_pos = input("Enter X Position: ")
            y_pos = input("Enter Y Position: ")
            dont_overide = input("Do you want to make the image a seperate file(yes/no)?: ")
            if dont_overide == "yes":
                output_img = input("Enter the File Path for the Outputed PNG Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

        # If someone said no to the Position Question 
        if pos == "no": 
            margin = input("Enter a margin value(when in doubt, use 5): ")
            dont_overide = input("Do you want to make the image a seperate file(yes/no)?: ")
            if dont_overide == "yes":
                output_img = input("Enter the File Path for the Outputed PNG Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

    # Converts numbers from a string to a integer(number) the program can use without having a error 
    Font_Size = int(font_size)
    A = int(a)

    # If someone said yes to the Color Question 
    if color == "yes": 
        R = int(r)
        B = int(b)
        G = int(g)


    # If someone said yes to the Position Question 
    if pos == "yes":
        X_Pos = int(x_pos)
        Y_Pos = int(y_pos)

    # If someone said no to the Position Question  
    if pos == "no":
        Margin = int(margin)


    # Converts image to rgba 
    img = Image.open(watimg).convert("RGBA")
    width, height = img.size

    # Creates a new image for text 
    txt = Image.new("RGBA", img.size, (225,225,225,0))

    # Font and text settings 
    if c_font == "yes":
        font = ImageFont.truetype(font_file, Font_Size)
        draw = ImageDraw.Draw(txt)
        text = watermark
        textwidth, textheight = draw.textsize(text, font)
        
    if c_font == "no": 
        font = ImageFont.truetype('arial.ttf', Font_Size)
        draw = ImageDraw.Draw(txt)
        text = watermark
        textwidth, textheight = draw.textsize(text, font)

    # If someone said no to the Position Question 
    # If someone said yes to the Color Question
    if pos == "no" and color == "yes":
        # Calculates the position for the watermark(bottom right hand corner)
        margin = Margin 
        x = width - textwidth - margin
        y = height - textheight - margin 
        # Fill(r, g, b, a)                 V Grabs vaules from the RGBA questions 
        draw.text((x, y), text, font=font, fill=(R, G, B, A))

    # If someone said no to the Color Question
    if pos == "no" and color == "no":
        # Calculates the position for the watermark(bottom right hand corner)
        margin = Margin 
        x = width - textwidth - margin
        y = height - textheight - margin 
        # Fill(r, g, b, a)                 V Grabs vaules from the RGBA questions 
        draw.text((x, y), text, font=font, fill=(225, 225, 225, A))

    # If someone said yes to the Position Question 
    # If someone said yes to the Color Question
    if pos == "yes" and color == "yes":
        draw.text((X_Pos, Y_Pos), text, font=font, fill=(R, G, B, A))

    # If someone said no to the Color Question
    if pos == "yes" and color == "no":
        draw.text((X_Pos, Y_Pos), text, font=font, fill=(225, 225, 225, A))


    # Combines the 2 images 
    comp = Image.alpha_composite(img, txt)

    # Shows the image 
    comp.show()

    # Image saved as what was the specified file name in the file path specified 
    if dont_overide == "yes":
        comp.save(output_img)
        
    if dont_overide == "no":
        comp.save(watimg)