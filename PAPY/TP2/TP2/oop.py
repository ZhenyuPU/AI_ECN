import argparse
from pathlib import Path


class Generate:
    def __init__(self, path):
        self.path = Path(path)
        self.branch = '│   '
        self.tee = '├── '

    def print_dirtree(self, dir_only=False, level=0, length_limit=1000):
        if length_limit == 0 or level > length_limit:
            return

        if not self.path.exists():
            return
        if level <= 1:
            print(self.tee * level + self.path.name + '/')
        else:
            print(self.branch * (level-1) + self.tee + self.path.name + '/')

        for item in self.path.iterdir():
            item_path = self.path / item
            if item_path.is_dir():
                sub_path = Generate(item_path)
                sub_path.print_dirtree(dir_only, level+1, length_limit-1)
            else:
                print(self.branch * level + self.tee + str(item.name))
        return

def main():
    parser = argparse.ArgumentParser(description="Display file tree.")
    parser.add_argument("path", help="Path to the directory or file to display.")
    args = parser.parse_args()

    file_tree_viewer = Generate(args.path)
    file_tree_viewer.print_dirtree()

if __name__ == "__main__":
    main()
