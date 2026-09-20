# Here is a function with args and kwargs mixed
def create_task(title, *tags, **details):
    print(f"Task: {title}")
    print(f"Tags: {tags}")
    print(f"Details: {details}")

create_task("Finish homework", "urgent", "school", due="tomorrow", priority="high")