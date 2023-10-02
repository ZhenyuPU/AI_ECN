import os

def print_dirtree(directory, dir_only=False, level=float('inf'), length_limit=1000, indent=''):
    if level == 0 or length_limit == 0:
        return
    
    if not os.path.exists(directory):
        return

    print(indent + os.path.basename(directory) + '/')
    indent += '├── '

    if dir_only:
        items = [item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))]
    else:
        items = os.listdir(directory)

    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if length_limit > 0:
                print_dirtree(item_path, dir_only, level - 1, length_limit - 1, indent)
            else:
                print(indent + '... (too many items)')
                break
        else:
            print(indent + item)

# Exemple d'utilisation
filename = "TP2/"
path = os.path.dirname(os.path.abspath(filename))
print_dirtree(filename)
