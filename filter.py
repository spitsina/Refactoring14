import numpy as np
from PIL import Image
class MonochromePhoto:
    def __init__(self, pixArray, pixSize=10, gradation=5):
        self.image = np.array(pixArray)
        self.size = pixSize
        self.grad = 255 // gradation
        self.width = len(self.image) 
        self.height = len(self.image[0])
        
    def get_grey_image(self):        
        for x in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):                
                    self.image[x:x + self.size, y:y + self.size] = self.get_medium_color(x, y)
        return Image.fromarray(self.image)    
    def get_medium_color(self, x, y):
        return int(self.image[x:x + self.size, y:y + self.size].sum() / 3 // self.size ** 2 // self.grad * self.grad)
    
initialImg = Image.open("img2.jpg")
arr = MonochromePhoto(initialImg=initialImage, pixSize=int(input()), gradation=int(input())).get_monochrome_photo()
arr.save('res.jpg')
