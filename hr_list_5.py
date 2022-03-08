def find_second_lowest(arr):
    winner = min(arr)
    second_winner = 2535847
    for i in range(0,len(arr)):
        if(arr[i] > winner and arr[i] ):
            second_winner = min(second_winner, arr[i])
    return second_winner

if __name__ == '__main__':
    score_array = []
    names_array = []
    for _ in range(int(input())):
        enter_arr = []
        name = input()
        score = float(input())
        names_array.append(name)
        score_array.append(score)
    second_lowest_score = find_second_lowest(score_array)
    sorted_names = []
    for i in range(len(score_array)):
        if(score_array[i] == second_lowest_score):
            sorted_names.append(names_array[i])
    for val in sorted(sorted_names):
        print(val)

