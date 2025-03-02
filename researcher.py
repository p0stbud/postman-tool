import os


def _researcher(namespaces):
    path = namespaces.path
    if path:
        print(namespaces.path)
    else:
        path = os.getcwd()
        print(path)
    print('researcher body')