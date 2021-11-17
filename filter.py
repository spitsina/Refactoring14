from PIL import Image
import numpy as np

class PixelArt:
    def __init__(self, pixel_array, pixel_size:int, graduation:int):
        self.image = np.array(pixel_array)
        self.size = pixel_size
        self.graduation = graduation
        self.height = len(self.image)
        self.width = len(self.image[0])

    def make_image_grey(self):
        for pix_width in range(0, self.width, self.size):
            for pix_height in range(0, self.height, self.size):
                self.make_color_grey(color=self.make_medium_color(pix_width, pix_height), pix_width=pix_width, pix_height=pix_height)
        return Image.fromarray(self.image)

    def make_medium_color(self, pix_width, pix_height):
        color = 0
        for column in range(pix_width, pix_width + self.size):
            for line in range(pix_height, pix_height + self.size):
                color += sum([int(self.image[column][line][j]) for j in range(3)])
        return int(color / 3 // (self.size ** 2))

    def make_color_grey(self, color, pix_width, pix_height):
        for column in range(pix_width, pix_width + self.size):
            for line in range(pix_height, pix_height + self.size):
                self.image[column][line][0] = int(color // self.graduation) * self.graduation
                self.image[column][line][1] = int(color // self.graduation) * self.graduation
                self.image[column][line][2] = int(color // self.graduation) * self.graduation
                
img = Image.open("img2.jpg")
graduation = 50
pixel_size = 10
res = PixelArt(pixel_array=img, pixel_size=pixel_size, graduation=graduation).make_image_grey()
res.save('res.jpg')
