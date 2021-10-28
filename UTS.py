user = [
    {
        "saldo" : 200000
    }
]

def cek_saldo():
    for i in range(len(user)):
        return int(i)
    return -1

def tambah_saldo(uang):
     if user ["saldo"] >= int(uang):
        user['saldo'] = user['saldo'] + int(uang)
        print("Anda berhasil menambahkan uang sebesar Rp." + int(uang))
        print("sisa saldo anda adalah Rp.",user['saldo'])
     else:
        print("Ops saldo anda tidak cukup") 

def ambil_saldo(uang):
    if user ["sald0"] >= int(uang):
        user ["saldo"] = user ["saldo"] - int(uang)
        print("Anda berhasil menarik uang sebesar Rp." + int(uang))
        print("Sisa saldo anda adalah Rp.", user ["saldo"])
    else:
        print("Oops Saldo tidak mencukup")


print("SELAMAT DATANG DI ATM Pesonainformatika")
print("1.Informasi Saldo")
print("2.Tambah saldo")
print("3.Ambil Saldo")
print("4.Keluar")
print("================")
a = int(input("Silahkan pilih menu : "))
if a == 1:
    print("")
    print("Sisa Saldo anda adalah Rp.", ["saldo"])
    print("")
    print("")
elif a == 2:
    print("Silahkan masukan nominal yang yang akan di transfer")
    nominal = input("Nominal Yang Akan Di Tambahkan: ")
    tambah_saldo(nominal)
    print("")
elif a == 3:
    nominal = input("Nominal Yang Akan Di Tarik : ")
    ambil_saldo(nominal)
    print("")
elif a == 4:
    exit
else:
    print("pilihan tidak tersedia")