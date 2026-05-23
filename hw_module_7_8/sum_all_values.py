import avl

def sum_tree_values(node):
    if node is None:
        return 0
    result = node.key + sum_tree_values(node.left) + sum_tree_values(node.right)
    return result

# checking:
root = None
keys = [20, 15, 35, 80]

for key in keys:
    root = avl.insert(root, key)

total_sum = sum_tree_values(root)
print(f"Sum all tree values: {total_sum}")