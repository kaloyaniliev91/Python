budget = float(input())
category = input()
num_people = int(input())

ticket_price = 0
transport_percent = 0

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

if 1 <= num_people <= 4:
    transport_percent = 0.75
elif 5 <= num_people <= 9:
    transport_percent = 0.6
elif 10 <= num_people <= 24:
    transport_percent = 0.5
elif 25 <= num_people <= 49:
    transport_percent = 0.4
elif num_people >= 50:
    transport_percent = 0.25

total_cost = num_people * ticket_price + budget * transport_percent

if budget >= total_cost:
    remaining_money = budget - total_cost
    print(f"Yes! You have {remaining_money:.2f} leva left.")
else:
    needed_money = total_cost - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")