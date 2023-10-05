import os
import os.path


class Generate:
    def __init__(self, path):
        self.path = path
        self.branch = '│   '
        self.tee = '├── '

    def print_dirtree(self, dir_only=False, level=0, length_limit=1000):
        if length_limit == 0 or level > length_limit:
            return

        if not os.path.exists(self.path):
            return
        
        if level <= 1:
            print(self.tee * level + os.path.basename(self.path) + '/')
        else:
            print(self.branch * (level-1) + self.tee + os.path.basename(self.path) + '/')
       
        # 判断是否存在目录

        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isdir(item_path):
                sub_path = Generate(item_path)
                sub_path.print_dirtree(dir_only, level+1, length_limit-1)
            else:
                print(self.branch * level + self.tee + item)
        return


if __name__ == '__main__':
    path = "E:\Centrale Nantes\AI\A2\PAPY\TP2"
    g = Generate(path)
    g.print_dirtree()
