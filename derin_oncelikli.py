# grafı ziyaret etmeyi ve grafı derinlik öncelikli olarak dolaşmayı amaçlar. Kodun işlevlerini ve değişkenlerini açıklayalım:

# grafik: Grafik yapısını temsil eden bir sözlük. Her anahtar bir düğümü, değerler ise bu düğüme komşu olan diğer düğümleri temsil eder.

# ziyaret: Zaten ziyaret edilmiş düğümleri izleyen bir küme.

# dfs(ziyaret, grafik, dügüm): Derinlik öncelikli arama algoritmasını uygulayan bir fonksiyon. 
# ziyaret kümesi, ziyaret edilen düğümleri takip etmek için kullanılır. grafik, dolaşılacak olan grafı temsil eder. dügüm, dolaşmaya başlanacak olan düğümü belirtir.

# Fonksiyon, dügüm'ün henüz ziyaret edilmemişse, onu ziyaret eder, ekrana yazdırır ve ziyaret kümesine ekler.

# Daha sonra, grafik sözlüğündeki dügüm'e bağlı olan her komşu düğüm için DFS fonksiyonu yeniden çağrılır. 
# Bu işlem, derinlik öncelikli olarak her bir komşu düğümü ziyaret etmek için tekrarlanır.

# dfs(ziyaret, grafik, 'A'): DFS fonksiyonunu başlatır ve 'A' düğümünden başlayarak grafiği dolaşır. Başlangıç düğümü 'A' olarak belirtilmiştir.

# Bu kod, DFS algoritmasını kullanarak verilen grafı derinlik öncelikli olarak dolaşır ve ziyaret edilen düğümleri ekrana yazdırır. 
# Bu sayede, grafın tamamını veya belirli bir bölümünü dolaşmak mümkün olur.

grafik={
            'A':['B','C'],
            'B':['D','E'],
            'C':['F'],
            'D':[],
            'E':[],
            'F':[],
        }


ziyaret=set()

def dfs(ziyaret,grafik,dügüm):
    if dügüm not in ziyaret:
        print(dügüm)
        ziyaret.add(dügüm)
        for komsu in grafik[dügüm]:
            dfs(ziyaret,grafik,komsu)

dfs(ziyaret,grafik,'A')