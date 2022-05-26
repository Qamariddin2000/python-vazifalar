davlatlar_poytaxti={
    'AQSH':'Washinton D.C',
    'Italita':'Rim',
    'Malayziya':"Kuala-Lumpur",
    "O'zbekiston":'Toshkent',
    "Qirg'iziston":"Bishkek",
    "Qozog'iston":'Nursulton',
    'Rossiya':'Moskva',
    'Singapur':'Singapur',
    'Tojikiston':'Dushanbe'
}
print("Dunyo davlatlari: ")
for davlat in sorted(davlatlar_poytaxti.keys()):
    print(davlat)
print("Davlatlarning poytaxtlari: ")
for poytaxt in sorted(davlatlar_poytaxti.values()):
    print(poytaxt)