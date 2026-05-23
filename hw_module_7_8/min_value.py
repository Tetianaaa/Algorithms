import avl

def find_min_value(node):
    current = node
    if current is None:
        return None
    while current.left is not None:
        current = current.left

    return current

# checking:
root = None
keys = [25, 15, 40, 8, 12, 25]

for key in keys:
    root = avl.insert(root, key)

min_node = find_min_value(root)

if min_node:
    print(f"MIN value: {min_node.key}")
else:
    print("Empty tree")