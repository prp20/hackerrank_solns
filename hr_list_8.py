if __name__ == '__main__':
    n1 = int(input())
    eng_news = list(map(int, input().split()))
    n2 = int(input())
    french_news = list(map(int, input().split()))
    setval = set(eng_news)
    print(len(setval.symmetric_difference(french_news)))