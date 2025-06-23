import sys
MOD = 10 ** 9 + 7

n = int(sys.stdin.readline())
bottomUpCombos = [0] * (n + 1)

# Hardcoded base cases 
precomputed = [1, 1, 2, 4, 8, 16]
for i in range(min(n + 1, 6)):
    bottomUpCombos[i] = precomputed[i]

# Now use DP from total = 6 onward
for total in range(6, n + 1):
    for roll in range(1, 7):
        bottomUpCombos[total] += bottomUpCombos[total - roll]
    bottomUpCombos[total] %= MOD

print(bottomUpCombos[n])
