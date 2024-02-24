import sys  #Importing the sys module for system-specific functionality. Just in case TaskMaster decides to take over the world one operating system at a time.
import time  #Importing the time module to add some time-related flair to our assistant. Because even digital task assistants need a sense of timing.

class TaskMaster:
    def __init__(self):
        self.tasks = []  #Initializing an empty list to store tasks. TaskMaster's brain is as empty as this list before you fill it with tasks.

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display. Add some tasks to your list!")  #"Come on, give me something to do!"
        else:
            print("Your Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully! The TaskMaster approves!")  #TaskMaster giving you a virtual pat on the back for being productive.

    def edit_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f"Task {index} edited to '{new_task}'! TaskMaster is pleased with your edit!")  #"Nice job, you're learning!"

        else:
            print("Invalid task index. Please provide a valid index. TaskMaster is confused!") 

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f"Task '{deleted_task}' deleted successfully! TaskMaster is on a cleaning spree!")  #TaskMaster feeling like Marie Kondo, tidying up your task list.

        else:
            print("Invalid task index. Please provide a valid index. TaskMaster cannot delete thin air!") 

    def run(self):
        print("Welcome to TaskMaster - Your Digital Task Assistant!")
        time.sleep(1)  #Adding a small delay for dramatic effect. Because TaskMaster likes to make an entrance.

        while True:
            print("\nWhat would you like to do?")
            print("1. Display Tasks")
            print("2. Add Task")
            print("3. Edit Task")
            print("4. Delete Task")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task = input("Enter the task you want to add: ")
                self.add_task(task)
            elif choice == '3':
                index = int(input("Enter the index of the task you want to edit: "))
                new_task = input("Enter the new task: ")
                self.edit_task(index, new_task)
            elif choice == '4':
                index = int(input("Enter the index of the task you want to delete: "))
                self.delete_task(index)
            elif choice == '5':
                print("Thank you for using TaskMaster. Goodbye! TaskMaster bows gracefully.")  #TaskMaster's farewell bow, as elegant as ever.
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5. TaskMaster cannot comprehend gibberish!")  #TaskMaster pretending not to understand when you're being indecisive.

if __name__ == "__main__":
    taskmaster = TaskMaster()
    taskmaster.run()
