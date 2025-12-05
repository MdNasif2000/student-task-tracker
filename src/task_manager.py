from task import Task
import json
import datetime

class TaskManager:
    def __init__(self, filename = "tasks.json"):
        self.filename = filename
        self.tasks_list =[]
        self.load_from_file()

    def add_task(self):
        print("\nAdding New Task-")
        while True:
            title = input("Enter Your Title: ").strip()
            if title:
                break
            print("Title Can't Be Empty!\n")
        while True:
            description = input("Enter Description : ").strip()
            if description:
                break
            print("Description Can't Be Empty !\n")
        task = Task(title,description)
        self.tasks_list.append(task)
        print("\nTask Added Successfully ! ")

    def view_task(self):
        if not self.tasks_list:
            print("\nNo Saved Task !")
            return
        print("\n","All Tasks".center(30,"="))
        for task in self.tasks_list:
            print(f"\nID : {task.id}")
            print(f"Title : {task.title}")
            print(f"Description : {task.description}")
            print(f"Created At : {task.created_at}")
            if task.updated_at is not None:
                print(f"Updated At : {task.updated_at}\n")
        print("_"*30)
            
    def update_task(self):

        if not self.tasks_list:
            print("\nNo Task Found To Update !")
            return

        print("\nUpdating Task -")
        task_id = self.get_task_id("Enter The Task ID You want To Update : ")
        task = self.find_task_id(task_id)
        
        if task is None:
            print("\nTask Not Found ! ")
            return
        new_title = input(f"Enter new title (Leave Blank To Keep Current ) : ").strip()
        new_description = input(f"Enter new description (Leave Blank To Keep Current ) : ").strip()
        
        updated = False
        if new_title:
            task.title = new_title
            updated = True
        
        if new_description:
            task.description = new_description
            updated = True
            
        if updated:    
            task.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        print("\nTask Updated Successfully !") 
    
    def delete_task(self):
        if not self.tasks_list:
            print("\nNo Task Found To Delete !")
            return
        
        print("\nDeleting Task -")
        task_id = self.get_task_id("Enter The Task ID You Want To Delete : ")
        task = self.find_task_id(task_id)
        
        if task is None:
            print("\nTask Not Found ! ")
            return
        
        # self.tasks_list.remove(task)
        # print("\nTask Deleted Successfully ! ")    
        while True:
            confirm_input = input("\nConfirm Delete? (y/n) : ").lower()
            if confirm_input == "y" or confirm_input == "yes":
                self.tasks_list.remove(task)
                print("\nTask Deleted Successfully ! ")
                break
            elif confirm_input == "n" or confirm_input == "no":
                break
            else:
                print("Invalid Input ! Enter A Valid Option.")    
    def save_to_file(self):
        try:            
            with open(self.filename,"w") as file:
                data = [task.obj_to_dict() for task in self.tasks_list]
                json.dump(data,file, indent =4 )

        except Exception as e:
            print("\nError Saving Task : ",e)
        
    
    def load_from_file(self):
        try:
            with open(self.filename,"r") as file:
                data = json.load(file)
                self.tasks_list= [Task.dict_to_obj(task) for task in data]

        except FileNotFoundError:
            self.tasks_list =[]
            
        except json.JSONDecodeError:
            self.tasks_list =[]
            
    def find_task_id(self,task_id):
        for task in self.tasks_list:
            if task_id== task.id:
                return task
        return None
    
    def get_task_id(self,prompt):
        while True:
            try:
                task_id = int(input(prompt))
                return task_id
            except:
                print("\nInvalid Input ! Enter A Valid Task ID.")
                continue