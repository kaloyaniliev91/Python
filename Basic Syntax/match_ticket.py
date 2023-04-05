budget = float(input())
ticket_category = input()
people = int(input())

needed_sum = 0
pure_budget = 0
ticket = 0

if ticket_category == 'Normal':
    ticket = 249.99
elif ticket_category == 'VIP':
    ticket = 499.99

if 1 <= people <= 4:
    pure_budget = budget * 0.25
elif 5 <= people <= 9:
    pure_budget = budget * 0.40
elif 10 <= people <= 24:
    pure_budget = budget * 0.50
elif 25 <= people <= 49:
    pure_budget = budget * 0.60
elif people > 49:
    pure_budget = budget * 0.75

needed_sum = people * ticket
sum_lack = needed_sum - pure_budget
sum_over = pure_budget - needed_sum

if needed_sum > pure_budget:
    print(f'Not enough money! You need {sum_lack:.2f} leva.')
elif pure_budget >= needed_sum:
    print(f'Yes! You have {sum_over:.2f} leva left.')