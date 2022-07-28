buyurtmalar=['olma','anor','uzum','qovun']
e_bozor={
    'olma':10000,
    'uzum':15000,
    'qovun':15000,
    'tarvuz':10000

}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in e_bozor.keys():
        narh=e_bozor[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma.title()} yo'q")