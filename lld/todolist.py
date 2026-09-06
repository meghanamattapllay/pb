class Task:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.done=False

    def complete(self):
        self.done=True

    def pending(self):
        self.done=False

    def update(self,name):
        self.name=name

    def show(self):
        status="Done" if self.done else "Pending"
        print(self.id,self.name,status)


class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.tasks=[]

    def add_task(self,name):
        task=Task(len(self.tasks)+1,name)
        self.tasks.append(task)
        print("Task added")

    def delete_task(self,id):
        for task in self.tasks:
            if task.id==id:
                self.tasks.remove(task)
                print("Task deleted")
                return
        print("Task not found")

    def complete_task(self,id):
        for task in self.tasks:
            if task.id==id:
                task.complete()
                print("Task completed")
                return
        print("Task not found")

    def pending_task(self,id):
        for task in self.tasks:
            if task.id==id:
                task.pending()
                print("Task marked pending")
                return
        print("Task not found")

    def update_task(self,id,name):
        for task in self.tasks:
            if task.id==id:
                task.update(name)
                print("Task updated")
                return
        print("Task not found")

    def search_task(self,name):
        found=False
        for task in self.tasks:
            if name.lower() in task.name.lower():
                task.show()
                found=True
        if not found:
            print("Task not found")

    def show_all(self):
        if not self.tasks:
            print("No tasks")
            return
        for task in self.tasks:
            task.show()

    def show_pending(self):
        for task in self.tasks:
            if not task.done:
                task.show()

    def show_completed(self):
        for task in self.tasks:
            if task.done:
                task.show()


class TodoApp:
    def __init__(self):
        self.users=[]

    def add_user(self,user):
        self.users.append(user)

    def show_users(self):
        for user in self.users:
            print(user.id,user.name)


app=TodoApp()
user=User(1,"Meghana")
app.add_user(user)

while True:
    print("\n--- TODO LIST ---")
    print("1.Add Task")
    print("2.Delete Task")
    print("3.Complete Task")
    print("4.Mark Pending")
    print("5.Update Task")
    print("6.Search Task")
    print("7.Show All Tasks")
    print("8.Show Pending Tasks")
    print("9.Show Completed Tasks")
    print("10.Exit")

    choice=int(input("Enter choice: "))

    if choice==1:
        name=input("Enter task: ")
        user.add_task(name)

    elif choice==2:
        id=int(input("Enter task id: "))
        user.delete_task(id)

    elif choice==3:
        id=int(input("Enter task id: "))
        user.complete_task(id)

    elif choice==4:
        id=int(input("Enter task id: "))
        user.pending_task(id)

    elif choice==5:
        id=int(input("Enter task id: "))
        name=input("Enter new task: ")
        user.update_task(id,name)

    elif choice==6:
        name=input("Enter task name: ")
        user.search_task(name)

    elif choice==7:
        user.show_all()

    elif choice==8:
        user.show_pending()

    elif choice==9:
        user.show_completed()

    elif choice==10:
        print("Thank you")
        break

    else:
        print("Invalid choice")