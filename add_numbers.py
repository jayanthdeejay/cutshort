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
    negs = []
    for i in numbers:
        i = i.strip()
        if not i:
            pass
        elif(i[0] == '-'):
            negs.append(int(i))
        elif i.isdigit():
            sum += int(i)
                
    
    if(negs):
        raise ValueError("negatives not allowed: {}".format(negs))
    else:
        return sum
