def solution(number):
    l = []
    sum = 0
    if number >= 0:
        for i in range(number):
            num1 = i
            div_3 = num1 % 3
            if div_3 == 0:
                l.append(num1)
            else:
                continue
        for j in range(number):
            num2 = j
            div_5 = num2 % 5
            if num2 not in l and div_5 == 0:
                l.append(num2)
            else:
                continue

        for k in l:
            sum += k
        return sum
    else:
        return 0