month, date = (s for s in input().split())
if (month == "OCT" and date == "31") or (month == "DEC" and date == "25"):
    print("yup")
else:
    print("nope")
