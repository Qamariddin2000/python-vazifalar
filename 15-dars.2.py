davlatlar_poytaxti={
    'AQSh':'Washinton D.C',
    'Italita':'Rim',
    'Malayziya':"Kuala-Lumpur",
    "O'zbekiston":'Toshkent',
    "Qirg'iziston":"Bishkek",
    "Qozog'iston":'Nursulton',
    'Rossiya':'Moskva',
    'Singapur':'Singapur',
    'Tojikiston':'Dushanbe'
}
davlat=input('Qaysi davlatning potaxtini bilishni istaysiz? ')
poytaxt=davlatlar_poytaxti.get(davlat)
if not poytaxt==None:
    print(f"{davlat}ning poytaxti {poytaxt}")
else:
    print("Kechirasiz, bida bu haqida ma'lumot yo'q")