house_Price= 10000000
has_good_credit =True
if has_good_credit:
if has_good_credit:
    down_payment = 0.1 * house_Price
else:
    down_payment = 0.2 * house_Price
print(f"Down Payment: ${down_payment}")
name = input("Please enter your name")
print(len(name))

if len(name) < 3:
    print("Very little characters")
elif len(name) > 50:
    print("very long characters")
else :
    print("name looks good")


