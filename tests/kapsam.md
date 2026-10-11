# Üç kapsam örneği

## Local-Global Değişken Kapsamı

    x = 10  # Global değişken

    def fonksiyon():
        x = 20  # Local değişken
        print(x)

    fonksiyon()
    print(x)

Tahminim: 20-10 , Çıktı: 20-10
Açıklama: Fonksiyon içindeki `x = 20`, global `x = 10` değerini değiştirmez. Sadece aynı isimde yeni bir local değişken oluşturur. Eğer gerçekten fonksiyon içinden x'in değiştirilmesi isteniyorsa, `global x` olarak çağrılması gerekir.

## Enclosing - iç içe fonksiyonlar

    def dis():
        x = 10

        def ic():
            print(x)

        ic()

    dis()

Tahminim: 10, Çıktı: 10

Açıklama: `ic()` fonksiyonunda `x` bulunmadığı için Python bir üstteki `dis()` fonksiyonunun değişkenini kullanır. Eğer değişken içerden değiştirilmek istenirse, `nonlocal x` olarak çağrılmalı.

## UnboundLocalError

    x = 10

    def fonksiyon():
        print(x)
        x = 20

    fonksiyon()

Tahminim: 10, Çıktı: UnboundLocalError: cannot access local variable 'x'
where it is not associated with a value
Açıklama: Fonksiyonun içinde x = 20 ataması görüldüğü için, x değişkeni local olarak kabul edilir. print satırına gelindiğinde ise değişken henüz atanmadığından dolayı UnboundLocalError durumu oluşur.
