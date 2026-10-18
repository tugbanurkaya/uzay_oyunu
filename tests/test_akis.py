from uzay_oyunu.akis import fibonacci, yakit_gostergesi
from itertools import islice, takewhile
import pytest

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