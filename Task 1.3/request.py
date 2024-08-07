request_spending = {
    "Mahek": {
    "balance": 3000.00,
    "transactions": [
        {"amount": -9000.00, "category": "Creatives"},
        {"amount": 7000.00, "category": "Sponsor"},
        {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    
    "Arham": {
    "balance": 5000.00,
    "transactions": [
        {"amount": 8000.00, "category": "Stalls"},
        {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    
    "Unnati": {
    "balance": 3500.00,
    "transactions": [
        {"amount": -5000.00, "category": "Attraction"},
        {"amount": 2500.00, "category": "Promo"},
        {"amount": -900.00, "category": "Lighting"}, 
        {"amount":-3000.00, "category": "Games"}
        ]
    },
    
    "Gaurang": {
    "balance": 2000.00,
    "transactions": [
        {"amount": 1500.00, "category": "Website"},
        {"amount": 1000.00, "category": "C2C"},
        {"amount": -500.00, "category": "Posters"}
        ]
    }
}

def account_balance(request_spending, account_id):
    print(request_spending[account_id]['balance'])

def money_owed(request_spending, account_id):
    transac = request_spending[account_id]['transactions']
    # print(type(transac))
    total =0
    for i in range(len(transac)):
        total += transac[i]['amount']
    print(total)
    
def total_spending(request_spending, account_id, category):
    cat_list = []
    cat_lst = []
    match account_id:
        case 'Mahek':
            cat_lst = ['Creatives','Sponsor','Prize-Money']
            cat_list = [0,1,2]
        case 'Arham':
            cat_lst = ['Stalls','Seminars']
            cat_list = [0,1]
        case 'Unnati':
            cat_lst = ['Attraction','Promo','Lightning','Games']
            cat_list = [0,1,2,3]
        case 'Gaurang':
            cat_lst = ['Website','C2C','Posters']
            cat_list = [0,1,2]
    cnt = -1
    for i in cat_lst:
        cnt += 1
        if(i==category):
            #cat_list[i]
            print(request_spending[account_id]['transactions'][cat_list[cnt]]['amount'])

total_spending(request_spending,'Arham','Seminars') 
account_balance(request_spending,"Gaurang")
money_owed(request_spending,"Gaurang")
    
    
    
    # a= dict(request_spending[account_id]['transactions'])
    # print(a)
    # #b=a[category]
    # #print(b)
    # for x in a:
    #     b=a.gets("category")
    #     if(category == b):
    #         print(a)
# total_spending(request_spending,"Unnati","Attraction")
    
    
    
    
    
    
    
    #  match account_id:
    #     case "Mahek":
    #         match:
    #             case 
    #         print("One")
    #     case "Arham":
    #         print("Two")
    #     case "Unnati":
    #         print("Three")
    #     # default pattern
    #     case "Gaurang":
    #         print("Number not between 1 and 3")