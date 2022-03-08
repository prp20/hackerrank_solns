n = int(input());
dic = {} 
for x in input().split():
  dic[x] = dic.get(x,0) + 1
  print(dic)
for key in dic:
  if dic[key] != n: 
      print(key)
      break