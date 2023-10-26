kendaraan=["mobil","sport","mercedes-AMG GT",3.982]
kendaraan.append("black")
print(kendaraan)
kendaraan.append("roda 4")
print(kendaraan)
kendaraan.append("Rp.3,4 Miliar")
kendaraan.remove("sport")
print(kendaraan)

pilihan=input("masukan pilihan")
match pilih:
    case"luas kotak":
        print("sisi*sisi*sisi")
    case("luas lingkaran"):
        print("22/7*r*r")
    case("luas segitiga"):
        print("1/2*alas*tinggi")
    case _:
        print("masukan kembali pilihan")
