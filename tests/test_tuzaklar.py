#def yakit_ekle(miktar: int, depo: list[int] = []) -> list[int]:
#    """Depoya yakıt ekler."""

#    depo.append(miktar)

#    return depo

def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Yakıt ekler, depo verilmemişse yeni bir liste oluşturur."""

    if depo is None:
        depo = []

    depo.append(miktar)

    return depo


def test_yakit_ekle() -> None:
    """Her çağrıda ayrı bir yakıt deposu oluştuğunu kontrol eder."""

    ilk_depo = yakit_ekle(25)
    ikinci_depo = yakit_ekle(50)

    assert ilk_depo == [25]
    assert ikinci_depo == [50]