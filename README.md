# İleri Python Programlama - Uzay Oyunu Projesi

---

**Kurum:** İstanbul Nişantaşı Üniversitesi <br>
**Ders:** Python ile Programlama <br>
**Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç <br>
**Dönem:** 2026 - 2027 Güz <br>
**Bölüm:** Veri Bilimi ve Analitiği <br>
**Öğrenci Adı Soyadı:** Tuğba Nur Kaya <br>
**Öğrenci Numarası:** 20253005004

---


# Uzay Oyunu

**Uzay Oyunu**, Python ile geliştirilmiş, terminal üzerinden oynanan bir gezegenler arası gezip bulmacaları çözen bir oyundur. Oyuncu başlangıç gezegeni olan Dünya'dan yola çıkar, farklı gezegenlerde görevleri tamamlar ve bağlantıları takip ederek kara deliğe ulaşmaya çalışır.

Gezegenler arasındaki yolculuklar `galaksi.json` dosyasında tanımlanan bağlantılara göre yapılır. Her gezegene doğrudan gidilemez. Örneğin Dünya'dan sonra Centauri ve Sirius gezegenine gidebilir.

Oyunu bitirmek için yakıt bitmeden önce kredi kazanmalı, yardımcı pilotu bulmalı ve hiperdrive almalı bu adımları tamamladıktan sonra kara deliğe ulaşmalı. Yakıt biterse, uzayda sürüklenir ve oyun kaybedilir.

---

\***\*Programın Çalışması İçin Gereken Komutlar\*\***

---

**Oyunu başlatmak için:**

```bash

python -m uzay_oyunu.oyun

uv run python -m uzay_oyunu.oyun

```

**Oyunu başlatmak için:**

```bash

python -m uzay_oyunu.oyun

uv run python -m uzay_oyunu.oyun

```

**Tüm testleri çalıştırmak için:**

```bash

python -m pytest

uv run pytest

```

**Fonksiyon testlerini çalıştırmak için:**

```bash

python -m pytest tests/test_fonksiyonlar.py -v

uv run pytest tests/test_fonksiyonlar.py -v

```

**Tuzak testlerini çalıştırmak için:**

```bash

python -m pytest tests/test_tuzaklar.py -v

uv run pytest tests/test_tuzaklar.py -v

```

**Akış testlerini çalıştırmak için:**

```bash

python -m pytest tests/test_akis.py -v

uv run pytest tests/test_akis.py -v

```

**İstatistik testlerini çalıştırmak için:**

```bash

python -m pytest tests/test_istatistik.py -v

uv run pytest tests/test_istatistik.py -v

```

**Rota sürelerini görüntülemek için:**

```bash

python -m pytest tests/test_akis.py -v -s

uv run pytest tests/test_akis.py -v -s

```

## Hafta 3 – Fonksiyonlar Derinlemesine

Uzay oyununun `travel()` fonksiyonu küçük ve test edilebilir fonksiyonlara bölündü ve oyun haritası `galaksi.json` adındaki veri dosyasına taşındı.

| Görev                              | Açıklama                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 – Saf fonksiyonlar               | `uzay_oyunu/oyun.py` adlı dosya oluşturulup içerisine `envanter_metni()` ve `hedef_menusu()` adlı iki fonksiyon oluşturuldu. Fonksiyonlar print etmez, metni döndürür. Testler fonksiyonlardan önce `tests/test_fonksiyonlar.py` dosyasına yazıldı.                                                                                                                                                                                              |
| 2 – Esnek parametreler             | `uzay_oyunu/kayit.py` modülüne `gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler)` fonksiyonu yazıldı. `oncelik` yalnızca adıyla verilebilir. `main` bloğunda doğrudan çağrı ile `*liste` / `**sözlük` açarak çağrı gösterilir.                                                                                                                                                                                                           |
| 3 – Galaksiyi veri dosyasından kur | Gezegenler, bağlantılar ve başlangıç bilgileri `uzay_oyunu/galaksi.json` dosyasında tutuldu. `oyun.py` içerisinde `galaksi_kur(gezegenler, baglantilar, baslangic, **kwargs)` fonksiyonu oluşturuldu. Başlangıç gezegeni listede bulunmazsa `ValueError` hatası fırlatır. Yakıt belirtilmediğinde ise varsayılan değer 50 olarak ayarlanır. `travel()` fonksiyonunda gidilebilecek gezegenler `galaksi["baglantilar"][planet]` üzerinden alınır. |
| 4 – Tuzaklar ve kapsam             | `tests/tuzaklar.py` dosyasında `depo=[]` hatası gösterildi ve `None` kalıbıyla düzeltildi. Dersteki LEGB kapsam kuralları (tahmin, gerçek çıktı) ve `UnboundLocalError` örneklerle açıklandı.                                                                                                                                                                                                                                                    |
| 5 – Closure ve lambda              | `uzay_oyunu/araclar.py` modülünde `hamle_sayaci()` fonksiyonu `nonlocal` kullanılarak oluşturuldu. `en_bagli_gezegenler(galaksi)` fonksiyonu, `sorted()` ve `key=lambda` kullanarak gezegenleri bağlantı sayısına göre azalan, eşitlik durumunda alfabetik olarak sıralar.                                                                                                                                                                       |
| Bonus – Süre ölçümü                | `sure_olc(fonksiyon)` fonksiyonu yazıldı. `*args` ve `**kwargs` ile fonksiyonu çağırır, `time.perf_counter()` kullanarak çalışma süresini ölçen sarmalayıcı dööndürür ve ekrana yazdırır.                                                                                                                                                                                                                                                        |

`global` anahtar kelimesi hiçbir görevde kullanılmamıştır.

---

## Hafta 4 – Üreteçler ve functools

Kodlar `uzay_oyunu/akis.py` ve `uzay_oyunu/istatistik.py` modüllerinde oluşturulup, `tests/test_akis.py` ve `tests/test_istatistik.py` dosyalarında test edilmiştir.

| Görev                              | Açıklama                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 – Fibonacci üreteci              | `uzay_oyunu/akis.py`dosyasında sonsuz bir`fibonacci()` üreteci oluşturuldu. Değerler üç farklı yolla alındı: `next()` (ilk 3), `itertools.islice` (ilk 12), `itertools.takewhile` (100'den küçükler). `tests/test_akis.py` dosyasında üretecin tek kullanımlık olduğu ve diğer gösterimler test edildi.                                                                |
| 2 – Yakıt göstergesi               | `uzay_oyunu/akis.py` dosyasında `yakit_gostergesi(yakit, tuketim)` üreteci oluşturuldu. Her `next()` çağrısında yakıtı tüketim kadar azaltıp kalan yakıtı üretir, 0'a inince durur. `uzay_oyunu/oyun.py` dosyasındaki `travel()` her yolculukta bir değer çeker, `StopIteration` yakalanınca oyuncu "Yakıtın bitti, uzayda sürükleniyorsun…" mesajıyla oyunu kaybeder. |
| 3 – Seyir defteri boru hattı       | `veri/seyir.txt` dosyası oluşturuldu ve bu dosya üç üreteçle işlenir: `satirlari_oku()`, `ayristir()`, `uzun_yolculuklar()`. Hiçbir aşama tüm dosyayı listeye okumaz.                                                                                                                                                                                                  |
| 4 – Önbellekli rota sayacı         | `rota_sayaci(baglantilar)` içinde `@lru_cache` ile süslenmiş `rota_sayisi(gezegen, adim)` tanımlanıp döndürülür. `time.perf_counter()` kullanarak süreler ölçülür ve karşılaştırmalar yapılıp `README.md`ye yazılır.                                                                                                                                                   |
| 5 – map, filter, reduce ve partial | `istatistik.py` modülünde galaksi verisi üzerinde aynı üç soru iki yolla yanıtlandı: map/filter/reduce ve liste üreteci/`sum`. `functools.partial` ile `yolculuk` fonksiyonundan `hiz=3` sabit `hizli_yolculuk` oluşturuldu.                                                                                                                                           |
| Bonus                              | Kaynak kitaptaki `zamanlayici(aralik)` üreteci ile 10 saniye boyunca her 2 saniyede "tik", her 5 saniyede "tak" yazılır. meşgul bekleme ve `time.sleep` farkı açıklandı.                                                                                                                                                                                               |

### Görev 4 – Önbellekli / Önbelleksiz Rota Ölçümü Değerlendirmesi

| Sürüm                                       | Süre               | Rota Sayısı |
| ------------------------------------------- | ------------------ | ----------- |
| Önbelleksiz (`rota_sayisi_onbelleksiz`)     | ≈ 1.6343337 saniye | 4315343     |
| `@lru_cache` ile önbellekli (`rota_sayaci`) | ≈ 0.0000524 saniye | 4315343     |

Önbellekli rota hesaplaması yaklaşık 31190 kat daha hızlıdır.
Önbellekli ve Önbelleksiz sürümlerin dünya başlangıç gezegeni iken ve 20 adım için toplam rota sayıları birbirine eşit çıkmıştır.

---

**Önbellek Bilgisi**

```
CacheInfo(hits=47, misses=51, maxsize=None, currsize=51)
```
