from typing import Counter
from PIL import Image, ImageFilter 

from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

class Filter():
    in_img = input("Enter Image File Path(can be a relative file path(ex. Watermark Adder/image.png)): ")
    filter_option = input("Choose a filter(contour, detail, edge_enhance, edge_enhance_more, emboss, find_edges, smooth, smooth_more, sharpen): ")
    
    dont_overide = input("Do you want to save as a seperate file(yes/no)?: ")
    
    if dont_overide == "yes":
        output = input("Enter the File Path for the Outputed Image(can be a relative file path(ex. Watermark Adder/image.png)): ")
    
    img = Image.open(in_img)
    
    if filter_option == "contour":
         img1 = img.filter(CONTOUR)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
   
    if filter_option == "detail":
         img1 = img.filter(DETAIL)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
            
    if filter_option == "edge_enhance":
         img1 = img.filter(EDGE_ENHANCE)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
            
    if filter_option == "edge_enhance_more":
         img1 = img.filter(EDGE_ENHANCE_MORE)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
            
    if filter_option == "emboss":
         img1 = img.filter(EMBOSS)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
            
    if filter_option == "find_edges":
         img1 = img.filter(FIND_EDGES)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
        
    if filter_option == "smooth":
         img1 = img.filter(SMOOTH)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)
            
    if filter_option == "smooth_more":
         img1 = img.filter(SMOOTH_MORE)
         img1.show()
         if dont_overide == "yes":
            img1.save(output)
            
         if dont_overide == "no":
            img1.save(in_img)