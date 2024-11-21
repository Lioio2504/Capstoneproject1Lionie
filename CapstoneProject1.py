#Data Kontak Telepon (Dictionary)
database_kontak = [
    {
        "Nama": "Amanda",
        "Alamat": "Jl. Sukses Sejati",
        "Nomor": "000 1111 3333",
        "Profesi": "Sales",
        "Usia": 25,
    },
    {
        "Nama": "Belinda",
        "Alamat": "Jl. Makmur Sejati",
        "Nomor": "000 2222 4444",
        "Profesi": "Baker",
        "Usia": 53,
    },
    {
        "Nama": "Carmane",
        "Alamat": "Jl. Indah Sejati",
        "Nomor": "000 3333 5555",
        "Profesi": "Engineer",
        "Usia": 35,
    },
    {
        "Nama": "Daniel",
        "Alamat": "Jl. Raya Sejati",
        "Nomor": "000 4444 6666",
        "Profesi": "Doctor",
        "Usia": 29,
    },
    {
        "Nama": "Emanuel",
        "Alamat": "Jl. Jaya Sejati",
        "Nomor": "000 5555 7777",
        "Profesi": "Student",
        "Usia": 15,
    }
]

menu=0
while menu!=5:
    print("Selamat datang")
    print("List Menu: ")
    print("1. Menampilkan Daftar Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Update Kontak")
    print("5. Exit Program")
    try:
        menu = int(input("Masukkan input Menu, 1-5: "))
        if menu == 1:
            #Read
            print("|Index   | Nama     \t | Alamat          \t | Nomor          \t | Profesi   \t |Usia  \t ")
            for i in range(0, len(database_kontak)):
                print(f"|{i}\t | {database_kontak[i]["Nama"]}  \t | {database_kontak[i]["Alamat"]}   \t | {database_kontak[i]["Nomor"]} \t | {database_kontak[i]["Profesi"]} \t |{database_kontak[i]["Usia"]} \t ")
        elif menu == 2:
            #Create
            nama_kontak_lama = [nama['Nama'] for nama in database_kontak]
            nama_kontak_baru = input("Masukkan update nama kontak baru: ")
            if nama_kontak_baru in nama_kontak_lama:
                print("Sudah ada kontak dengan nama tersebut! ")
            else:
                alamat_baru = str(input("Masukkan alamat kontak baru: "))
                nomor_baru = str(input("Masukkan nomor kontak baru: "))
                profesi_baru = str(input("Masukkan profesi kontak baru: "))
                usia_baru = int(input("Masukkan usia kontak baru: " ))
                database_kontak.append({
                    "Nama":nama_kontak_baru,
                    "Alamat":alamat_baru,
                    "Nomor":nomor_baru,
                    "Profesi":profesi_baru,
                    "Usia":usia_baru,
                })   
        elif menu == 3:
            #delete
            print("Database Kontak")
            print("|Index   |Nama     \t |Alamat          \t |Nomor          \t |Gender   \t |Usia  \t ")
            for i in range(0,len(database_kontak)):
                print(f"|{i}\t | {database_kontak[i]['Nama']}  \t | {database_kontak[i]['Alamat']}   \t | {database_kontak[i]['Nomor']} \t | {database_kontak[i]['Profesi']} \t |{database_kontak[i]['Usia']} \t ")
            indeks_kontak_deleted = int(input("Masukkan index kontak yang mau dihapus: "))
            del database_kontak[indeks_kontak_deleted]
        elif menu == 4:
            #update
            print("Database Kontak")
            print("|Index   |Nama     \t |Alamat          \t |Nomor          \t |Gender   \t |Usia  \t ")
            for i in range(0,len(database_kontak)):
                print(f"|{i}\t | {database_kontak[i]['Nama']}  \t | {database_kontak[i]['Alamat']}   \t | {database_kontak[i]['Nomor']} \t | {database_kontak[i]['Profesi']} \t |{database_kontak[i]['Usia']} \t ")
            indeks_kontak_updated = int(input("Masukkan index kontak yang mau diperbarui: "))
            print(f"Kontak yang akan diperbarui: {database_kontak[indeks_kontak_updated]["Nama"]}, {database_kontak[indeks_kontak_updated]["Alamat"]}, {database_kontak[indeks_kontak_updated]["Nomor"]} ")
            #print(f"Nomor kontak yang akan diperbarui: {database_kontak[indeks_kontak_updated]["Nomor"]}")
            #print(f"Alamat kontak yang akan diperbarui: {database_kontak[indeks_kontak_updated]["Alamat"]}")
            nama_kontak_updated = str(input("Masukkan nama kontak baru: "))
            nomor_kontak_updated = str(input("Masukkan nomor " + nama_kontak_updated + ": "))
            alamat_kontak_updated = str(input("Masukkan alamat " + nama_kontak_updated + ": "))
            profesi_kontak_updated = str(input("Masukkan profesi " + nama_kontak_updated + ": "))
            usia_kontak_updated = str(input("Masukkan usia " + nama_kontak_updated + ": "))
            database_kontak[indeks_kontak_updated]['Nama'] = nama_kontak_updated
            database_kontak[indeks_kontak_updated]['Nomor'] = nomor_kontak_updated
            database_kontak[indeks_kontak_updated]['Alamat'] = alamat_kontak_updated
            database_kontak[indeks_kontak_updated]['Profesi'] = profesi_kontak_updated
            database_kontak[indeks_kontak_updated]['Usia'] = usia_kontak_updated
            print(f"{nama_kontak_updated}, {nomor_kontak_updated}, {alamat_kontak_updated}")
        else:
            pass
    except Exception:
        print("Please check your input again")
