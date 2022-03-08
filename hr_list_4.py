if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = max(arr)
    second_winner = -23456
    for i in range(0,len(arr)):
        if(arr[i] != winner):
            second_winner = max(second_winner, arr[i])
    print(second_winner)