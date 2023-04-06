student_name = input()
grades_total_counter = 0
counter_of_years = 0
failed_counter = 0

while True:
    current_year_grade = float(input())

    if current_year_grade < 4:
        failed_counter += 1
        if failed_counter == 2:
            print(f'{student_name} has been excluded at {counter_of_years + 1} grade')
            break
    else:
        grades_total_counter += current_year_grade
        counter_of_years += 1

        if counter_of_years == 12:
            average_grade = grades_total_counter / 12
            print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
            break