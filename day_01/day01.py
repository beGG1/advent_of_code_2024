
if __name__ == "__main__":
    # reading the imput
    with open('./input') as f:
        s = f.read()
    
    # creating 2 lists
    s = s.split('\n')
    first_lst = []
    second_lst = []
    for i in s:
        x, y = i.split('   ')
        first_lst.append(int(x))
        second_lst.append(int(y))
    
    # sorting lists
    first_lst.sort()
    second_lst.sort()
    
    # calculating the first answer
    summ = 0
    for i in range(len(first_lst)):
        summ += (abs(first_lst[i] - second_lst[i]))
    
    # Print answer to part 1
    print("Sum of differences: ", summ)
    
    simmilarity_score = 0
    for i in first_lst:
        simmilarity_score += i * second_lst.count(i)
    print("Simmilarity score: ",simmilarity_score)
    