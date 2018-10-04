while True:
    print('Inputkan bilangan bulat: ',end = '')
    try:
        x = int(input())
        if x.lower() == 'exit':
            break
        else:
            if x%2 == 1:
                print(x,' adalah bilangan ganjil.')
            else:
                print(x,' adalah bilangan genap.')
    except:
        print('Invalid input, ketik exit untuk mengakhiri program.')
        x = input()
        if x.lower() == 'exit':
            break

