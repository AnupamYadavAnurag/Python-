# Product data: (Product ID, Price, Stock Quantity)
products = [
    ("p001", 150.00, 5),            
    ("p002", 200.00, 0),    
    ("p003", 50.50, 10),            
    ("p004", "99.99", 3),          
    ("p005", 300.00, 0), 
    ("p006", 75.00, -1)             # fixed wrong comma
] 

def process_stock(product_list):    # mssing colon
    total_value = 0                
    out_of_stock_items = []       

    for product in product_list:
        # Calculate the value of each product in stock
        stock_value = float(product[1]) * product[2]   # convert string price to float
        total_value += stock_value                     # changed = to +=

        # Check for out of stock items
        if product[2] == 0:                            # old check used stock value, change to quantity
            out_of_stock_items.append(product[0])      # changed .add() to .append()

    return total_value, out_of_stock_items


stock_value, low_stock = process_stock(products)

print(f"Total value of all stock: {stock_value}")  
print(f"Out of stock products: {low_stock}")
