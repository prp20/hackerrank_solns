def get_average_marks(arr, qname):
    average = 0
    for key, value in arr.items():
        if(key == qname):
            average = sum(value)/len(value)
    return average

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(get_average_marks(student_marks, query_name)))