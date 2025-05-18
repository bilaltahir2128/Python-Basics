km =-1
for i in range(5):
    print(f"You ran {i+1} km.")
    ques=input("Are you tired? ")
    if ques=='yes':
        km=i+1
        break
    else:
        km=i+1
        continue

if km<5:
    print("Unfortunately you didn't finish the rase.You ran ",km+1,"km.")

elif km==5:
    print("Congratulations! you finish the 5km race. ")