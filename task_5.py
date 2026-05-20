file = open('words.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
# Пропуск пустот
words = []
for line in lines:
    word = line.strip()
    if word != '':
        words.append(word)

# Сортировка по алфавиту
alphabetical = sorted(words)

# Сортировка по длине слова
by_length = sorted(words, key=len)

# Сортировка в обратном алф порядке
reverse_alphabetical = sorted(words, reverse=True)


# Запись результатов
file_out = open('sorted_alphabetically.txt', 'w', encoding='utf-8')
for word in alphabetical:
    file_out.write(word + '\n')
file_out.close()

file_out = open('sorted_by_length.txt', 'w', encoding='utf-8')
for word in by_length:
    file_out.write(word + '\n')
file_out.close()

file_out = open('sorted_reverse.txt', 'w', encoding='utf-8')
for word in reverse_alphabetical:
    file_out.write(word + '\n')
file_out.close()

print('Готово! Созданы файлы:')
print('sorted_alphabetically.txt (по алфавиту A-Z)')
print('sorted_by_length.txt (по длине слова, от коротких к длинным)')
print('sorted_reverse.txt (обратный алфавитный порядок Z-A)')

print('\nРЕЗУЛЬТАТ')
print('Исходные слова:', words)
print('По алфавиту:', alphabetical)
print('По длине:', by_length)
print('Обратный алфавит:', reverse_alphabetical)