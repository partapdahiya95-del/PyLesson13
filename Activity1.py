def greet_customer():
    print("Welcome to my lemon juice stand")

greet_customer()

cup_num = int(input("Enter the number of cups: "))
price_per_cup = int(input("Enter the price per cup: "))

def calculate_total(price_per_cup, cup_num):
    total = price_per_cup * cup_num
    return total

cal_total = calculate_total(price_per_cup, cup_num)

total_cost = round(cal_total, 2)
print("Your total cost is ", total_cost)

amt_paid = int(input("Enter the amount you paid: "))
def calculate_change(total, amt_paid):
    change = amt_paid - total
    return change

cal_change = calculate_change(total_cost, amt_paid)

print("I have to give you ", cal_change)

print("===== LEMONADE STAND RECEIPT =====")
print("Price per cup: ", price_per_cup)
print("Cup sold: ", cup_num)
print("Total Cost: ", total_cost)
print("Amount paid: ", amt_paid)
print("Change due: ", total_cost - amt_paid)
print("Thanks for stopping by the stand!")
print("====================================")