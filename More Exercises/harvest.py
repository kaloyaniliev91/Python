import math

grape_total_area = int(input())
grape_per_one_sq_meter = float(input())
wine_for_sale = int(input())
workers = int(input())

wine_per_person = 0


total_grape = grape_total_area * grape_per_one_sq_meter
total_wine = (total_grape * 0.4) / 2.5

diff = abs(total_wine - wine_for_sale)

if total_wine >= wine_for_sale:
    wine_per_person = (total_wine - wine_for_sale) / workers
    print(f'Good harvest this year! Total wine: {math.floor(total_wine)} liters.')
    print(f'{math.ceil(diff)} liters left -> {math.ceil(diff / workers)} liters per person.')
else:
    print(f'It will be a tough winter! More {math.floor(diff)} liters wine needed.')