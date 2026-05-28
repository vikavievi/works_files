alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Ф - шифрования
def encrypt(text):
    result = ''
    for char in text:
        if char.islower():
            pos = alphabet_lower.find(char)
            new_pos = (pos + 3) % 26
            result = result + alphabet_lower[new_pos]
        elif char.isupper():
            pos = alphabet_upper.find(char)
            new_pos = (pos + 3) % 26
            result = result + alphabet_upper[new_pos]
        else:
            result = result + char
    return result

#Ф - расшифровки
def decrypt(text):
    result = ''
    for char in text:
        if char.islower():
            pos = alphabet_lower.find(char)
            new_pos = (pos - 3) % 26
            result = result + alphabet_lower[new_pos]
        elif char.isupper():
            pos = alphabet_upper.find(char)
            new_pos = (pos - 3) % 26
            result = result + alphabet_upper[new_pos]
        else:
            result = result + char
    return result

# Исходный
file = open('resource/secret.txt', 'r', encoding='utf-8')
original = file.read()
file.close()

# Зашифрованный
encrypted = encrypt(original)
file_out = open('resource/encrypted.txt', 'w', encoding='utf-8')
file_out.write(encrypted)
file_out.close()

# Расшифрованный
decrypted = decrypt(encrypted)
file_out = open('resource/decrypted.txt', 'w', encoding='utf-8')
file_out.write(decrypted)
file_out.close()

print('Готово!')
print('Исходный текст:', original)
print('Зашифрованный:', encrypted)
print('Расшифрованный:', decrypted)