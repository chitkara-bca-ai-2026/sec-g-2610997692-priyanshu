
print("DATA CONVERSION UTILITY")

product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))
total_price = price * quantity
amount_str = str(total_price)
print()

print("TYPE CASTING SUMMARY")

print(f"{'Variable':<15} {'Value':<15} {'Python Type'}")

print(f"{'product_name':<15} {product_name:<15} {type(product_name)}")
print(f"{'price':<15} {price:<15} {type(price)}")
print(f"{'quantity':<15} {quantity:<15} {type(quantity)}")
print(f"{'total_price':<15} {total_price:<15} {type(total_price)}")
print(f"{'amount_str':<15} {amount_str:<15} {type(amount_str)}")
print()
print("TAX INVOICE")

print(f"  Product Name   : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print(f"  Invoice Total  : Rs. {amount_str}")

