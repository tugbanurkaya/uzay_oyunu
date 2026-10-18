import json
from pathlib import Path
from .araclar import hamle_sayaci, en_bagli_gezegenler
from .akis import yakit_gostergesi

"""Uzay Oyununa Hoş Geldin!

Amaç: Gezegenden gezegene gidip bulmacaları çözerek kara deliğe atlamak.
Oyunu kazanmak için kredi kazanmalı, pilot bulmalı, hiperdrive almalı
ve kara deliğe atlamalısın.
Dikkat: Adımları sırasıyla uygulamalısın.
Yakıtın biterse uzayda sürüklenir ve oyunu kaybedersin!
"""

def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Envanterdeki eşyaları metin olarak döndürür."""

    envanter_icerigi = []

    if credits:
        envanter_icerigi.append("bol kredi")

    if engines:
        envanter_icerigi.append("motorlar")

    if copilot:
        envanter_icerigi.append("yetenekli bir pilot")

    if len(envanter_icerigi) == 0:
        return ""

    return "Sende: " + ", ".join(envanter_icerigi)


def hedef_menusu(hedefler: list[str]) -> str:
    """Numaralı hedef menüsünü döndürür.
    Hedefler liste şeklindedir ve metin döndürülür."""

    menu = ["\nNereye gitmek istersin?"]

    for sira, hedef in enumerate(hedefler, start=1):
        menu.append(f"[{sira}] {hedef}")

    return "\n".join(menu)

def galaksi_kur(gezegenler: list[str],baglantilar: dict[str, list[str]],baslangic: str, **kwargs: int) -> dict:
    """Gezegenleri ve bağlantılarını kullanarak galaksiyi sözlük olarak oluşturur."""

    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç '{baslangic}' gezegeni gezegenler listesi içinde yok")

    yakit = kwargs.get("yakit", 50)

    galaksi = {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit
    }

    return galaksi


def travel(galaksi: dict, envanter: dict, sayac, gosterge: int) -> str | None:
    """Oyuncunun gezegenler arasında yolculuk yapmasını sağlar.
     Geçerli hedef seçilmidiğinde yakıtı azalır ve aynı zamanda hamleleri sayar. 
    Yakıt biterse oyunu sonlandırır. 'Yakıtın bitti, uzayda sürükleniyorsun...' döndürür.
    Yakıt bitmeden oyuna devam ederken gidilen gezegenin adını döndürür."""

    planet = galaksi["konum"]
    hedefler = galaksi["baglantilar"][planet]
    
    print(envanter_metni(
        envanter["credits"],
        envanter["engines"],
        envanter["copilot"]
    ))
    
    print(hedef_menusu(hedefler))
    
    secim = input("Seçiminiz: ")

    if secim.isdigit():
        secim = int(secim)

        if 1 <= secim <= len(hedefler):
            hedef = hedefler[secim - 1]

            if hedef == "kara_delik" and not all (envanter.values()):
                print("Once tum gerekli esyalari toplamalisin!")
                return None
            try:
                galaksi["yakit"] = next(gosterge)

            except StopIteration:
                print("Yakıtın bitti, uzayda sürükleniyorsun...")
                galaksi["Oyun bitti"] = True
                return None

            hamle = sayac()

            galaksi["konum"] = hedef

            print(f"{hedef} gezegenine gidildi.")
            print(f"Kalan yakıt: {galaksi["yakit"]}")

            return hedef
            
        else:
            print("Geçersiz seçim!")
            return None
    else:
        print("Lütfen sayı giriniz!")
        return None

if __name__ == "__main__":
    with open(Path(__file__).resolve().parent / "galaksi.json", "r", encoding="utf-8") as dosya:
         veri = json.load(dosya)

    g = galaksi_kur(**veri)
    gosterge = yakit_gostergesi(g["yakit"], 5)
    g["Oyun bitti"] = False
    
    envanter = {
        "credits": False,
        "engines": False,
        "copilot": False
    }

    sayac = hamle_sayaci()
    toplam_hamle = 0

    tamamlanan_adimlar = set()
    oyun_kazanildi = False

    while g["konum"] != "kara_delik" and not g["Oyun bitti"]:
        gidilen = travel(g, envanter, sayac, gosterge)
        
        if gidilen is not None:
            toplam_hamle += 1

        if gidilen == "centauri" and "centauri" not in tamamlanan_adimlar:
            if envanter["credits"] == False:
                print("Sende kredi yok! Once kredileri toplamalısın.")
                continue
            envanter["engines"] = True
            tamamlanan_adimlar.add("centauri")
        
        elif gidilen == "sirius" and "sirius" not in tamamlanan_adimlar:
            cevap = input("Bilgi sorusu: Türkiye'nin başkenti neresidir? ")
            if cevap.capitalize() == "Ankara":
                envanter["credits"] = True
                tamamlanan_adimlar.add("sirius")
            else:
                print("Yanlış cevap, tekrar denemelisin.")

        elif gidilen == "orion" and "orion" not in tamamlanan_adimlar:
            envanter["copilot"] = True
            tamamlanan_adimlar.add("orion")

        if g["konum"] == "kara_delik" and all(envanter.values()):
            oyun_kazanildi = True
            break
    
    if oyun_kazanildi:
        print("Tebrikler! Kara deliğe atladın, oyun bitti!")
        print(f"Oyunu {toplam_hamle} hamlede bitirdin!")
        en_bagli_gezegenler(g)
