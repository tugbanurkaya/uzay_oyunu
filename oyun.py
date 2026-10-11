"""Uzay Oyununa Hoş Geldin!

Amaç: Gezegenden gezegene gidip bulmacaları çözerek kara deliğe atlamak.
Oyunu kazanmak için kredi kazanmalı, pilot bulmalı, hiperdrive almalı
ve kara deliğe atlamalısın.
Dikkat: Adımları sırasıyla uygulamalısın.
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

    menu = ["Nereye gitmek istersin?"]

    for sira, hedef in enumerate(hedefler, start=1):
        menu.append(f"[{sira}] {hedef}")

    return "\n".join(menu)