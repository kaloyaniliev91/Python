MAX_POINTS = 1250.5

actor_name = input()
points = float(input())
judges = int(input())

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2

    if points > MAX_POINTS:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break

else:
    print(f'Sorry, {actor_name} you need {MAX_POINTS - points:.1f} more!')