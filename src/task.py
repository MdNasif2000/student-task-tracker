import datetime
import random

class Task:
    used_ids =set()

    def gen_task_id(self):
        while True:
            gen_id = random.randint(100000,999999)
            if gen_id not in Task.used_ids:
                Task.used_ids.add(gen_id)
                return gen_id
    def __init__(self,title,description):
        self.id = self.gen_task_id()
        self.title = title
        self.description = description
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = None
        
    def obj_to_dict(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "created_at" : self.created_at 
            }
        if self.updated_at is not None:
            data["updated_at"] = self.updated_at
        return data    
    @classmethod
    def dict_to_obj(cls,data):
        obj = cls(data["title"],data["description"])
        obj.id = data["id"]
        obj.created_at = data["created_at"]
        obj.updated_at = data.get("updated_at")
        Task.used_ids.add(obj.id)
        return obj
        