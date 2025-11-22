def task():
    tasks = []
    print("Welcome to Task Manager Please choose your task:")

    total_tasks = int(input("Enter number of tasks you want to add: "))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter the name of task {i} : ")
        tasks.append(task_name)

    print(f"Your Today's Tasks Are :\n{tasks}")

    while (True):
        operation = int(input("1. Add Task\n2. Update Tasks \n3. View Tasks \n4. Exit\nChoose an operation: "))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.")

        elif operation == 2:
            updated_tasks = input("Enter the task number you want to update: ")
            if updated_tasks in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(updated_tasks)
                tasks[ind] = up
                print(f"Task updated successfully to '{up}'.")

        elif operation == 3:
            print(f"Your Today's Tasks Are :\n{tasks}")    

        elif operation == 4:            
            print("Exiting the Task Manager. Have a great day!")            
        break
            
task()