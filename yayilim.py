# Bu Python kodu, genişlik öncelikli arama (BFS - Breadth First Search) algoritmasını kullanarak bir grafı ziyaret etmeyi ve 
# grafı genişlik öncelikli olarak dolaşmayı amaçlamaktadır. Kodun işlevlerini ve değişkenlerini açıklayalım:

# grafik: Grafik yapısını temsil eden bir sözlük. Her anahtar bir düğümü, değerler ise bu düğüme komşu olan diğer düğümleri temsil eder.

# ziyaret: Ziyaret edilen düğümlerin listesi. Bu liste, daha önce ziyaret edilmiş olan düğümleri izlemek için kullanılır.

# yıgın: BFS algoritmasında kullanılan bir yığındır. Bu yığın, henüz ziyaret edilmemiş olan düğümleri tutar. Başlangıçta, sadece başlangıç düğümü dügüm yığına eklenir.

# bfs(ziyaret, grafik, dügüm): BFS algoritmasını uygulayan bir fonksiyon. ziyaret listesi, ziyaret edilen düğümleri takip etmek için kullanılır. 
# grafik, dolaşılacak olan grafı temsil eder. dügüm, dolaşmaya başlanacak olan düğümü belirtir.

# Fonksiyon, başlangıç düğümünü ziyaret eder ve ziyaret listesine ekler.
# Ardından, başlangıç düğümünü yıgın yığına ekleriz.
# yıgın yığı boşaltıldığı sürece (tüm düğümler ziyaret edilene kadar) bir döngü çalışır. Her adımda, yıgın'ın en üstündeki düğüm çıkarılır (pop) ve ekrana yazdırılır.
# Daha sonra, çıkarılan düğümün komşuları grafik sözlüğünden alınır. Henüz ziyaret edilmemiş olan her komşu düğüm ziyaret listesine eklenir ve yıgın yığına eklenir.
# Bu kod, BFS algoritmasını kullanarak verilen grafı genişlik öncelikli olarak dolaşır ve ziyaret edilen düğümleri ekrana yazdırır. 
# Bu şekilde, grafiğin genişlik öncelikli dolaşımını gerçekleştirmiş oluruz.



grafik={
            'A':['B','C'],
            'B':['D','E'],
            'C':['F'],
            'D':[],
            'E':[],
            'F':[],
        }

ziyaret=[]
yıgın=[]


def bfs(ziyaret,grafik,dügüm):
    ziyaret.append(dügüm)
    yıgın.append(dügüm)

    while yıgın:
        s=yıgın.pop(0)
        print(s,end=" ")

        for komsu in grafik[s]:
            if komsu not in ziyaret:
                yıgın.append(komsu)


bfs(ziyaret,grafik,'A')