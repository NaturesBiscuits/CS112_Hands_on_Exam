print("****************************")
print("| Number System Conversion |")
print("****************************")
print("By: Butad, John Esteve")
print("By: Flores, John Vincent\n")

answer = eval(input("Enter a number: "))
print("********************************************")
print("[1] Decimal Number to Binary Number")
print("[2] Decimal Number to Octal Number")
print("[3] Decimal Number to Hexadecimal Number")
print("********************************************")

chosen = eval(input("How do you want ot convert " + str(answer) + "? Enter from [1-3]: "))
if chosen == 1:
    final = eval(format(answer, 'b'))
    system = 'Binary'
elif chosen == 2:
    final = eval(format(answer, 'o'))
    system = 'Ocatal'
elif chosen == 3:
    final = eval(format(answer, 'x'))
    system = 'Hexadecimal'
else:
    print("Invalid option. Please try again.")

print("********************************************************")
print("Decimal", answer, "Converted to", system, "Number is", final)
print("********************************************************")
