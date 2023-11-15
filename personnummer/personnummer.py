persnmr = input()
if "-" in persnmr:
    if int(persnmr[:2]) < 20:
        print("20"+persnmr.replace("-",""))
    else:
        print("19"+persnmr.replace("-",""))
elif "+" in persnmr:
    if int(persnmr[:2]) < 20:
        print("19"+persnmr.replace("+",""))
    else:
        print("18"+persnmr.replace("+",""))