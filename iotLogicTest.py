import locale

all_items =["susu","daging","lampu","masker","apel"]
all_prices = [50000,20000,15000,25000,30000]

promo_items =[all_items[0],all_items[3]]
promo_prices =[all_items[0],all_items[3]]

price_items=[]
name_items=[]
amount_items=[]

def welcome():
    print("=======================")
    print('Welcome to TokoPaedi :)')
    print('Please Select Menu\n 1:Show All Item List\n 2.Show Promo Item List\n 3.Checkout\n 4.Add another Item\n 6.Exit')
    print("=======================")
def checkout():
    print("Select Menu:")
    print("=======================")
    print(" 3:Checkout item\n 4.Add another Promo items\n 5.Add another Available items")
def wtb():
    print("\nWant to buy ? (Y/N)")
# To use default settings, set locale to None or leave the second argument blank.
# print(locale.setlocale(locale.LC_ALL, ''))

# To use a specific locale (Great Britain's locale in this case)
locale.setlocale(locale.LC_ALL, 'id_ID')

welcome()
global total
global indX
sumPrices=0
while True:
    userInput=input()
    if (userInput=="0"):
        welcome()
    if (userInput=="1"):
        print("All Available Items:")
        for x in range(len(all_items)):
            print("-", all_items[x])
        wtb()
        userInput
    if (userInput =="2"):
        print("\033[A","All Promo Items:")
        for x in range(len(promo_items)):
            print("-",promo_items[x])
        wtb()
        userInput
    if (userInput=="Y" or userInput=="y"):
        print("\033[A","Please Input Item: (character must be correct e.g -> susu)")
        itemInput=input()                                                       #input item
        save_items = all_items.index(itemInput)                                 #save selected item
        print("\033[A",all_items[save_items], "selected\n")
        print("Enter Amount: ")
        amount=input()
        total = int(amount)*all_prices[save_items]                              #print (bill) total
        print("\033[A",all_items[save_items], "selected:", amount,"pcs\n")
        price_items.append(total)                                               #save unit price to array
        name_items.append(itemInput)                                            #save item name to array
        amount_items.append(amount)
        checkout()
    if (userInput=='3'):
        for indX in range(len(price_items)):
            sumPrices=sumPrices+price_items[indX]
        finalPrice = locale.currency(sumPrices, grouping=True)
        print("\033[A","\nTotal Harga:\t",finalPrice)
        print(" Detail:")
        indItem = name_items.index(itemInput)
        for x in range(len(name_items)):                                        #breakdown shopping item
            untPrice = locale.currency(price_items[x], grouping=True)           
            print(" ",amount_items[x], name_items[x], "\t->",untPrice)
        
    if(userInput=='4'):
        print("\033[A","All Promo Items:")
        for x in range(len(promo_items)):
            print("-",promo_items[x])
        wtb()
        userInput
    if(userInput=='5'):
        print("\033[A","All Available Items:")
        for x in range(len(all_items)):
            print("-",all_items[x])
        wtb()
        userInput
    if (userInput=='6'):
        print('Thank you for shopping, Have a Nice day')
        exit()
    
