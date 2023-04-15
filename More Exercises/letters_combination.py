start = ord(input())
end = ord(input())
skip = input()

count = 0

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            if chr(i) != skip and chr(j) != skip and chr(k) != skip:
                print(chr(i) + chr(j) + chr(k), end=' ')
                count += 1

print(count)