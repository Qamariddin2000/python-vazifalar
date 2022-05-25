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
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
