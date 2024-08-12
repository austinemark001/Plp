my_list = []

for i in range(1,4):
    my_list.append(i * 10)

another_list = [50, 60, 70]
my_list.extend(another_list)

my_list.sort(key=None)

for i in my_list:
    if i == 30:
        print(i)
        