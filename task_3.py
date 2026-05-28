file1 = open('resource/file1.txt', 'r', encoding='utf-8')
text1 = file1.read()
file1.close()

file2 = open('resource/file2.txt', 'r', encoding='utf-8')
text2 = file2.read()
file2.close()

file3 = open('resource/file3.txt', 'r', encoding='utf-8')
text3 = file3.read()
file3.close()

combined_file = open('resource/combined.txt', 'w', encoding='utf-8')

combined_file.write('=== Содержимое file1.txt ===\n')
combined_file.write(text1)
combined_file.write('\n\n')

combined_file.write('=== Содержимое file2.txt ===\n')
combined_file.write(text2)
combined_file.write('\n\n')

combined_file.write('=== Содержимое file3.txt ===\n')
combined_file.write(text3)

combined_file.close()

print('Какие мы молодцы! Файлы объединены в combined.txt')