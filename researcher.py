import os


def researcher_tool(namespaces):
    path = namespaces.path
    if path:
        print(namespaces.path)
    else:
        path = os.getcwd()
        print(path)
    print('researcher body')