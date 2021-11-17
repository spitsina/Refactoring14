from PIL import Image
import numpy as np
def get_pixel_image(image, pixel_size = 10, gradation = 5):
    gradation_img = 255 // gradation
    array_img = np.array(image).astype(int)
    length_img = len(array_img)
    height_img = len(array_img[0])
    i = j = 0
    while i < length_img:
        while j < height_img:
            sector = array_img[i: i + pixel_size, j: j + pixel_size]
            colors_sum = np.sum(sector)
            average_color = int(colors_sum // (pixel_size ** 2))
            set_color(int(average_color // gradation_img) * gradation_img / 3, array_img, pixel_size, i, j)
            j += pixel_size
        i += pixel_size
    return Image.fromarray(np.uint8(array_img))

def set_color(new_color, vector, pixel_size, i, j):
    for sector1 in range(i, i + pixel_size):
        for sector2 in range(j, j + pixel_size):
            for c in range(3):
                vector[sector1][sector2][c] = new_color
                
original_img = Image.open("img2.jpg")
result = get_pixel_image(image = original_img, pixel_size = int(input()), gradation = int(input()))
result.save('res.jpg')
