heritage = float(input())
year_to_live = int(input())

YEARS = 18

for current_year in range(1800, year_to_live + 1):
    if current_year % 2 == 0:
        heritage -= 12000
    else:
        heritage -= (12000 + 50 * YEARS)
    YEARS += 1

if heritage >= 0:
    print(f'Yes! He will live a carefree life and will have {heritage:.2f} dollars left.')
else:
    print(f'He will need {abs(heritage):.2f} dollars to survive.')