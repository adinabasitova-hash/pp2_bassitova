#1
def convertToOunces(grams):
  return grams * 28.3495231

#2
def convertToCelsius(F):
  return (5 / 9) * (F - 32)

#3
'''r + c = 35
   4r + 2c = 94
   '''
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    print("Rabbits:", rabbits)
    print("Chickens:", chickens)

#4
def filter_prime(numbers):
    prime_numbers = []

    for x in numbers:
        if x < 2:
            continue

        prime = True

        for i in range(2, x):
            if x % i == 0:
                prime = False
                break

        if prime:
            prime_numbers.append(x)

    return prime_numbers


numbers = list(map(int, input().split()))



#5
def permutations(s):
    if len(s) == 1:
        return [s]

    result = []

    for i in range(len(s)):
        char = s[i]
        rest = s[:i] + s[i+1:]

        for p in permutations(rest):
            result.append(char + p)

    return result


s = input()

for p in permutations(s):
    print(p)
