search_word = input('Введите слов для поиска: ')

file = open('text.txt', 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()

found_lines = []
total_count = 0

for i in range(len(lines)):
    line = lines[i]

    line_lower = line.lower()
    word_lower = search_word.lower()

    words = line_lower.split()

    count_in_line = words.count(word_lower)

    if count_in_line > 0:
        total_count = total_count + count_in_line
        found_lines.append(i + 1)

print('\nРЕЗУЛЬТАТ ПОИСКА')

if total_count > 0:
    print('Слово найдено')
    print('Количество вхождений:', total_count)
    print('Строки:', found_lines)
else:
    print('Слово не найдено')
    print('Количество вхождений: 0')
    print('Строки: []')

result_file = open('search_results.txt', 'w', encoding='utf-8')
result_file.write('Искомое слово: ' + search_word + '\n')
result_file.write('Найдено: ' + ('да' if total_count > 0 else 'нет') + '\n')
result_file.write('Количество вхождений: ' + str(total_count) + '\n')
result_file.write('Номера строк: ' + str(found_lines) + '\n')
result_file.close()

print('\nРезультат также сохранён в файл search_results.txt')