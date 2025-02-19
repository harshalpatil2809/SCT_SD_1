#Function that convert celsius into fahrenite and kelvin
def celcius():
    fah1 = (cel * 9/5) + 32
    print(f"The Fahrenheit is {fah1}\u00B0F")
    kel1 = cel + 273.15
    print(f"The Kelvin is {kel1}K")

#Function that convert fahrenite into celcius and kelvin
def fahrenite():
    cel1 = (fah - 32) * 5/9
    print(f"The Celsius is {cel1}\u00B0C")
    kel1 = (cel1 * 9/5) + 32
    print(f"The Kelvin is {kel1}K")

#Function that convert kelvin into fahrenite and celsius
def kelvin():
    cel1 = kel - 273.15
    print(f"The Celsius is {cel1}\u00B0C")
    fah1 = (cel1 * 9/5) + 32
    print(f"The Fahrenheit is {fah1}\u00B0F")

try:
    #User will give the input
    user_input = input("choose One ( Celsius / Fahrenheit / Kelvin ): ").lower()

    if(user_input == "celsius"):
        cel = int(input("Enter the Celsius: "))
        celcius()
    elif(user_input == "fahrenheit"):
        fah = int(input("Enter the Fahrenheit: "))
        fahrenite()
    elif(user_input == "kelvin"):
        kel = int(input("Enter the Kelvin : "))
        kelvin()
    else:
        print("Invalid Input...!")

except Exception as e:
    print(e)