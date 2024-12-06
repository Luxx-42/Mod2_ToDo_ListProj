toDo = []
completed_tasks = []

def add_task():
    ''' Adds a task to the to-do list '''
    add_T = input("What task would you like to add? (Enter 'none' if nothing): ").strip()

    if add_T.lower() == 'none':
        return
    else:
        toDo.append(add_T)
        print(f"\n'{add_T}' has been added to the list.")

def view_task():
    ''' Prints out a view of the to-do list. '''
    if not toDo:
        print("Your to-do list has nothing in it.")
        add_2_addTask = input("would you like to add to it? (enter yes or no): ").lower()
        if add_2_addTask == 'yes':
            add_task()
        else:
            return
    else:
        print("Your to-do list to get done:")
        for num, task in enumerate(toDo, start=1):
            print(f"{num}. {task.capitalize()}")

def task_complete():
    ''' Adds a comleted task to the completed task list from user input '''
    while True:
        try:
            if not toDo:
                print("\nThere's nothing in your to-do list.")
                add_task()
                return

            print("\nYour current tasks:")
            for num, task in enumerate(toDo, start=1):
                print(f"{num}. {task.capitalize()}")

            ask_which1 = int(input("\nWhat task did you complete? Enter a number (If none, enter '0'): ")) - 1

            if ask_which1 == -1:
                return
            if 0 <= ask_which1 < len(toDo):
                task_comp = toDo.pop(ask_which1)
                completed_tasks.append(task_comp)
                print(f"\nYou have completed '{task_comp.capitalize()}'.")
                print("\nHere is your completed list:")
                for numb, tasck in enumerate(completed_tasks, start=1):
                    print(f"Completed {numb}. {tasck.capitalize()}")
                return
            else:
                print("\nInvalid task number. Please try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def del_task():
    '''Deletes a task from the to-do list.'''
    if not toDo:
        print("\nNothing is in your list.")
        add_2_addTask = input("Would you like to add to it? (Enter 'yes' or 'no'): ").lower()
        if add_2_addTask == 'yes':
            add_task()
        else:
            return

    while True:
        try:
            print("\nYour present tasks:")
            for num, task in enumerate(toDo, start=1):
                print(f"{num}. {task.capitalize()}")

            delete_tsk = int(input("\nEnter the task number to delete: "))-1
            
            if 0 <= delete_tsk < len(toDo):
                deleted_tsk = toDo.pop(delete_tsk)
                print(f"\nTask '{deleted_tsk.capitalize()}' has been deleted.")
                return
            else:
                print("incorrect task number. Try again.")
        except ValueError:
            print("\nIncorrect input. Enter a valid number.")

print("\nWelcome to the To Do list app!")

while True:
    print("\n--------------------------------")
    print("Here is you list of options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    try:
        ask_user = int(input("\nWhat would you like to do? Enter a number: "))
        if ask_user == 1:
            add_task()
        elif ask_user == 2:
            view_task()
        elif ask_user == 3:
            task_complete()
        elif ask_user == 4:
            del_task()
        elif ask_user == 5:
            print("Thanks for making your to do list!")
            break
    except ValueError:
            print("Please enter a number between 1 and 5.")