from typing import Iterator
from itertools import islice, takewhile

# Hafta 4 - Görev 1: Fibonacci Üreteci

def fibonacci()-> Iterator[int] :
    """Sonsuz fibonacci dizisi üreten fonksiyon. Fibonacci sayıları 0 ve 1 ile başlar.
    yield ile sayıları sırasıyla kendinden önceki iki sayının toplamı şeklinde üretir. """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # next() ile ilk ilk 3 değeri bulma
    g = fibonacci()
    ilk_uc_deger =(next(g), next(g), next(g)) 
    print("next() ile fibonaccinin ilk 3 değeri: ", ilk_uc_deger)

    # itertools.islice() ile ilk 12 değeri bulma
    ilk_12_degeri = (list(islice(fibonacci(), 12)))
    print("\nislice() ile fibonaccinin ilk 12 değeri: ", ilk_12_degeri)

    # itertools.takewhile() ile 100'den küçük değerleri bulma   
    yuzden_kucuk_degerler = (list(takewhile(lambda x: x < 100, fibonacci())))
    print("\ntakewhile() ile fibonaccinin 100'den küçük değerleri: ", yuzden_kucuk_degerler)