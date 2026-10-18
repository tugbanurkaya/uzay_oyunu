from typing import Iterator, Iterable, Callable
from itertools import islice, takewhile
from functools import lru_cache

# Hafta 4 - Görev 1: Fibonacci Üreteci

def fibonacci()-> Iterator[int] :
    """Sonsuz fibonacci dizisi üreten fonksiyon. Fibonacci sayıları 0 ve 1 ile başlar.
    yield ile sayıları sırasıyla kendinden önceki iki sayının toplamı şeklinde üretir. """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # next() ile ilk ilk 3 değeri bulma
    g = fibonacci()
    ilk_uc_deger =(next(g), next(g), next(g)) 
    print("next() ile fibonaccinin ilk 3 değeri: ", ilk_uc_deger)

    # itertools.islice() ile ilk 12 değeri bulma
    ilk_12_degeri = (list(islice(fibonacci(), 12)))
    print("\nislice() ile fibonaccinin ilk 12 değeri: ", ilk_12_degeri)

    # itertools.takewhile() ile 100'den küçük değerleri bulma   
    yuzden_kucuk_degerler = (list(takewhile(lambda x: x < 100, fibonacci())))
    print("\ntakewhile() ile fibonaccinin 100'den küçük değerleri: ", yuzden_kucuk_degerler)

# Hafta 4 - Görev 2: Yakıt Göstergesi

def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]: 
    """Her next() çağrısında yakıtı tüketim kadar azaltıp kalan yakıtı yield üretir ve yakıt 0’a inince durur."""
    if tuketim <= 0:
        raise ValueError("Tüketim pozitif olmalı")
    while yakit > 0 :
        yakit = max(yakit - tuketim, 0)
        yield yakit
    return 

# Hafta 4 - Görev 3: Seyir Defteri Boru Hattı

def satirlari_oku(yol: str) -> Iterator[str]:
    """1. Üreteç dosyadaki boş ve yorum satırlarını atlayarak diğer satırları yield ile üretir.
    Hiçbir aşamada tüm dosyayı bir listeye okumaz (tembel değerlendirme)."""
    with open(yol, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            düzgün_satir = satir.strip()
            if düzgün_satir and not düzgün_satir.startswith("#"):
                yield düzgün_satir

def ayristir(satirlar: Iterable[str]) -> Iterator[tuple[str, str, int]]:
    """2. üreteç her satırdan (kaynak, hedef, yakit) demeti üretir.
    Örneğin 'dünya -> sirius 12' satırını ("dünya","sirius",12) demetine dönüştürür."""
    for satir in satirlar:
        rota, yakit=satir.rsplit(" ", 1)
        kaynak, hedef = rota.split(" -> ")
        yield kaynak, hedef, int(yakit)

def uzun_yolculuklar(kayitlar: Iterable[tuple[str, str, int]], esik: int) -> Iterator[tuple[str, str, int]]:
    """3. üreteç yakıtı eşikten büyük olan kayıtları süzen üreteç."""
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit

# Hafta 4 - Görev 4: Önbellekli Rota Sayacı

def rota_sayisi_onbelleksiz(baglantilar: dict[str,list[str]], gezegen: str, adim: int) -> int:
    """Önbellek kullanmadan her çağrıda bağlantılı gezegenlerdeki rota sayısını hesaplar."""
    if adim == 0:
        return 1
    return sum(rota_sayisi_onbelleksiz(baglantilar, h, adim-1) for h in baglantilar[gezegen])

def rota_sayaci(baglantilar: dict[str, list[str]]) -> Callable[[str, int], int]:
    """Gezegen bağlantılarını kullanarak olduğu adımdaki rota sayısını hesaplayan önbellekli fonksiyonu @lru_cache kullanarak üretir."""
    @lru_cache(maxsize=None)

    def rota_sayisi(gezegen:str, adim: int) -> int: 
        """Olduğu gezegenden tam adım yolculuk yapabildiği gezegenlere olan rota sayısını döndürür."""
        if adim == 0:
            return 1
        return sum(rota_sayisi(h, adim-1) for h in baglantilar[gezegen])

    return rota_sayisi