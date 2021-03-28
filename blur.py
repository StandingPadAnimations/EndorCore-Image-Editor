from PIL import Image, ImageFilter

class Blur(): 
    # Prompts
    in_img = input("Enter Image File Path(can be a relative file path(ex. Watermark Adder/image.png)): ")
    blur_type = input("What type of bluring(simple/box/gaussian)?: ")

    # If someone choose box
    if blur_type == "box":
        radius = input("What do you want the radius to be?: ")
      
    # If some choose gaussian 
    if blur_type == "gaussian":
        radius = input("What do you want the radius to be?: ")

    dont_overide = input("Do you want to save as a seperate file(yes/no)?: ")
    
    # If someone choose yes for dont_overide 
    if dont_overide == "yes":
        output = input("Enter the File Path for the Outputed Image(can be a relative file path(ex. Watermark Adder/image.png)): ")

    # If someone choose box
    if blur_type == "box":
        Radius = int(radius)
        
    # If some choose gaussian 
    if blur_type == "gaussian":
        Radius = int(radius)


    img = Image.open(in_img)

    # Simple blur
    if blur_type == "simple": 
        blurImage = img.filter(ImageFilter.BLUR)
        
        blurImage.show()
        
        if dont_overide == "yes":
            blurImage.save(output)
        
        if dont_overide == "no":
            blurImage.save(img)

    # Box blur 
    if blur_type == "box":
        blurImage = img.filter(ImageFilter.BoxBlur(Radius))
        
        blurImage.show()
        
        if dont_overide == "yes":
            blurImage.save(output)
        
        if dont_overide == "no":
            blurImage.save(img)
    
    # Gaussian blur         
    if blur_type == "gaussian":
        blurImage = img.filter(ImageFilter.GaussianBlur(Radius))
        
        blurImage.show()
        
        if dont_overide == "yes":
            blurImage.save(output)
        
        if dont_overide == "no":
            blurImage.save(img)
    




