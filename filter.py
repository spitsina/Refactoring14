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
    
flag = 'no'
while flag == 'no':
    print('Введите название фото')
    initialImg = Image.open('{}'.format(input()))
    print('Выберите величину ячейки\n' +
          'Размер должен быть инициализирован целым положительным числом')
    picSize = int(input())
    print('Выберите количество оттенков\n' +
          'Количество должно быть инициализировано целым положительным числом')
    grad = int(input())
    arr = MonochromePhoto(initialImg, pixSize=picSize, gradation=grad).get_grey_image()
    print('Введите название новой картинки')
    name = input()
    print('Введите формат нового фото(jpg, png и т.д.)')
    formt = input()
    arr.save('{}.{}'.format(name, formt))
    print('Если хотите завершить сессию, наберите \'yes\', если нет-нажмите enter')
    if input() == 'yes':
        flag = 'yes'
