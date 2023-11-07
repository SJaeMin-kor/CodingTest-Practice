def my_factorial(a):
    if a > 1:
        return a*my_factorial(a-1)
    else:
        return 1

def solution(n):
    answer = 0
    a = 1
    while True:
        if my_factorial(a) > n:
            answer = a-1
            break
        elif my_factorial(a) == n:
            answer = a
            break
        else:
            a += 1

    return answer