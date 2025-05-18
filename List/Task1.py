expences=[2200,2350,2600,2130,2190]
print(f'IN Feb the expence is : {expences[1]-expences[0]} more than January.')

print(f"The expences of the first quater of the year are : {expences[0]+expences[1]+expences[2]}")

print('Did i spent 2000 in any month? ',2000 in expences)

expences.append(1980)
print('Expences at the end of June will be : ',expences)

expences[3]=expences[3]-200
print('The updated expences list will be : ', expences)