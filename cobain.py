file = open("receiver_list.txt", "r")
for i in file:
    i = i.replace("\n", "")
    print(i.split(" "))