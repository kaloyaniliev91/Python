v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1 = p1 * h
pipe2 = p2 * h

total = pipe1 + pipe2

total_percent = (total * 100) / v

remaining = total - v

pipe1_percent = (pipe1 * 100) / total
pipe2_percent = (pipe2 * 100) / total

if total <= v:
    print(f'The pool is {total_percent:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.')
else:
    print(f'For {h:.2f} hours the pool overflows with {remaining:.2f} liters.')