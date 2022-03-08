

if __name__ == '__main__':
    no_of_input_elements = int(input())
    input_array = set(list(map(int, input().split())))
    no_of_cases = int(input())
    task_cases_array = []
    for _ in range(no_of_cases):
        task, value = input().split()
        task_array = list(map(int, input().split()))
        task_cases_array.append(task)
        task_cases_array.append(int(value))
        task_cases_array.append(task_array)
    for i in range(len(task_cases_array)):
        if(str(task_cases_array[i])):
            if(task_cases_array[i] == "intersection_update"):
                input_array.intersection_update(task_cases_array[i+2])
            elif(task_cases_array[i] == "update"):
                input_array.update(task_cases_array[i+2])
            elif(task_cases_array[i] == "symmetric_difference_update"):
                input_array.symmetric_difference_update(task_cases_array[i+2])
            elif(task_cases_array[i] == "difference_update"):
                input_array.difference_update(task_cases_array[i+2])
    print(sum(input_array))
