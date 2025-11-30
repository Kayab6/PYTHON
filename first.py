# print("hello kavya")
# print("this is LOQ  ")

# for i in range(10):
#     print(i)

# li=[10,20,230,40]
# li.append(10)
# print(li)


# TO DO LIST 

print("the todo list ")
task=[]
def menu():
    print("1, CREATE NEW TASK")
    print("2, DELETE A TASK")
    print("3, VIEW TASKS")
    print("4, EXIT")
# if choice ==1;
#     add_task()
def add_task():
    tell=input("enter ur task:")
    task.append(tell)
    print(task)


def view_tasks():
    if len(task)==0:
        print("no tasks yet")

    else:
        i=0
        while i<len(task):
            print(str(i+1),"."+task[i])
            i=i+1
            

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
