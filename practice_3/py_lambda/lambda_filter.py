# Here is filter with lambda to get only the todos marked as high priority
tasks = [
    {"title": "Cook dinner", "priority": "High"},
    {"title": "Do coding", "priority": "Medium"},
    {"title": "Clean room", "priority": "High"},
]
high_priority = list(filter(lambda t: t["priority"] == "High", tasks))
print(high_priority)