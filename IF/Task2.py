sugar=input("Enter your fasting sugar level:")
sugar=float(sugar)

if sugar <80:
    print("Your sugar level is low.")
elif sugar>100:
    print("Your sugar level is high.")
else:
    print("Your sugar level is normal.")