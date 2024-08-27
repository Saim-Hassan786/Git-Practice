list1 = ["Khabib","Islam","Poirer","Pareira","Jones","Olivera"]
print(f"The number 1 pound for pound fighter is the World is {list1[1]}")
print(f"The Goats of UFC are {list1[0]} and {list1[4]}")
print(f"Best Boxer in the UFC is {list1[2]}")
print(f"The greatest comeback of all time is given by {list1[3]}")
print(f"The most vicious striker in the World of UFC is {list1[3]}")

list0 = []
while True:
    user_input = input("Enter A Number ")
    if user_input == "":
        break
    x = int(user_input)
    list0.append(x)
print(list0)

def get_last_number(lst):
    print(lst[-1])
list3 = [12,34,67,89,8,34,89,3,89,34,89,34,90,5,90,45,8,5,8,5647,44,978234,8078070,242343]
get_last_number(list3)
