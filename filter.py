from PIL import Image
import numpy as np

def get_pixel_image(image, pixel_size = 10, gradation = 5):
    array_img = np.array(image).astype(int)
    height_img = len(array_img[0])
    length_img = len(array_img)
    gradation_img = 255 // gradation
    i = j = 0
    while i < length_img:
        while j < height_img:
            colors_sum = get_elem_sum(array_img, pixel_size, i, j)
            average_color = int(colors_sum // (pixel_size ** 2))
            set_color(int(average_color // gradation_img) * gradation_img / 3, array_img, pixel_size, i, j)
            j += pixel_size
        i += pixel_size
    return Image.fromarray(np.uint8(array_img))


def get_elem_sum(img, pixel_size, i, j):
    color_sum = 0
    for sector1 in range(i, i + pixel_size):
        for sector2 in range(j, j + pixel_size):
            n1 = img[sector1][sector2][0]
            n2 = img[sector1][sector2][1]
            n3 = img[sector1][sector2][2]
            M = n1 + n2 + n3
            color_sum += M
    return color_sum


def set_color(new_color, vector, pixel_size, i, j):
    for sector1 in range(i, i + pixel_size):
        for sector2 in range(j, j + pixel_size):
            for c in range(3):
                vector[sector1][sector2][c] = new_color


original_img = Image.open("img2.jpg")
result = get_pixel_image(image = original_img, pixel_size = int(input()), gradation = int(input()))
result.save('res.jpg')
