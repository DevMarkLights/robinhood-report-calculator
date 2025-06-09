import csv

amountMadeThisMonthFromOptions=0
dividendIncomeThisMonth=0
transfersToSpending=0
with open('May 1, 2025 -  May 31, 2025.csv', 'r') as file:
    csv_reader = csv.reader(file)
    i = 0
    print("\n"+file.name.split('.')[0])
    for row in csv_reader:
        if row[0] == '' or i == 0:
            i+=1
            continue
        if row[5].lower() == 'bto' or row[5].lower() == 'btc': #loss
            amountMadeThisMonthFromOptions = amountMadeThisMonthFromOptions - float(row[8].replace('(','').replace(')','').replace('$','').replace(',',''))
        elif row[5].lower() == 'sto' or row[5].lower() =='stc': # profit
            amountMadeThisMonthFromOptions = amountMadeThisMonthFromOptions + float(row[8].replace('$','').replace(',',''))
        elif row[5].lower() == 'cdiv': # profit
            dividendIncomeThisMonth = dividendIncomeThisMonth + float(row[8].replace('$','').replace(',',''))
        elif row[5].lower() == 'xent': # loss
            transfersToSpending = transfersToSpending + float(row[8].replace('(','').replace(')','').replace('$','').replace(',',''))
        i+=1

print("\nAmount made from options:    $"+ str(round(amountMadeThisMonthFromOptions,2)))
print("Dividends made:                $"+ str(round(dividendIncomeThisMonth,2)))
print("Transfers to spending account: $"+ str(round(transfersToSpending,2)))
print("Total income:                  $"+ str(round(amountMadeThisMonthFromOptions+dividendIncomeThisMonth,2))+"\n")