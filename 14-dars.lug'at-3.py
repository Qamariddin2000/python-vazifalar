python_izohli_lugati={
    'integer':'butun son',
    'float':"o'nlik son",
    'string':'matn',
    'list':"ro'yxat",
    'tuple':"o'zgarmas qiymat",
    'if,else':'shartlarni tekshirish',
    'for':'takrorlash operatori'
    }
kalit=input("Kalit so'z kiriting: ")
print(python_izohli_lugati.get(kalit,"bunday so'z mavjud emas"))
