


# TesPy

TesPy - помощник для перевода RenPy игр адаптированный под Windows и Linux, работающий в терминале.

## Установка

Скачайте и установите [Python 3](https://www.python.org/downloads/release)

Далее в терминале
```
pip install googletrans
cd path\to\program
python TesPy.py
```
Все готово. Удачи в переводе!

## Инструкция

Вначале введите название файла, который хотите перевести (Например: screens.rpy)
1) Перевести - переводит файл на русский язык
   * Сохранить - сохраняет результат и переходит к следующему слову
   * Ввести вручную - вводите свой перевод слова
   * Отменить - сбрасывает результат и переходит к следующему слову
2) Продолжить - пропускает слово
3) Вернуться - возвращается к предыдущему слову
4) Завершить работу - сохраняет результат в log.txt и закрывает программу

__После завершения работы весь переведенный текст сохраняется в log.txt в папке с программой.__

## Функционал

* Автоматический поиск слов для перевода в файле
* Автоматический перевод слов с помощью Google
* Возможность корректировки текста вручную

## Идея автора

Изначальной задумкой было сделать программу которая автоматически переводила бы игры на RenPy.
Но технически реализовать корректный перевод без участия человека для меня было не выполнимой задачей.
Поэтому каждый перевод проверяется и корректируется вами. С уважением cooler010.

### Last update: 13.05.2019 version=1.0.1
