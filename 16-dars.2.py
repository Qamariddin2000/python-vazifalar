navoiy={
    'ism':'Alisher Navoiy',
    'tyil':1441,
    'vyil':1501,
    'tjoy':'Xirot',
    'asarlari':['Layli va majnun','Sabbai Sayyor', 'Sadi iskandariy','Mahbub ul-qulub']
}
vohidov={
    'ism':'Erkin Vohidov',
    'tyil':1936,
    'vyil':2016,
    'tjoy':"Farg'ona",
    'asarlari':["O'zbegim","Nido",'Donish qishloq latifalari',"Ruhlar isyoni"]
}
qodiriy={
    'ism':'Abdulla Qodiriy',
    'tyil':1894,
    'vyil':1938,
    'tjoy':"Toshkent",
    'asarlari':["O'tkan kunlar",'Mehrobdan chayon','Uloqda','Obid ketmon']
}
temur={
    'ism':'Amir Temur',
    'tyil':1336,
    'vyil':1405,
    'tjoy':'Shahrisabz',
    'asarlari':['Temur tuzuklari',"G'arbga qilingan yurishlar"]
}
mashhurlar=[navoiy, vohidov, qodiriy, temur]
for inson in mashhurlar:
    asarlar=inson['asarlari']
    print(f"\n{inson['ism']}ning mashhur asarlari: ")
    for asar in asarlar:
        print(asar)