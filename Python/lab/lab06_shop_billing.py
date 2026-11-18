
print("CLOTHING STORE BILLING SYSTEM")

customer_name = input("Enter Customer Name: ")
garment_name = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))
total_amount = price * quantity
print()

print("BILL")

print(f"  Customer Name  : {customer_name}")
print(f"  Garment Name   : {garment_name}")
print(f"  Price per Unit : Rs. {price}")
print(f"  Quantity       : {quantity}")
print(f"  Total Amount   : Rs. {total_amount}")

