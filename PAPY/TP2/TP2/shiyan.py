import os

def print_dirtree(path, dir_only=False, level=0, length_limit=1000):
    space =  '    '
    branch = '│   '
    tee =    '├── '
    last =   '└── '
    if level >= length_limit:
        return
    
    path = os.path.dirname(os.path.abspath(path))
    print(path)
    if os.path.exists(path):
        if os.path.isdir(path):
            print(tee * level + os.path.basename(path) + "/")
            if not dir_only:
                for item in os.listdir(path):
                    if os.path.isdir(item):
                        print(branch * level + tee + item + "/")
                        #dir_only = True
                        item_path = item + "/"
                        print_dirtree(item_path, dir_only, level + 1, length_limit)
                    else:
                        print(branch * level + tee + item)
                    return
            #else:
                #print(branch * level + tee + path)
                #return

# 例子用法：
# 打印 "foo" 目录下的文件和目录树，仅显示目录，深度限制为2，最大行数限制为10
filename = "TP2/"
path = os.path.dirname(os.path.abspath(filename))
print_dirtree(filename, dir_only=False, level=0, length_limit=10)
