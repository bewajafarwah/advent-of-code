def parse_arguments(lines):
    ids = {}

    for line in lines:
        id = int(line.split(' ')[1][:-1])
        sets = []
        for _set in ''.join(line.split(':')[1:]).split(';'):
            _tmp = []
            for val in _set.split(","):
                num, color = val.strip().split(" ")
                _tmp.append([int(num), color])
            sets.append(_tmp)

        ids[id] = sets
    return ids

def read_lines():
    with open('day2.in', 'r') as f:
        lines = f.read().splitlines()
    return parse_arguments(lines)

lines = read_lines()

mapping = {
        'red': 12,
        'green' : 13,
        'blue' : 14
}

def check_set(_set):
    current = {"blue" : 0, "green" : 0, "red": 0}   
    for num, color in _set:
        current[color] += num
    for color in current:
        if current[color] > mapping[color]:
            return False
    return True

def part1():

    total_sum = 0

  
    for id in lines:
        flg = True
        for _set in lines[id]:
            if not check_set(_set):
                flg = False
                break
        if flg:
            total_sum += id

 
    print(f"part1: {total_sum}")

def max_val(_set, current):
    for num, color in _set:
        current[color] = max(current[color], num)
    return current

def part2():

    total_sum = 0
    for id in lines:
        current = {"blue" : 0, "green" : 0, "red": 0} 
        for _set in lines[id]:
            current = max_val(_set, current)
        
        power = 1
        for color in current:
            power *= current[color]

        total_sum += power


    print(f"part2: {total_sum}")

if __name__ == "__main__":
    part1()
    part2()

