def NIM(nim):
    list(nim)
    if len(nim) > 9:
        if len(nim) < 11:
            univ = []
            fakultas = []
            jurusan = []
            angkatan = []
            kodeM = []
            univ.append(nim[0])
            fakultas.append(nim[1])
            jurusan.append(nim[2])
            jurusan.append(nim[3])
            angkatan.append(nim[4])
            angkatan.append(nim[5])
            for i in range(6,10):
                kodeM.append(nim[i])
            print(nim)
            print("".join(univ),'adalah kode universitas')
            print("".join(fakultas),'adalah kode fakultas')
            print("".join(jurusan),'adalah kode jurusan')
            print("".join(angkatan),'adalah kode angkatan')
            print("".join(kodeM),'adalah kode mahasiswa')
            input()
    else:
        print('NIM kurang dari 10 digit')
        print('Silahkan input 10 digit NIM anda')
        NIM(input())

NIM(input())
    
