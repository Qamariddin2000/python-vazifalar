restoran_menu={
    'osh':20000,
    "non":4000,
    'somsa':6000,
    "shashlik":10000,
    'norin':15000,
    'choy':3000,
    "sho'rva":9000,
    'bishteks':13000,
    'xonim':12000,
    'manti':15000
}
print("3 ta taom buyurtma bering. ")
buyurtmalar=[]
for a in range(3):
    taom=input(f"{a+1}-taom: ").lower()
    buyurtmalar.append(taom)
for taom in buyurtmalar:
    if taom in restoran_menu.keys():
        print(f"{taom.title()} {restoran_menu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q")