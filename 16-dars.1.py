navoiy={
    'ism':'Alisher Navoiy',
    'tyil':1441,
    'vyil':1501,
    'tjoy':'Xirot'
}
vohidov={
    'ism':'Erkin Vohidov',
    'tyil':1936,
    'vyil':2016,
    'tjoy':"Farg'ona"
}
qodiriy={
    'ism':'Abdulla Qodiriy',
    'tyil':1894,
    'vyil':1938,
    'tjoy':"Toshkent"
}
temur={
    'ism':'Amir Temur',
    'tyil':1336,
    'vyil':1405,
    'tjoy':'Shahrisabz'
}
mashhurlar=[navoiy, vohidov, qodiriy, temur]
for inson in mashhurlar:
    print(f"{inson['ism']} {inson['tyil']}-yilda "
    f"{inson['tjoy']}da tavallud topgan. {inson['vyil']-inson['tyil']}-yil "
    " umr ko'rgan")