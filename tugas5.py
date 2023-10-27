kendaraan = ["mobil","sport","mercedes-AMG GT",3.982]
kendaraan.append("pink")
print(kendaraan)
kendaraan.append("roda 4")
print(kendaraan)
kendaraan.append("Rp.3,4 Miliar")
kendaraan.remove("sport")
print(kendaraan)


pilihan = input("masukan pilihan:")
match pilihan:
    case "1":
        s = int(input("masukan sisi:"))
        persegi = s*s
        print("luas persegi",persegi)
    case "2":
        phi = 3,14
        r = int(input("masukan jari:"))
        lingkaran = phi*r*r
        print("luas lingkaran",lingkaran)
    case "3":
        l = 1/2
        a = int(input("masukan alas:"))
        t = int(input("masukan tinggi"))
        segitiga = l*a*t
        print("luas segitiga",segitiga)
    case _:
        print("pilihan tidak tersedia")


   