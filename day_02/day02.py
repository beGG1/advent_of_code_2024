import copy

if __name__ == "__main__":
    # reading the imput
    with open('./input') as f:
        s = f.read()

    s = s.split('\n')
    a = []
    for i in s:
        a.append(list(map(int, i.split(' '))))
    safe = 0
    
    for i in a:
        if i == sorted(i) or i == sorted(i, reverse=True):
            flag = 1
            for j in range(len(i) - 1):
                if abs(i[j] - i[j + 1]) < 1 or abs(i[j] - i[j + 1]) > 3:
                    flag = 0
                    break
            safe += flag
    print(f"Safe: {safe}")
    
    # Part 2
    
    with open('./input') as f:
        s = f.read()

    s = s.split('\n')
    a = []
    for i in s:
        a.append(list(map(int, i.split(' '))))
    safe = 0
    for b in a:
        for d in range(len(b)):
            i = list(copy.deepcopy(b))
            i = i[:d] + i[d+1:]
            flag = 1
            inc_dec = i == sorted(i) or i == sorted(i, reverse=True)
            if inc_dec:
                for j in range(len(i) - 1):
                    if abs(i[j] - i[j + 1]) < 1 or abs(i[j] - i[j + 1]) > 3:
                        flag = 0
                        break
            if flag and inc_dec:
                safe += flag
                break
    print(f"Safe Part_2: {safe}")