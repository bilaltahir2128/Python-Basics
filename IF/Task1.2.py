Pakistan = ["Lahore","Karachi","Islamabad"]
india = ["mumbai", "banglore", "chennai", "delhi"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1=input("Enter 1st city name : ")
city2=input("Enter 2nd city name : ")

if city1 in Pakistan and city2 in Pakistan:
    print("Both cities belongs to Pakistan.")
elif city1 in india and city2 in india:
    print("Both cities belongs to india.")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities belongs to bangladesh.")

else:
    print("Both cities not belongs to same country.")