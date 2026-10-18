# Hafta 4 - Görev 5: map, filter, reduce ve partial testleri

from uzay_oyunu.istatistik import gezegen_adlari_buyuk_harf_map, gezegen_adlari_buyuk_harf_liste
from uzay_oyunu.istatistik import baglanti_sayisi_filter, baglanti_sayisi_liste
from uzay_oyunu.istatistik import toplam_baglanti_sayisi_reduce, toplam_baglanti_sayisi_sum
from uzay_oyunu.istatistik import hizli_yolculuk

def test_buyuk_harf() -> None:
    """Pdf'deki gibi gezegen isimleinin ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"] olup olmadığını kontrol eder."""

    ornek_cikti=["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]

    assert gezegen_adlari_buyuk_harf_map() == ornek_cikti
    assert gezegen_adlari_buyuk_harf_liste() == ornek_cikti

def test_baglanti_sayisi() -> None:
    """En az iki bağlantısı olan gezegenleri kontrol eder."""
    ornek_cikti = ["dünya", "centauri", "sirius", "orion"]

    assert baglanti_sayisi_filter() == ornek_cikti
    assert baglanti_sayisi_liste() == ornek_cikti

def test_toplam_baglanti_sayisi() -> None:
    """Toplam bağlantı sayısının 10 olup olmadığını kontrol eder."""
    assert toplam_baglanti_sayisi_reduce() == 10
    assert toplam_baglanti_sayisi_sum() == 10

def test_hizli_yolculuk() -> None:
    """hizlü_yolculuk ta hızın sabit 3 olarak sabitlendiğini kontrol eder."""
    assert hizli_yolculuk("centauri") == "centauri gezegenine 3 hızla gidiliyor." 