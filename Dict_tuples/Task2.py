import statistics

stocks={
     'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl': [234,180,160]
}
def print_all():
    for country,price in stocks.items():
        avg=statistics.mean(price)
        print(f"{country} ==> {price} ==>> avg :{avg}")

def add():
    stock = input("Enter a stock name to add:")
    price = input("Enter price of the stock:")
    price=float(price)
    if stock in stocks:
        stocks[stock].append(price)
    else:
        stocks[stock] = [price]
    

def main():
    operation=input("Enter the operation (add,print)")
    operation=operation.lower()
    if operation=="add":
        add()
    elif operation=="print":
        print_all()
    else:
        print("Invalid operatoion! ")

main()