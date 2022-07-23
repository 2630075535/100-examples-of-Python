def sun_of_aquare(n):
    result = 0
    for number in range(1, n+1):
        result += number * number
    return result


print("sun of aquare 3", sun_of_aquare(3))
print("sun of aquare 5", sun_of_aquare(5))
print("sun of aquare 10", sun_of_aquare(10))



