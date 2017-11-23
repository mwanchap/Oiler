def getSumOfMultiples(baseNum, count):
    the_sum = baseNum

    for i in range(2, count/baseNum):
        the_sum += baseNum * i

    return the_sum

def sumDivisibleBy(number, count):
    the_max = int(count/number)
    return int(number * (the_max * (the_max + 1)) /2)

count = 999
count3 = sumDivisibleBy(3, count) + sumDivisibleBy(5, count) - sumDivisibleBy(15, count)
print(count3)