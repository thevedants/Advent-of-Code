def generate_sublists(lst):
    sublists = []
    
    # Iterate over the list and create sublists by excluding one element at a time
    for i in range(len(lst)):
        sublist = lst[:i] + lst[i+1:]  # Exclude the element at index i
        sublists.append(sublist)
    
    return sublists

# Example usage:
lst = [1, 2, 3, 4]
result = generate_sublists(lst)
print("Sublists:", result)