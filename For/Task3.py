expense_list = [2340, 2500, 2100, 3100, 2980]
month=["jan","feb","march","apil","may"]

amount=input("Enter an expense amount : ")
amount=int(amount)

month_no=-1
 
for i in range(len(expense_list)) :
   if amount==expense_list[i]:
      month_no=i
      break

if month_no!=-1:
    print("You spent ",amount," in ",month[i])
else:
   print("Expense amount entered is invalid!")
