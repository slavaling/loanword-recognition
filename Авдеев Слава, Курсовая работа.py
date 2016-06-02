import re


def choose_lang():
    lang = str(input('Укажите на каком языке написан текст: ')) 
    if lang == 'Татарский':
        file3 = open('tatar.txt', 'r', encoding='utf-8')
    elif lang == 'Аварский':
        file3 = open('avar.txt', 'r', encoding='utf-8')
    elif lang == 'Удмуртский':
        file3 = open('udmurt.txt', 'r', encoding='utf-8')
    elif lang == 'Мокшанский':
        file3 = open('moksh.txt', 'r', encoding='utf-8')
    else:
        print('Такого языка в базе данных нет')
        exit(0)
    suff = file3.read()
    file3.close()
    suff = suff.split() 
    return suff


def get_words():
    words = []
    file = open('text1.txt', 'r', encoding='utf-8')
    text = file.read()
    text = text.split()
    file.close()
    for i in text:
        i = i.strip(',!."\'?:;`~(){}[]\\/—-|«»@\r\n')
        i = i.lower()
        i = re.sub('[0-9]+', '', i)
        if i != '':
            words.append(i)
    return words


def Russian_Words():
    ListOfRus = []
    file2 = open('rus.txt', 'r', encoding='utf-8')
    ListOfRus = file2.read()
    ListOfRus = ListOfRus.split()
    file2.close()
    return ListOfRus


def borrowed_words(words, ListOfRus, suff):
    n = ''
    result = []
    for i in words:
        if i in ListOfRus:
            if len(i) > 4:
                result.append(i)
        else:
            for j in suff:
                if i.endswith(j):
                    n = re.sub(j + '$', '', i)
                    if n in ListOfRus:
                        if len(n) > 4:
                            result.append(i)
                            break
                    else:
                        n = n + 'ь'
                        if n in ListOfRus:
                            if len(n) > 4:
                                result.append(i)
                                break
    return result


def ListOfBorrowedWords(result):
    file4 = open('result.txt', 'w', encoding='utf - 8')
    if result == []:
        file4.write('Заимствований обнаружено не было')
        file4.close()
    else:
        file4.write('Были обнаружены следующие заимствования:')
        file4.write('\r\n\r\n')
        for i in result:
            file4.write(i)
            file4.write('\r\n')
    file4.close()


ListOfBorrowedWords(borrowed_words(get_words(), Russian_Words(), choose_lang()))
    

