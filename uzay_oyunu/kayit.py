def gorev_kaydi(baslik:str, *adimlar: str, oncelik:str = "normal", **ekler:str) -> str:
    """Görev bilgilerini metin olarak döndürür.
    baslik: Görevin adı
    *adimlar: "İstenilen sayıda adım olabilir.
    oncelik: Yalnızca adıyla verilebilir.istenilen oncelik="yüksek", varsayılan ise "normal" kabul edilir.
    **ekler: Göreve ait ek bilgiler.
    """
    istenen = f"[{oncelik.upper()}] {baslik}"

    for sayi, adim in enumerate(adimlar, start=1):
        istenen += f"\n  {sayi}. {adim}"

    for anahtar,deger in ekler.items():
        istenen+=f"\n  {anahtar}: {deger}"

    return istenen

if __name__ == "__main__":
    
    # 1.Normal (doğrudan argümanları yazarak) çağrı

    kayit1=gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik = "yüksek",
        sorumlu= "Ayşe",
    )

    print("--Normal Çağrı-- \n\n", kayit1)

    # 2. Bir listeyi argümanlara açarak (*) ve bir sözlüğü adlı argümanlara açarak (**) çağırmak
    baslik="Kara deliğe atla"
    adimlar=["Kredi kazan","Pilot bul", "Hiperdrive al"]
    ekler={"sorumlu": "Ayşe"}

    kayit2 = gorev_kaydi(baslik, *adimlar, oncelik="yüksek", **ekler,)
    print("\n--2. *args **kwarg ile Çağrı--\n\n", kayit2)