from uzay_oyunu.akis import fibonacci
from itertools import islice, takewhile

#  GÖREV 1: Fibonacci Üreteci Testleri

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