class MyGraph:
    def __init__(self):     # Corrected constructor
        self.MyGraph = {}  #where we'll store the graph
        self.visited = []  #to keep track of the nodes i have already visited
        self.queue = []

    def add_edge(self, node, neighbors): #node is the node you want to add
        self.MyGraph[node] = neighbors   #neighbors is a list of nodes that are connected to this node

    def bfs(self, start_node):           #start_node is the node where BFS will begin
        self.visited.append(start_node)
        self.queue.append(start_node)

        while self.queue:
            m = self.queue.pop(0)
            print(m, end=" ")

            for neighbour in self.MyGraph[m]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour) #adds the neighboring node to the queue so it will be processed next

x = MyGraph()

# Adding edges to the graph
x.add_edge('3', ['4', '6'])
x.add_edge('4', ['1', '4'])
x.add_edge('6', ['8'])
x.add_edge('1', [])
x.add_edge('4', ['8'])
x.add_edge('8', [])

print("The BFS is : ")
x.bfs('3')


