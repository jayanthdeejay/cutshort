import re

def add(numbers):
    if not numbers.strip():
        return 0
    if(numbers[0:2] == '//'):
        delimiter = numbers[2]
        numbers = numbers[3:]
    else:
        delimiter = ','
    numbers = numbers.replace("\n", ",")
    numbers = numbers.replace(delimiter, ",")

    # Replace 2 or more consecutive commas with one
    # --
    pattern = re.compile(r'(,){2,}')
    numbers = re.sub(pattern, ',', numbers)
    # --
    
    numbers = numbers.split(",")
    sum = 0
    for i in numbers:
        if not i:
            pass
        if i.strip().isdigit():
            sum += int(i.strip())
    return sum
