def hitung_bmi(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan ** 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kekurangan berat badan. Disarankan untuk meningkatkan pola makan sehat dan berkonsultasi dengan ahli gizi."
    elif 18.5 <= bmi < 24.9:
        return "Berat badan normal. Pertahankan gaya hidup sehat dan pola makan seimbang."
    elif 25 <= bmi < 29.9:
        return "Kelebihan berat badan. Disarankan untuk melakukan olahraga secara teratur dan memperhatikan pola makan."
    else:
        return "Obesitas. Disarankan untuk berkonsultasi dengan dokter atau ahli gizi untuk merencanakan program penurunan berat badan."

def kalkulator_bmi():
    print("Selamat datang di Kalkulator BMI!")
    
    try:
        berat_badan = float(input("Masukkan berat badan Anda (kg): "))
        tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))
        
        if berat_badan <= 0 or tinggi_badan <= 0:
            print("Berat badan dan tinggi badan harus lebih dari 0. Coba lagi.")
            return
        
        bmi = hitung_bmi(berat_badan, tinggi_badan)
        
        print(f"\nHasil perhitungan BMI Anda: {bmi:.2f}")
        print(kategori_bmi(bmi))
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

if __name__ == "__main__":
    kalkulator_bmi()
