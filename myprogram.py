import sys
total = 0

n = len(sys.argv)

for i in range (1,n):
    total += int(sys.argv[i])

print("The total is:",total)