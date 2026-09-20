# Here is sorted with lambda, sorting tasks by title length
tasks = [
    {"title": "Cook dinner", "priority": "High"},
    {"title": "Do coding", "priority": "Medium"},
    {"title": "Clean room", "priority": "High"},
]

sorted_by_length = sorted(tasks, key=lambda t: len(t["title"]))
print(sorted_by_length)