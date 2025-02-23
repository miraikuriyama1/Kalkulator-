def kalkulator_al():
    print("Pilih perjumlahan coy:")
    print("1. tambah (+)")
    print("2. kurang (-)")
    print("3. kali (*)")
    print("4. bagi (/)")

    perhitungan = input("pilih perhitungan (1/2/3/4): ")
    angka1 = float(input("angka pertama: "))
    angka2 = float(input("angka kedua: "))

    if perhitungan == '1':
        hasil = angka1 + angka2
        simbol = '+'
    elif perhitungan == '2':
        hasil = angka1 - angka2
        simbol = '-'
    elif perhitungan == '3':
        hasil = angka1 * angka2
        simbol = '*'
    elif perhitungan == '4':
       if angka2 != 0:
          hasil = angka1 / angka2
          simbol = '/'
       else:
           print("Error! ngak bisa di bagi sama 0 .")
           return
    else:
        print("pilihan tidak valid!")
        return
    
    print(f"Hasil: {angka1} {simbol} {angka2} = {hasil}")

kalkulator_al()