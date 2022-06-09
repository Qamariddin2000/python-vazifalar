davlatlar={
    "o'zbekiston":{
        'poytaxt':"toshkent",
        'maydon':448978,
        'aholi':33000000,
        'pul birligi':"so'm"
    },
    'rossiya':{
        'poytaxt':"moskva",
        'maydon':17098246,
        'aholi':144000000,
        'pul birligi':'rubl'
    },
    'aqsh':{
        'poytaxt':'vashington',
        'maydon':9631418,
        'aholi':327000000,
        'pul birligi':'dollar'
    },
    'malayziya':{
        'poytaxt':'kuala_Lumpur',
        'maydon':329750,
        'aholi':25000000,
        'pul birligi': "rinngit"
    }
}
davlat=input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning potaxti {info['poytaxt'].title()}"
    f"\nHududi: {info['maydon']} kv.km"
    f"\nAholisi: {info['aholi']}"
    f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
