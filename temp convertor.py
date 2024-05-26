# I am currently on if loop
print('''
  _______                                   _                     _____                          _             
 |__   __|                                 | |                   / ____|                        | |            
    | | ___ _ __ ___  _ __   __ _ _ __ __ _| |_ _   _ _ __ ___  | |     ___  _ ____   _____ _ __| |_ ___  _ __ 
    | |/ _ \ '_ ` _ \| '_ \ / _` | '__/ _` | __| | | | '__/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \| '__|
    | |  __/ | | | | | |_) | (_| | | | (_| | |_| |_| | | |  __/ | |___| (_) | | | \ V /  __/ |  | || (_) | |   
    |_|\___|_| |_| |_| .__/ \__,_|_|  \__,_|\__|\__,_|_|  \___|  \_____\___/|_| |_|\_/ \___|_|   \__\___/|_|   
                     | |                                                                                       
                     |_|                                                                                       
''')
unit = str(input("\t____CHOOSE UNIT CONVERTOR____\n \tC - Kelvin to Celsius\n \tK - Celsius to Kelvin\n \tF - Celsius to Fahrenheit \n \tF`- Kelvin to Faghrenheit\n \tK`- Fahrenheit to Kelvin\n \tC`- Fahrenheit to Celsius\n---> "))
user_inpt = int(input("Enter the Temparatuere - "))
unit.upper()

if unit == "c":
    formula_1 = user_inpt - 273.15
    print(f'{user_inpt} K is equivelent to {formula_1} C')
elif unit == "k":
    formula_2 = user_inpt + 273.15
    print(f'{user_inpt} C is equivelent to {formula_2} K')
elif unit == "f":
    formula_3 = user_inpt*(9/6) + 32
    print(f'{user_inpt} C is equivelent to {formula_3} F')
elif unit == "f`":
    formula_4 = (user_inpt - 273.15)* 9/5 + 32
    print(f'{user_inpt} K is equivelent to {formula_4} F')
elif unit == "k`":
    formula_5 = (user_inpt - 32) * 5/9 + 273.15
    print(f'{user_inpt} F is equivelent to {formula_5} K')
elif unit == "c`":
    formula_6 = (user_inpt - 32 ) * 5/9
    print(f'{user_inpt} F is equivelent to {formula_6} C')
else:
    print("Inalid input enter correct conversion!!!!")
print(">>>>>>-| Thank you |-<<<<<<<")