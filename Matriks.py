import math

def main():
    print('Main Menu')
    print('1. Penjumlahan')
    print('2. Perkalian')
    print('3. Pengurangan')
    print('4. Perpangkatan')
    print('Pilihan: ',end='')
    pil(int(input()))

def pil(x):
    if x == 1:
        add()
    elif x == 2:
        multiply()
    elif x == 3:
        reduction()
    elif x == 4:
        power()
    else:
        print('Tidak Valid')
        main()

def create():
    m = []
    print('Jumlah baris matriks: ',end='')
    x = int(input())
    print('Jumlah kolom matriks: ',end='')
    y = int(input())
    print('Masukkan nilai matriks, tekan enter untuk ganti barisan. Pisahkan nilai dengan ","')
    for i in range(x):
        m.append(list(map(int, input().split(","))))
    return m

def pm(m):
    for i in m:
        print(i)
    print('Tekan Enter untuk kembali ke menu utama.',end='')
    input()
    main()

def add():
    m1 = create()
    m2 = create()
    res = [[[]for j in range(len(m2[0]))]for i in range(len(m2))]
    j = 0
    if (len(m1[0]) == len(m2[0])):
        if (len(m1) == len(m2)):
            for i in range(len(m1)):
                for j in range(len(m1[0])):
                    res[i][j] = m1[i][j] + m2[i][j]
            pm(res)
    else:
        print('Matriks tidak valid, kembali ke menu utama',end='')
        input()
        main()

def reduction():
    m1 = create()
    m2 = create()
    res = [[[]for j in range(len(m2[0]))]for i in range(len(m2))]
    j = 0
    if (len(m1[0]) == len(m2[0])):
        if (len(m1) == len(m2)):
            for i in range(len(m1)):
                for j in range(len(m1[0])):
                    res[i][j] = m1[i][j] - m2[i][j]
            pm(res)
    else:
        print('Matriks tidak valid, kembali ke menu utama',end='')
        input()
        main()

def multiply():
    m1 = create()
    m2 = create()
    res = [[0 for j in range(len(m1))]for i in range(len(m2[0]))]
    if (len(m2) == len(m1[0])):
        result = kali(m1,m2,res)
        pm(result)
    else:
        print('Matriks tidak valid, kembali ke menu utama',end='')
        input()
        main()

def kali(m1,m2,res):
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][i]
    return res

def power():
    m1 = create()
    print('Pangkat: ',end='')
    p = int(input())
    if(len(m1[0]) == len(m1)):
        for i in range(1,p):
            res = [[0for j in range(len(m1[0]))]for i in range(len(m1))]
            m1 = kali(m1,m1,res)
        pm(res)
    else:
        print('Matriks tidak valid, kembali ke menu utama',end='')
        input()
        main()

main()
