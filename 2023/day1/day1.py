import re

with open('day1.in', 'r') as f:
    lines = f.read().splitlines()

def part1():
    total_sum = 0
    
    for line in lines:
        
        numbers = []
        for ch in line:
            if ch.isdigit():
                numbers.append(ch)
        total_sum += int(numbers[0] + numbers[-1])
    
    print(f'part1: {total_sum}')

def part2():
    number_mapping = {'one': '1',
        'two' : '2',
        'three': '3',
        'four' : '4',
        'five': '5',
        'six': '6',
        'seven' : '7',
        'eight': '8',
        'nine': '9',
    }

    total_sum = 0

    for line in lines:
        numbers = []
        
        for i, ch in enumerate(line):
            if ch.isdigit():
                numbers.append([i, ch])
        
        for num in number_mapping:
            for m in re.finditer(num, line):
                numbers.append([m.start(), number_mapping[num]])
        
        numbers.sort(key=lambda x:x[0])
        total_sum += int(numbers[0][1] + numbers[-1][1])

    print(f'part2: {total_sum}')


if __name__ == "__main__":
    part1()
    part2()
