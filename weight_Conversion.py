
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g:")
if unit.upper() == "L" :
    converted = weight * 0.45359237
    print(f"Your weight in kgs is: {converted}")
elif unit.upper() == "K" :
    converted = weight / 0.45359237
    print(f"Your weight in lbs is: {converted}")
else :
    print("Please enter a valid value! ")


    #dngfmjd,msdkmskymst,ms,tdgm,tsu