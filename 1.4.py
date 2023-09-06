my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
x=0
for i in sorted(my_dict.items(), key = lambda para : para[1]):
    x+=1
    if x > 3:
        print(i)

