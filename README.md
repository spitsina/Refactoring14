PIXEL ART


С помощью приложения вы накладываете фильтр, получаете черно-белый пиксель-арт, который можно набрать уже мозаикой.


В результате из такой картинки:

![Исходная каритинка](https://pbs.twimg.com/media/original.jpg)

![Запуск filter.py](https://pbs.twimg.com/media/filter.py.png)

![Запуск old_filter.py](https://pbs.twimg.com/media/old_filter.py.png)

![Запуск filter_with_filename.py](https://pbs.twimg.com/media/filter_with_filename.py.png)

![Результат](https://github.com/bibilov/refactoring/blob/main/Black-White.jpg)

![ТЕСТИРОВАНИЕ И ОТЛАДЧИК](https://pbs.twimg.com/media/тестирование1.png https://pbs.twimg.com/media/тестирование2.png https://pbs.twimg.com/media/отладчик.png)

Мы получаем огромную разницу во времени из-за ожидания пользовательского воода в файле filter.py. В файле filter_with_filename.py изначало прописано имя картинки и прочие необходимые нам параметры. За счет этого небольшого изменения время выполнение программы существенно сократилось. Полученное время намного меньше времени выполнения old_filter.py. Из этого можем сделать вывод, что отрефакторенный код намного быстрее первоначального.
