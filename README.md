# Uzay Oyunu

**Uzay Oyunu**, Python ile geliştirilmiş, terminal üzerinden oynanan bir gezegenler arası gezip bulmacaları çözen bir oyundur. Oyuncu başlangıç gezegeni olan Dünya'dan yola çıkar, farklı gezegenlerde görevleri tamamlar ve bağlantıları takip ederek kara deliğe ulaşmaya çalışır.

Gezegenler arasındaki yolculuklar `galaksi.json` dosyasında tanımlanan bağlantılara göre yapılır. Her gezegene doğrudan gidilemez. Örneğin Dünya'dan sonra Centauri ve Sirius gezegenine gidebilir.

Oyunu bitirmek için önce kredi kazanmalı, yardımcı pilotu bulmalı ve hiperdrive almalı bu adımları tamamladıktan sonra kara deliğe ulaşmalı.

**Oyunu başlatmak için:**

```bash

python -m uzay_oyunu.oyun

uv run python -m uzay_oyunu.oyun

```

**Tüm testleri çalıştırmak için:**

```bash

python -m pytest

uv run python -m pytest

```

**Yalnızca fonksiyon testlerini çalıştırmak için:**

```bash

python -m pytest tests/test_fonksiyonlar.py -v

uv run python -m pytest tests/test_fonksiyonlar.py -v

```
