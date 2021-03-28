import time

time_duration = 1.5

edit = input("Hello! What do you want to do(none/watermark/blur/filter): ")

if edit == "watermark":
    print("Ok, starting watermark maker...")
    time.sleep(time_duration)
    from watermark.py import *
    
    
if edit == "blur":
    print("Ok, starting blur...")
    time.sleep(time_duration)
    from blur.py import * 
    
    
if edit == "filter":
    print("Ok, starting filter...")
    time.sleep(time_duration)
    from filters.py import * 
    

    
    
if edit == "none":
    print("Understandable, have a great day!") 