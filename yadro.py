import random


def lock(data, A1, key):
    if len(A1) != len(key):
        print("Критическая ошибка!/nДлина алфавита не совпадает с длиной ключа.")
        exit()
    dict = {}
    for i, e_ in enumerate(A1):
        dict.update({A1[i]: key[i]})
    lock_data = ''
    for symb in data:
        lock_data += dict.get(symb)
    file = open('locked_data.txt', 'w', encoding="utf-8")
    file.write(lock_data)
    file.close()
    return (lock_data)


def unlock(lock_data, A1, key):
    if len(A1) != len(key):
        print("Критическая ошибка!/nДлина алфавита не совпадает с длиной ключа.")
        exit()
    dict = {}
    for i, e_ in enumerate(key):
        dict.update({key[i]: A1[i]})
    unlock_data = ''
    for element in lock_data:
        unlock_data += dict.get(element)
    file = open('data.txt', 'w', encoding="utf-8")
    file.write(unlock_data)
    file.close()
    return (unlock_data)


def generator(A1):
    text = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()'
    seed = list(text)
    random.shuffle(seed)
    key = ''.join(seed[:len(A1)])
    file = open('key.txt', 'w', encoding="utf-8")
    file.write(key)
    file.close()
    return (key)


file = open('data.txt', encoding="utf-8")
data = file.read()
file.close()

file = open('locked_data.txt', encoding="utf-8")
locked_data = file.read()
file.close()

file = open('A1.txt', encoding="utf-8")
A1 = file.read()
file.close()

print("Сгенерировать новый ключ? (Y/N)")
q1 = input()

if q1 == ("Y") or q1 == ("y"):
    generator(A1)
    file = open('key.txt')
    key = file.read()
    file.close()
    print("ВНИМАНИЕ! После создания нового ключа доступно только ШИФРОВАНИЕ.\n"
          "Если дешифровать ключом которым не производилось шифрование, то данные искозятся.", end='\n\n')
else:
    file = open('key.txt')
    key = file.read()
    file.close()

print("Для шифрования нажмите 1, а для дешифрования нажмите 2.")
q2 = input()

if q2 == ("1"):
    print(lock(data, A1, key) + "\n\nВы успешно зашифровали сообщение!"
                                "\nВаше сообщение сохраннено в файл locked_data.")
    exit()
elif q2 == ("2"):
    print(
        unlock(locked_data, A1, key) + "\n\nВы успешно расшифровали сообщение!"
                                       "\nВаше сообщение сохраннено в файл data.")
    exit()
