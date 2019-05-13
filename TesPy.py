# Creater: Cooler
# Data create: 12.05.2019
# Last update: 13.05.2019

from googletrans import Translator
from sys import platform
import re
import os
if platform == 'linux' or platform == 'linux2':
    clearcmd = 'clear'
elif platform == 'win32':
    clearcmd = 'cls'
clear = lambda:os.system(clearcmd)
translator = Translator()
clear()
print('[TESPY] Creator: Cooler010\n')
nametextfile = input('Имя файла(с расширением): ')
clear()
# Read file
file = open(nametextfile,'r+')
data = file.read()
occ = [m.end() for m in re.finditer('"', data)]

x = 0
y = 1

while y < len(occ):
    occ = [m.end() for m in re.finditer('"', data)]
    text = data[occ[x]:occ[y]-1] ; print(text)
    quest1 = input('[1] Перевести\n[2] Продолжить\n[3] Вернуться\n[4] Завершить работу\n>>> ')
    if quest1 == '1':
        clear()
        translate = translator.translate(text, dest='ru')
        print(translate.text)
        quest2 = input('[1] Сохранить\n[2] Ввести вручную\n[3] Отменить\n>>> ')
        if quest2 == '1':
            clear()
            data = data[:occ[x]] + translate.text + data[occ[y]-1:]
        elif quest2 == '2':
            txtforquest = input('Ваш текст: ')
            data = data[:occ[x]] + txtforquest + data[occ[y]-1:]
            clear()
    elif quest1 == '2':
        clear()
    elif quest1 == '3':
        clear()
        x -= 2 ; y -= 2
        continue
    elif quest1 == '4':
        break
    x += 2 ; y += 2

output = open('log.txt','w', encoding='utf-8')
output.write(data)
output.close()
print('Программа завершена. Результат сохранён в [log.txt]')
