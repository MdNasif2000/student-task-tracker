from task_manager import TaskManager
class Main:
    
    def show_menu(self):
        print("\n", "Student Task Tracker".center(30, "="), "\n")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
    def run(self):
        manager = TaskManager()
        while True:
            self.show_menu()
            choice =input("\nEnter Your Choice : ")
            
            if choice not in ["1","2","3","4","5"]:
                print("\nInvalid Choice ! Please Choose Between (1-5)")
                continue
            if choice == "5":
                manager.save_to_file()
                if manager.tasks_list:
                    print("***Tasks Saved !***")
                    break
                break

            if choice == "1":
                manager.add_task()
                manager.save_to_file()

            if choice == "2":
                manager.view_task()
                manager.save_to_file()
                
            if choice == "3":
                manager.update_task()
                manager.save_to_file()
                
            if choice == "4":
                manager.delete_task()
                manager.save_to_file()
    
    
student1 = Main()
student1.run()