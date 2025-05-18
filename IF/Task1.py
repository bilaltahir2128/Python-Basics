Pakistan = ["Lahore","Karachi","Islamabad"]
india = ["mumbai", "banglore", "chennai", "delhi"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input("Enter a city name: ")

if city in Pakistan:
    print(city," is in Pakistan.")
elif city in india:
    print(city,"is in India.")
elif city in bangladesh:
    print(city, "is in Bangladesh.")

else :
    print("The city you entered is not recongnized in our registered countries.")