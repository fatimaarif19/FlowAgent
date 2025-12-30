def reflect(tasks, status):
  pending = []
  for task in tasks:
    name = task["task"]
    if status.get(name) == "pending":
        pending.append(name)

    if pending:
       return f"{len(pending)} tasks are pending..Time to drop reminders."
    
    return "All tasks are on track!!"
    