def calculate_total(shoppig_list):
    prices=[]
    try:
        with open(r"C:\Users\lenovo\Desktop\python training\text files\prices.txt","r")as file:
            for i in file:
                i=i.strip()
                if '='in i:
                 item,price=i.split('=')
                prices[item.strip()]=float(price.strip())
    except:
        print("Error: Price list not available.")
        return 0.0
    total = 0.0
    for item in shopping_list:
        if item in prices:
            total += prices[item]
        else:
            print(f"Warning: {item} not found.")

    return total
shopping_list = ['apple', 'banana', 'apple', 'milk']
total = calculate_total(shopping_list)
print("Total cost:", total)
