import random


def lock(data, Alphabet, key):
    if len(Alphabet) != len(key):
        print("Критическая ошибка!\nДлина алфавита не совпадает с длиной ключа.")
        exit()
    dict = {}
    for i, e_ in enumerate(Alphabet):
        dict.update({Alphabet[i]: key[i]})
    lock_data = ''
    for symbol in data:
        lock_data += dict.get(symbol)
    file = open('locked_data.txt', 'w', encoding="utf-8")
    file.write(lock_data)
    file.close()
    return lock_data


def unlock(lock_data, Alphabet, key):
    if len(Alphabet) != len(key):
        print("Критическая ошибка!\nДлина алфавита не совпадает с длиной ключа.")
        exit()
    dict = {}
    for i, e_ in enumerate(key):
        dict.update({key[i]: Alphabet[i]})
    unlock_data = ''
    for element in lock_data:
        unlock_data += dict.get(element)
    file = open('open_data.txt', 'w', encoding="utf-8")
    file.write(unlock_data)
    file.close()
    return unlock_data


def generator(Alphabet):
    text = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()'
    seed = list(text)
    random.shuffle(seed)
    key = ''.join(seed[:len(Alphabet)])
    file = open('key.txt', 'w', encoding="utf-8")
    file.write(key)
    file.close()
    return key


def main():
    file = open('open_data.txt', encoding="utf-8")
    open_data = file.read()
    file.close()

    file = open('locked_data.txt', encoding="utf-8")
    locked_data = file.read()
    file.close()

    file = open('Alphabet.txt', encoding="utf-8")
    Alphabet = file.read()
    file.close()

    print("Сгенерировать новый ключ? (Y/N)")
    q1 = input()

    if q1 == ("Y") or q1 == ("y"):
        generator(Alphabet)
        file = open('key.txt')
        key = file.read()
        file.close()
        print("ВНИМАНИЕ! После создания нового ключа доступно только ШИФРОВАНИЕ.\n"
              "Если дешифровать ключом которым не производилось шифрование, то данные искозятся.", end='\n\n')
        print("Шифровать данные? Y/N")
        q2 = input()
        if q2 == ("Y") or q2 == ("y"):
            print(lock(open_data, Alphabet, key) + "\n\nВы успешно зашифровали сообщение!"
                                                   "\nВаше сообщение сохраннено в файл locked_data.txt")
            exit()
        else:
            exit()
    else:
        file = open('key.txt')
        key = file.read()
        file.close()

    print("Для шифрования нажмите 1, а для дешифрования нажмите 2.")
    q3 = input()

    if q3 == ("1"):
        print(lock(open_data, Alphabet, key) + "\n\nВы успешно зашифровали сообщение!"
                                               "\nВаше сообщение сохраннено в файл locked_data.txt")
        exit()
    elif q3 == ("2"):
        print(
            unlock(locked_data, Alphabet, key) + "\n\nВы успешно расшифровали сообщение!"
                                                 "\nВаше сообщение сохраннено в файл open_data.txt")
        exit()


if __name__ == '__main__':
    main()
