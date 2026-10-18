# Hafta 4 - Görev 5: map, filter, reduce ve partial
import json
from pathlib import Path
from functools import reduce

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

if __name__ == "__main__":
    print(gezegen_adlari_buyuk_harf_map())
    print(gezegen_adlari_buyuk_harf_liste())
    print(baglanti_sayisi_filter())
    print(baglanti_sayisi_liste())
    print(toplam_baglanti_sayisi_reduce())
    print(toplam_baglanti_sayisi_sum())