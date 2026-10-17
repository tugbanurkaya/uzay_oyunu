from collections.abc import Callable
import time
from typing import Any

def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıda bir artan, kendi durumunu ``nonlocal`` ile saklayan sayaç döndürür."""

    sayac = 0

    def arttir() -> int:
        """Kapanım içindeki hamle sayısını bir artırıp yeni değeri döndürür."""

        nonlocal sayac
        sayac += 1
        return sayac

    return arttir

def en_bagli_gezegenler(galaksi: dict[str]) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sıralar."""

    gezegenler: list[str] = galaksi.get("gezegenler", [])
    baglantilar: dict[str, list[str]] = galaksi.get("baglantilar", {})
    return sorted(
        gezegenler,
        key=lambda gezegen: (-len(baglantilar.get(gezegen, [])), gezegen),
    )

def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun çalışma süresini ölçer."""

    def olc(*args: Any, **kwargs: Any) -> Any:
        """Fonksiyonu çalıştırır ve geçen süreyi gösterir."""

        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        sure = time.perf_counter() - baslangic
        print(sonuc)
        print(f"Çalışma süresi: {sure:.6f} saniye")
        return sonuc
    return olc

en_bagli_gezegenler=sure_olc(en_bagli_gezegenler)