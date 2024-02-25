# Bu Python kodu, alfa-beta budama algoritmasını kullanarak bir min-max ağacını arar. İşlevlerin ve değişkenlerin ne yaptığını açıklayalım:

# agac: Min-max ağacını temsil eden bir liste. Her düğüm, alt düğümleri içeren bir liste içerir. En üst düzeydeki liste, kök düğümü temsil eder.

# kok: Ağacın kök düğümünün derinliğini temsil eden bir tamsayı.

# budama: Alfa-beta budama sırasında yapılan budama işlemlerinin sayısını izleyen bir sayaç.

# cocuklar(dal, derinlik, alfa, beta): Rekürsif olarak ağacın her düğümünü dolaşan ve alfa-beta budama işlemlerini gerçekleştiren bir fonksiyon. 
# dal parametresi, mevcut düğümün alt düğümlerini temsil eder. derinlik, mevcut düğümün ağaçtaki derinliğini belirtir. alfa ve beta, mevcut düğüm için en iyi bilinen değerlerdir.

# alfabeta(in_agac=agac, baslangıc=kok, alt=-15, ust=15): Alfa-beta budama algoritmasını çağıran ve sonuçları yazdıran bir fonksiyon. 
# in_agac parametresi, aramayı yapmak için kullanılan ağacı belirtir. baslangic, aramaya başlanacak düğümün derinliğini belirtir. alt ve ust, değerlerin min-max aralığını belirler.

# if __name__ == "__main__": bloğu: Programın doğrudan çalıştırıldığını kontrol eder. alfabeta() fonksiyonunu çağırır ve sonuçları yazdırır.

# Algoritma, min-max ağacını dolaşarak, belirli bir derinliğe kadar en iyi hamleyi bulmaya çalışırken, alfa-beta budama kullanarak gereksiz dalları keser. 
# Bu şekilde, hesaplama maliyeti azaltılır ve daha etkili bir arama gerçekleştirilir.


agac = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
kok = 0
budama = 0

def cocuklar(dal, derinlik, alfa, beta):
    global budama
    i = 0
    for cocuk in dal:
        if isinstance(cocuk, list):
            nalfa, nbeta = cocuklar(cocuk, derinlik + 1, alfa, beta)
            if derinlik % 2 == 1:
                beta = min(nalfa, beta)
            else:
                alfa = max(nbeta, alfa)
            if alfa >= beta:
                budama += 1
                break
        else:
            if derinlik % 2 == 0 and alfa < cocuk:
                alfa = cocuk
            if derinlik % 2 == 1 and beta > cocuk:
                beta = cocuk
            if alfa >= beta:
                budama += 1
                break
        i += 1
    if derinlik == kok:
        return alfa if kok == 0 else beta
    return alfa, beta

def alfabeta(in_agac=agac, baslangıc=kok, alt=-15, ust=15):
    global budama
    result = cocuklar(in_agac, baslangıc, alt, ust)
    if isinstance(result, tuple): # Eğer sonuç tuple ise
        alfa, beta = result
        print("(alfa, beta):", alfa, beta)
        print("Sonuc:", alfa if kok == 0 else beta)
    else: # Eğer sonuç tuple değilse
        print("Sonuc:", result)
    print("Budama Sayısı:", budama)
    return result

if __name__ == "__main__":
    alfabeta()
