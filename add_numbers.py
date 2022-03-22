def add(numbers):
    if not numbers.strip():
        return 0
    numbers = numbers.split(',')
    sum = 0
    for i in numbers:
        if i.strip().isdigit():
            sum += int(i.strip())
    return sum
