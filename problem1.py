def getSumOfMultiples(baseNum, count):
    the_sum = baseNum
    max_value = int(count/baseNum) + 1

    for i in range(2, max_value):
        the_sum += baseNum * i

    return the_sum

def sumDivisibleBy(number, count):
    the_max = int(count/number)
    return int(number * (the_max * (the_max + 1)) /2)

count = 999

# attempt 1
count2 = getSumOfMultiples(3, count) + getSumOfMultiples(5, count) - getSumOfMultiples(15, count)
print(count2)

# attempt 2
count3 = sumDivisibleBy(3, count) + sumDivisibleBy(5, count) - sumDivisibleBy(15, count)
print(count3)