import falcon
import os
import base64
from falcon_multipart.middleware import MultipartMiddleware
from selenium import webdriver
import chromedriver_binary
import os


def screenshot(data, tempPng): 
    tempHtml = 'temp.html'
    with open(tempHtml, 'wb') as f:
      f.write(data)
    options = webdriver.ChromeOptions() 
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options) 
    file_name = f'file:///{os.path.join(os.path.dirname(os.path.abspath(__file__)),tempHtml)}'.replace(os.sep,"/") 
    driver.get(file_name) 
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X) 
    driver.set_window_size(S('Width'),S('Height')) 
    driver.find_element_by_tag_name('body').screenshot(tempPng)
    os.remove(tempHtml)


class Image:

    def on_post(self, req, resp):
        data = req.stream.read()
        tempPng = 'temp.jpg'
        screenshot(data, tempPng)
        resp.downloadable_as = tempPng
        resp.content_type = 'image/png'
        resp.stream = open(tempPng, 'rb')
        resp.content_length = os.path.getsize(tempPng)
        resp.status = falcon.HTTP_200
        os.remove(tempPng)


app = falcon.API(middleware=[MultipartMiddleware()])
app.add_route('/image', Image())
