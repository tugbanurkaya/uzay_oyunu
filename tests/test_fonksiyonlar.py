import pytest
from uzay_oyunu.oyun import envanter_metni, hedef_menusu, galaksi_kur
from uzay_oyunu.kayit import gorev_kaydi 

# Görev 1 - Sabit Fonksiyon Testleri

def test_envanter_icerigi_dolu() -> None:
    """Envanterde eşya varsa "Sende:..." diye olan metni döndürür.
    Envanterde bol kredi ve yetenekli bir pilot var; hiperdrive yok."""
    assert envanter_metni(True, False, True) == "Sende: bol kredi, yetenekli bir pilot"

def test_envanter_icerigi_bos() -> None:
    """Envanterde eşya yoksa boş metin döndürür."""
    assert envanter_metni(False, False, False) == ""

def test_hedef_menusu() -> None:
    """Gezegenlerin numaralandırılmış gösterimini kontrol eder."""
    assert hedef_menusu(["centauri", "sirius"]) == (
        "Nereye gitmek istersin?\n"
        "[1] centauri\n"
        "[2] sirius"
    )

# Görev 2 - Esnek Parametre Testleri

istenen = """[YÜKSEK] Kara deliğe atla
  1. Kredi kazan
  2. Pilot bul
  3. Hiperdrive al
  sorumlu: Ayşe"""

def test_gorev_kaydi() -> None:
    """Görev kaydının doğru olup olmadığını kontrol eder."""
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    sonuc = gorev_kaydi("Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler)
    assert sonuc == istenen

def test_normal_cagri() -> None:
    """Görev kaydını doğrudan çağırma yöntemi ile kontrol eder."""

    sonuc = gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al",
        oncelik="yüksek", sorumlu="Ayşe")
    assert sonuc == istenen

def test_liste_ve_sozluk_ile_cagri() -> None:
    """Liste ve sözlük kullanarak görev kaydını kontrol eder."""

    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"oncelik": "yüksek", "sorumlu": "Ayşe"}
    assert gorev_kaydi("Kara deliğe atla", *adimlar, **ekler) == istenen

def test_varsayilan_oncelik_normal() -> None:
    """Öncelik belirtilmediğinde varsayılan olarak kontrol eder."""

    assert gorev_kaydi("Yakıt al") == "[NORMAL] Yakıt al"


# Görev 3 - Galaksiyi Kurma Testleri

def test_galaksi_kur() -> None:
    """Galaksinin başlangıç gezegen ve bağlantı bilgilerini kontrol eder."""

    gezegenler = ["dünya", "mars"]
    baglantilar = {"dünya": ["mars"], "mars": ["dünya"]}

    galaksi=galaksi_kur(gezegenler,baglantilar,"dünya",yakit=100)
    assert galaksi["konum"] == "dünya"
    assert galaksi["yakit"] == 100
    assert galaksi["baglantilar"] == baglantilar

def test_varsayilan_yakit() -> None:
    """Yakıt verilmezse varsayılan değeri (yakit = 50) kontrol eder."""

    galaksi = galaksi_kur(["mars"], {"mars": []}, "mars" )
    assert galaksi["yakit"] == 50

def test_hatali_baslangic() -> None:
    """Listede olmayan başlangıç gezegeninde 'ValueError' hatası fırlatır."""

    with pytest.raises(ValueError):
        galaksi_kur(["mars"], {"mars": []}, "dünya")