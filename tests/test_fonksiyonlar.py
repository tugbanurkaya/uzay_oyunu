from oyun import envanter_metni, hedef_menusu

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