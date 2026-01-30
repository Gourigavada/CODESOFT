# TASK - 1 Creating TodoList using python programing Language

def task():


    tasks = [] #empty list

    print("WELCOME TO THE TASK MANAGEMENT APP")

    total_task = int(input("Enter how many task you want to add = ")) 

    for i in range(1, total_task+1):
      task_name =input(f"Enter task {i} = ") 
      tasks.append(task_name)
      
    print(f"Today's tasks are\n {tasks}")
    
    while True:
       #Adding Task
       operations = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
       if operations == 1:

          add = input("Enter task you want to add = ")
          tasks.append(add)
          print(f"Task {add} has been successfully added...")

       elif operations == 2:
            #Update Task
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
               up = input("Enter new task = ")
               ind = tasks.index(updated_val) #2
               tasks[ind] = up
            print(f"Updated task {up}")
           
           #Delete Task
       elif operations == 3:
         del_val = input("Which task you want to delete = ")
         if del_val in tasks:
            ind = tasks.index(del_val)
            del_tasks = [ind]
            print(f"Task {del_val} has been deleted...")

         #view The Task
       elif operations == 4:
        print(f"Total tasks {tasks}")
       
       elif operations == 5:
          print("Closing the program....")
          break
    else: 
     print("invalid input....")

task()