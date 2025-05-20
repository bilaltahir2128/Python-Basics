population={
    "china":143,
    "india":136,
    "usa":32,
    "akistan":21}

def print_all():
    for country,p in population.items():
        print(f"{country} ==> {p}")


def add():
    country=input("Enter the country name: ")
    country=country.lower()
    if country in population:
        print("Country already exist in dictionary.")
    else:
        ppl=input(f"Enter the population of {country} :")
        population[country]=ppl
        print("Updated dictionary :",population)


def remove():
    country=input("Enter the country to remove :")
    country=country.lower()
    if country not in population:
        print(f"{country } is not present in our dictionary.")
    else:
        del population[country]
        print("Updated dictoionary: ",population)

def query():
    country=input("Enter the countryy for which you wants to query: ")
    country=country.lower()
    if country not in population:
        print("Country you entered not in our database.")
    else:
        print(f"{country } has population {population[country]} m ")

def main():
    operation=input("Enter the peration you want to do ( add, remove , query, print_all)") 
    operation=operation.lower()
    if operation == "add":
        add()
    elif operation == "remove":
        remove()
    elif operation == "query":
        query()
    elif operation == "print_all":
        print_all()
    else:
        print("Invalid operation! ")

main()