e_bozor={}
while True:
    mahsulot=input("Mahsulotni kiriting: ")
    narh=input(f"{mahsulot.title()}ning narhini kiriting: ")
    e_bozor[mahsulot]=int(narh)
    javob=input("Yana mahsulot qo'shasizmi? (ha/yo'q) ")
    if javob!='ha':
        break