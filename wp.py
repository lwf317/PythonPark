import os

def main2():
    WORKING_PATH = os.path.dirname(os.path.abspath('__file__')).replace("\\", "/")
    print WORKING_PATH
    PARENT_PATH = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir)).replace("\\", "/")
    print PARENT_PATH


def main():
    to_be_removed = []
    try:
        with open("exclude_list.txt", "r") as fd:
            items = fd.read().splitlines()
            for item in items:
                to_be_removed.append(item + ".csv")
    except IOError:
        print "No exclude_list.txt exist, no camera is pre-selected to be removed."

    print to_be_removed


if __name__ == "__main__":
    main()