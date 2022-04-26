
num_dict = {}
def search(num):
    for i in num:
        if num_dict.get(i):
            num_dict[i] += 1
        else: 
            num_dict[i] = 1
    print(num_dict)

search(num = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1])

# num_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
# print(num_list.count(1))
# print(num_list.count(2))
# print(num_list.count(3))
# print(num_list.count(4))





