def solve(balls):
    return round(sum(balls) / 2, 1)


"""head/tail so probability of head is 1/2...
Case 1:
4
1 
2
2
2
result = 1*1/2 + 2*1/2 + 2*1/2 + 2*1/2 = (1+2+2+2)/2 = 7/2 = 3.5"""


if __name__ == '__main__':
    balls_count = int(input())

    balls = []

    for _ in range(balls_count):
        balls_item = int(input())
        balls.append(balls_item)

    result = solve(balls)
    print(result)
