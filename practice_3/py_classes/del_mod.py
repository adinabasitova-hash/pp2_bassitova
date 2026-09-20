# Here is a class that deletes and modifies its own properties
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

t = Task("Buy groceries")
t.done = True
print(t.title, t.done)
del t.done