def parseTxtFile(filename, array):
    try:
        f = open(f'{filename}.txt', encoding='utf-8')

        for str in f:
            user = str.split('\n')[0]
            user = user.replace(' ', '')

            if (user != ''):
                array.append(user)

        f.close()
    except:
        print(f'Can\'t open file {filename}.txt')