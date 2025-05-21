with open('stocks.csv','r') as x,open ('output.csv','w') as out:
    out.write("Company name , PE Ratio , PB Ratio \n")
    next(x)

    for line  in x:
        tokens=line.split(',')
        stock=tokens[0]
        price=float(tokens[1])
        eps=float(tokens[2])
        book=float(tokens[3])
        pe=round(price/eps,2)
        pb=round(price/book,2)
        out.write(f"{stock},{pe},{pb} \n")