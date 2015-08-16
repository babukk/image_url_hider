#! /usr/bin/env python
# -*- coding: utf-8 -*-

my_html_string = '''талии типа: низкой талией
одежды двери лацкан: наборы руководителя
поп-элементов: спинкиплатье веб -.
перечисленные год/Сезон: Лето 2015
материал: спандекс/лайкра
состав: хлопок
компонент содержания: 71-80%
Цвет: черный
Размер: средний ярдов
ли внешняя торговля: да
ли бесшовные: является
чтобы применить Пол: Женский <br>
<img src="http://i03.c.aliimg.com/img/ibank/2015/210/543/2037345012_1560732369.jpg" style="width: 49%;"><br>
<img src="http://i03.c.aliimg.com/img/ibank/2015/086/933/2037339680_1560732369.jpg" style="width: 49%;">
'''





import requests

# url = 'http://127.0.0.1:5000/replace_img_src'
url = 'http://92.63.102.86/replace_img_src'


response = requests.post(url, data={'html': my_html_string}).json()

print  response['html']




