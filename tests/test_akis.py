from uzay_oyunu.akis import fibonacci, yakit_gostergesi, satirlari_oku, ayristir, uzun_yolculuklar
from itertools import islice, takewhile
import pytest , time , json
from pathlib import Path
from uzay_oyunu.akis import rota_sayisi_onbelleksiz, rota_sayaci

# Hafta 4 - GÖREV 1: Fibonacci Üreteci Testleri

def test_fibonacci_next() -> None:
    """Fibonacci dizisinin ilk 3 değerini next() ile kontrol eder."""
    g= fibonacci()
    assert(next(g),next(g), next(g)) == (0, 1, 1)

def test_fibonacci_ilk_12() -> None:
    """Fibonacci dizisinin ilk 12 değerini islice() kullanarak kontrol eder."""
    test_12= list(islice(fibonacci(),12))
    assert test_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_yuzden_kucuk_degerler() -> None:
    """Fibonacci dizisinin 100'den küçük değerlerini takewhile() ile kontrol eder."""
    test_deger = list(takewhile(lambda x: x < 100, fibonacci()))
    assert test_deger == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def test_fibonacci_tek_kullanimlik() -> None:
    """Fibonaccide bir üretecin tek kullanımlık olduğu test eder. 
    İkinci çağrıda kaldığı yerden devam eder, başa sarmaz.""" 
    g= fibonacci()

    birinci_deneme=list(islice(g,6))
    ikinci_deneme= list(islice(g,6))

    assert birinci_deneme == [0,1,1,2,3,5]
    assert ikinci_deneme == [8,13,21,34,55,89]
    assert birinci_deneme != ikinci_deneme

# Hafta 4 - Görev 2: Yakıt Göstergesi Testleri 

def test_yakit_gostergesi():
    """Verilen örnek list(yakit_gostergesi(100,30)) girdiyi ve [70,40,10,0] çıktıyı doğrular."""
    assert list(yakit_gostergesi(100,30)) == [70,40,10,0]

def test_tuketim_sifir_hatasi():
    """Tüketim sıfır olunca"""
    with pytest.raises(ValueError):
        next(yakit_gostergesi(100, 0))   

def test_yakit_bitmesi():
    """Yakıt bitince StopIteration döndürdüğünü doğrular."""
    g = yakit_gostergesi(40, 20)

    assert next(g) == 20
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)

# Hafta 4 - Görev 3: Seyir Defteri Boru Hattı Testleri

def test_satirlari_oku() -> None:
    """Seyir defterinde bulunan boş satırların ve yorum satırlarının atlandığını kontrol eder."""
    okuma = list(satirlari_oku("veri/seyir.txt"))
    assert len(okuma)==6
    assert okuma[0] == "dünya -> sirius 12"
    assert "# bakım molası" not in okuma

def test_ayristir_toplam_yakit() -> None:
    """Verilen örnekteki ayristir(satirlari_oku()) ile yakıt toplamının 88 olduğunu doğrular."""
    assert sum(y for _, _, y in ayristir(satirlari_oku("veri/seyir.txt"))) == 88

def test_uzun_yolculuklar() -> None:
    """Pdf'de verilen örnekteki ['sirius', 'centauri', 'orion', 'kara_delik'] çıktısını doğrular."""
    kayitlar = ayristir(satirlari_oku("veri/seyir.txt"))
    assert  [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)] == ["sirius", "centauri", "orion", "kara_delik"] 

# Hafta 4 - Görev 4: Rota Sayacı Testleri

veri_yolu = Path(__file__).resolve().parents[1]/"uzay_oyunu"/"galaksi.json"
with open(veri_yolu,"r",encoding="utf-8")as dosya:
    galaksi=json.load(dosya)

def test_onbelleksiz_rota_sayaci() -> None:
    """Önbelleksiz sürümün 20 adım için kaç saniye sürdüğünü hesaplar."""
    rota_sayisi = rota_sayisi_onbelleksiz(galaksi["baglantilar"],"dünya", 20)

    assert rota_sayisi == 4315343
    print("Önbelleksiz rota sayısı:", rota_sayisi)

def test_onbellekli_rota_sayaci() -> None:
    """önbellekli sürümün 20 adım için kaç saniye sürdüğünü hesaplar."""
    sayac=rota_sayaci(galaksi["baglantilar"])
    
    assert sayac("dünya", 3) == 9
    assert sayac("dünya", 10) == 2185
    assert sayac("dünya", 40) == 16832258606399
    assert sayac("dünya", 20) == 4315343
    print("Önbellekli rota sayısı:",sayac("dünya",20))

def test_sure_karsilastirmasi() -> None:
    """Önbellekli ve önbelleksiz rota sayacını 20 adım için kaç saniye sürdüğünü hesaplayarak karşılaştırır."""

    baslangic = time.perf_counter()
    onbelleksiz = rota_sayisi_onbelleksiz(galaksi["baglantilar"], "dünya", 20)
    onbelleksiz_sure = time.perf_counter() - baslangic

    sayac = rota_sayaci(galaksi["baglantilar"])

    baslangic = time.perf_counter()
    onbellekli = sayac("dünya", 20)
    onbellekli_sure = time.perf_counter() - baslangic

    assert onbelleksiz == onbellekli == 4315343

    karsilastirma = onbelleksiz_sure / onbellekli_sure

    print(f"Önbelleksiz süre: {onbelleksiz_sure:.7f} saniye")
    print(f"Önbellekli süre: {onbellekli_sure:.7f} saniye")
    print(f"Önbellekli hesaplama {karsilastirma:.0f} kat daha hızlıdır.")
    print("Cache:", sayac.cache_info())
