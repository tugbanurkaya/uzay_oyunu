# Hafta 4 - Görev 5: map, filter, reduce ve partial
import json, time
from pathlib import Path
from functools import reduce, partial
from typing import Generator

veri_yolu=Path(__file__).resolve().parent/"galaksi.json"
with open (veri_yolu,"r",encoding="utf-8") as dosya:
    galaksi=json.load(dosya)

def gezegen_adlari_buyuk_harf_map() -> list[str]:
    """map fonksiyonu ile gezegen adlarını büyük harflerle liste olarak döndürür."""
    return list(map(str.upper,galaksi["gezegenler"]))

def gezegen_adlari_buyuk_harf_liste() -> list[str]:
    """liste üreteci ile gezegen adlarını büyük harflarle liste olarak döndürür."""
    return [g.upper() for g in galaksi["gezegenler"]]

def baglanti_sayisi_filter() -> list[str]:
    """filter fonksiyonu ile bağlantı sayısı 2 ve daha fazla olan gezegenleri liste olarak yazdırır."""
    return list(filter(lambda g: len(galaksi["baglantilar"][g])>=2, galaksi["gezegenler"]))

def baglanti_sayisi_liste() -> list[str]:
    """liste üreteci ile bağlantı sayısı 2 ve daha fazla olan gezegenleri yazdırır."""
    return [g for g in galaksi["gezegenler"] 
            if len(galaksi["baglantilar"][g]) >= 2]

def toplam_baglanti_sayisi_reduce() -> int:
    """Gezegenlerin toplam bağlantı sayısını reduce kullanarak hesaplar."""
    return reduce( lambda toplam, g: toplam + len(galaksi["baglantilar"][g]), galaksi["gezegenler"], 0)

def toplam_baglanti_sayisi_sum() -> int:
    """Gezegenlerin toplam bağlantı sayısını sum ile hesaplar."""
    return sum(len(galaksi["baglantilar"][g]) for g in galaksi["gezegenler"])

def yolculuk(gezegen: str, hiz: int) -> str:
    """functools.partial ile yolculuk fonksiyonunda hızı sabit olan hizli_yolculuk adında bir fonksiyon yazdırır."""
    return f"{gezegen} gezegenine {hiz} hızla gidiliyor."

hizli_yolculuk =partial(yolculuk, hiz=3)

if __name__ == "__main__":
    print(gezegen_adlari_buyuk_harf_map())
    print(gezegen_adlari_buyuk_harf_liste())
    print(baglanti_sayisi_filter())
    print(baglanti_sayisi_liste())
    print(toplam_baglanti_sayisi_reduce())
    print(toplam_baglanti_sayisi_sum())
    print(hizli_yolculuk("centauri"))

# Python'da liste üreteci, sum fonksiyonu daha okunaklıdır. Karmaşık ifadelere gerek duymadan tek bir satırda kolaylıkla yazılıp istenilen değeri döndürür.

# Hafta 4 - Bonus : Tik Tak Zamanlayıcısı

def zamanlayici(aralik: float) -> Generator[bool, None, None]:
    """Kaynak kitabın ticker örneği: üreteç, iki çağrı arasında sonr değişkenini hatırlar.
    """
    son=time.time()
    while True:
        simdi=time.time()
        if simdi-son>=aralik:
            son = simdi
            yield True
        else:
            yield False

if __name__ == "__main__":
    tik = zamanlayici(2.0)
    tak = zamanlayici(5.0)

    baslangic = time.time()

    while time.time() - baslangic < 10:
        if next(tik):
            print("tik")

        if next(tak):
            print("tak")

        if time.time() - baslangic >= 10:
            break

# Programda zamanlayici() üreteci kullanılarak 10 saniye boyunca geçen süreyi kontrol ettiği için meşgul bekleme olarak adlandırılır.
# Meşgul bekleme while True döngüsü içinde koşulun gerçekleşip gerçekleşmediğini kontrol eder.
# time.sleep() ise belirtilen süre içerisinde yapılacak işlemleri durdurur ve bu sayede işlemcinin gereksiz çalışmasına engel olur.