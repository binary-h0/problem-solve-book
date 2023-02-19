import sys
input = sys.stdin.readline
n = int(input().rstrip())

def preorderSearch(graph, root):
    if root == '.':
        return
    print(root, end='')
    preorderSearch(graph, graph[root][0])
    preorderSearch(graph, graph[root][1])

def inorderSearch(graph, root):
    if root == '.':
        return
    inorderSearch(graph, graph[root][0])
    print(root, end='')
    inorderSearch(graph, graph[root][1])

def postorderSearch(graph, root):
    if root == '.':
        return
    postorderSearch(graph, graph[root][0])
    postorderSearch(graph, graph[root][1])
    print(root, end = '')

if __name__ == '__main__':
    graph = dict()
    graph['.'] = []
    for _ in range(n):
        root, r, l = map(str, input().rstrip().split())
        graph[root] = []
        graph[root].append(r)
        graph[root].append(l)
    preorderSearch(graph, 'A')
    print()
    inorderSearch(graph, 'A')
    print()
    postorderSearch(graph, 'A')
