def add(numbers):
    if not numbers:
        return 0
    numbers = numbers.split(',')
    sum = 0
    for i in numbers:
        if i.isdigit():
            sum += int(i)
    return sum
