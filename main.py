from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time
import os
import json

def capture_screenshot(url, output_path):
    options = Options()
    options.add_argument('--headless') 
    options.add_argument('--disable-gpu') 

    driver = webdriver.Chrome(options=options)
    capture_rect = [1320, 350, 2075, 770]
    # Coords order left, top, right, bottom
    # Picture is taken using space between left and right and top and bottom
    try:
        driver.set_window_size(2560, 1440)
        driver.get(url)
        time.sleep(3)
        
        driver.save_screenshot(output_path)
                
        im = Image.open(output_path)
        im_cropped = im.crop(capture_rect)
        im_cropped.save(output_path)
    finally:
        driver.quit()

if __name__ == "__main__":
    if not os.path.exists("Screenshots"):
        os.makedirs("Screenshots")
    with open('navigation_data.json', 'r') as file:
        data = json.load(file)
    fund_pages = data['Fundamentals']["options"]
    
    for i in fund_pages:
        url = "http://localhost:3000/fundamentals/"
        url = url + "" + i["urlKey"]
        path = "Screenshots/" + i["urlKey"] + ".png"
 
        capture_screenshot(url, path)

        
   
