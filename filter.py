from PIL import Image
import numpy as np


def get_mosaice_image(image, mosaice_size=10, gradation=4):
    threshold = 255 // gradation
    processed_image = np.array(image)
    image_length = len(processed_image)
    image_height = len(processed_image[1])
    i = 0
    while i < image_length - 1:
        j = 0
        while j < image_height - 1:
            matrix_sum = get_matrix_sum(processed_image, mosaice_size, i, j)
            average_color = int(matrix_sum // (mosaice_size ** 2))
            set_color(int(average_color // threshold) * threshold / 3, processed_image, i, j, mosaice_size)
            j += mosaice_size
        i += mosaice_size

    return Image.fromarray(np.uint8(processed_image))


def get_matrix_sum(source_color, size, i, j, ):
    color_sum = 0
    for sector_i in range(i, i + size):
        for sector_j in range(j, j + size):
            M = 0
            for color_id in range(3):
                M += source_color[sector_i][sector_j][color_id]
            color_sum += M
    return color_sum


def set_color(new_color, source_color, i, j, size):
    for sector_i in range(i, i + size):
        for sector_j in range(j, j + size):
            for color_id in range(3):
                source_color[sector_i][sector_j][color_id] = new_color


if __name__ == "__main__":
    img = Image.open("img2.jpg")
    res = get_mosaice_image(img)
    res.save('res.jpg')
