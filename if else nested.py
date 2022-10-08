mulai = False
jalan = False
berhenti = False
while True:
    perintah = input("masukkan perintah: ")
    if perintah == "nyala":
        if mulai:
            print("mobil sudah menyala")
        else:
            mulai = True
            print("mobil menyala ")
    elif perintah == "jalan":
        if jalan:
            print("mobil sudah berjalan")
        else:
            jalan = True
            print("mobil berjalan")
    elif perintah == "stop":
        if berhenti:
            print("mobil sudah berhenti")
        else:
            berhenti = True
            print("mobil berhenti")
    else:
        print("input salah dan program telah berhenti")
        break

