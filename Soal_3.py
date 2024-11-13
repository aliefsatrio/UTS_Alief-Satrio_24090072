def hitung_total_harga(jumlah_barang):
    total_harga = 0
    for i in range(jumlah_barang):
        harga = float(input(f"Masukkan harga barang ke-{i+1}: "))
        total_harga += harga
    return total_harga

def main():
    jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: "))

    if jumlah_barang <= 0:
        print("Jumlah barang harus lebih dari 0!")
        return

    total_harga = hitung_total_harga(jumlah_barang)

    print(f"\nTotal harga belanjaan Anda adalah: Rp {total_harga:.2f}")

if __name__ == "__main__":
    main()
