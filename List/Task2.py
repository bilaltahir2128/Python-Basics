heros=['Spider man','Thor','Hulk','Iron man','Caption america']

print("The length of the list is : ",len(heros))

heros.append('Black panther')
print ('New updated list is :',heros)

heros.remove('Black panther')
print('List after removing Black panther :',heros)

heros.insert(3,'Black panther')
print("List after adding Black panther after hulk :",heros)

heros[1:3]={'Doctor strange'}
print("List after adding Doctor strange in place of Thor & Hulk :",heros)

heros.sort()
print("Final List sorted in alphabetic order :",heros)