# Muzeyga chipta narhi foydalanuvchining 
# yoshiga bog'liq: 
# 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 
# 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin 
# va chipta narhini chiqarsin. 
#Foydalanuvchi exit yoki quit deb yozganda 
#dastur to'xtasin (ikkita shartni ham tekshiring).
savol="Yoshingizni kiriting: "
ishora=True
while ishora:
    yosh=input(savol)
    if yosh=='exit' or yosh=='quit':
        ishora=False
    else:
        yosh=int(yosh)
        if yosh<7:
            narh=2000
        elif 7<=yosh<18:
            narh=3000
        elif 18<=yosh<65:
            narh=10000
        else:
            narh=0
        if narh==0:
            print("Sizga chipta bepul")
        else:
            print(f"Chipta {narh} so'm")

