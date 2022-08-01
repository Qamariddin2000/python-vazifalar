def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)