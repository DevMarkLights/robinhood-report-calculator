import csv
from tabulate import tabulate
amountMadeThisMonthFromOptions=0
dividendIncomeThisMonth=0
transfersToSpending=0
optionStocksP_L={}
file_name=''
def addToMap(symbol,amount):
    if optionStocksP_L.get(symbol) == None:
        optionStocksP_L[symbol] = amount
    else:
        optionStocksP_L[symbol] = optionStocksP_L[symbol] + amount

with open('May 1, 2025 -  May 31, 2025.csv', 'r') as file:
    csv_reader = csv.reader(file)
    i = 0
    file_name=file.name
    print("\n"+file.name.split('.')[0])
    for row in csv_reader:
        if row[0] == '' or i == 0:
            i+=1
            continue
        if row[5].lower() == 'bto' or row[5].lower() == 'btc': #loss
            amountMadeThisMonthFromOptions = amountMadeThisMonthFromOptions - float(row[8].replace('(','').replace(')','').replace('$','').replace(',',''))
            addToMap(row[3],-float(row[8].replace('(','').replace(')','').replace('$','').replace(',','')))
        elif row[5].lower() == 'sto' or row[5].lower() =='stc': # profit
            amountMadeThisMonthFromOptions = amountMadeThisMonthFromOptions + float(row[8].replace('$','').replace(',',''))
            addToMap(row[3],float(row[8].replace('$','').replace(',','')))
        elif row[5].lower() == 'cdiv': # profit
            dividendIncomeThisMonth = dividendIncomeThisMonth + float(row[8].replace('$','').replace(',',''))
        elif row[5].lower() == 'xent': # loss
            transfersToSpending = transfersToSpending + float(row[8].replace('(','').replace(')','').replace('$','').replace(',',''))
        i+=1

print("\nAmount made from options:    $"+ str(round(amountMadeThisMonthFromOptions,2)))
print("Dividends made:                $"+ str(round(dividendIncomeThisMonth,2)))
print("Transfers to spending account: $"+ str(round(transfersToSpending,2)))
print("Total income:                  $"+ str(round(amountMadeThisMonthFromOptions+dividendIncomeThisMonth,2))+"\n")


table=[]
# keys = optionStocksP_L.keys
for symbol in optionStocksP_L:
    table.append([symbol,optionStocksP_L.get(symbol)])

print(tabulate(table,['symbol','amount'],'fancy_outline'))

with open('ouput.txt','w') as file:
    file.write(file_name+"\n\n")
    file.write("Amount made from options:    $"+ str(round(amountMadeThisMonthFromOptions,2))+"\n")
    file.write("Dividends made:                $"+ str(round(dividendIncomeThisMonth,2))+"\n")
    file.write("Transfers to spending account: $"+ str(round(transfersToSpending,2))+"\n")
    file.write("Total income:                  $"+ str(round(amountMadeThisMonthFromOptions+dividendIncomeThisMonth,2))+"\n")

    file.write("\n"+tabulate(table,['symbol','amount'],'rounded_outline'))