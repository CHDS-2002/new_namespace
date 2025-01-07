# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')


# single_root_words - функция для создания списка
#                   с однокоренными словами
def single_root_words(root_word, *other_words):
    same_words = []

    # Поиск однокоренных слов
    for word in other_words:
        if (root_word.lower() in word.lower()
                or word.lower() in root_word.lower()):
            same_words.append(word)

    return same_words


# print_root_words - функция для вывода однокоренными словами
def print_root_words(result):
    print('Однокоренные слова: ', result, end='.\n')


# Найдём однокоренные слова
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выведем однокоренные слова
print('\nВЫВОД ДАННЫХ\n')
print_root_words(result1)
print_root_words(result2)
print()

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
