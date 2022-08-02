def person_info(ism, familiya, tyil, tjoy, email="", tel=None):
    mijoz={'ism':ism,
           'familiya':familiya,
           'tyil':tyil,
           'tjoy':tjoy,
           'email':email,
           'telefon':tel,
           'yosh':2022-tyil}
    return mijoz
print("Mijozlar haqida ma'lumotlarni kiriting: ")
mijozlra=[]
while True:
    ism=input("Ismi: ")
    familiya=input("Familiyasi: ")
    tyil=int(input("Tug'ilgan yilingiz: "))
    tjoy=input("Tug'ilgan joyingiz: ")
    email=input("Email: ")
    tel=input("Telfon raqam: ")
    mijozlar.append(person_info(ism, familiya, tyil, tjoy, email, tel ))
    javob=input("Yana odam qo'shasizmi? (ha/yo'q)")
    if javob!=ha:
        break
print("Mijozlar: ")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} "
          f"{mijoz['yosh']} da, telefon raqami:{mijoz['telefon']}, "
          f"email-{mijoz['email']}")