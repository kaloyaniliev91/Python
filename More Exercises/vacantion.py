needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while True:
    action = input()
    money = float(input())

    if action == 'spend':
        spending_counter += 1
        days_counter += 1

        if money <= owned_money:
            owned_money -= money

        elif money > owned_money:
            owned_money = 0

        if spending_counter == 5:
            print(f"You can't save the money.\n{days_counter}")
            break

    elif action == 'save':
        spending_counter = 0
        days_counter += 1
        owned_money += money

    if owned_money >= needed_money:
        print(f'You saved the money for {days_counter} days.')
        break