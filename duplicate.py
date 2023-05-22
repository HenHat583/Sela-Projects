lst = ["banana", "banana", "epic", "speedrun", "speedrun", "purple"]
def list_duplicate_delete(lst):
    return list(set(lst))
print(list_duplicate_delete(lst))