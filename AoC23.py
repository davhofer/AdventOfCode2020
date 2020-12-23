class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        nodes.append(node.data)
        node = node.next
        while node is not self.head:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

input = "2 4 7 8 1 9 3 5 6"
t_input = "3 8 9 1 2 5 4 6 7"
n = 10000000

cups = LinkedList()
current = None
onenode = None
for i in input.split(' '):
    if cups.head == None:
        cups.head = Node(i)
        current = cups.head
    else:
        current.next = Node(i)
        current = current.next
    if i == '1':
        onenode = current
for i in range(10,1000001):
    current.next = Node(str(i))
    current = current.next
current.next = cups.head
current = cups.head



def sm(i):
    return (i-1)%9+1

for i in range(n):
    #print(cups)
    # if i%100000 == 0:
    #     print(i)
    print(i)
    extract = current.next
    start = current
    current.next = current.next.next.next.next
    destination = str(sm(int(current.data)-1))
    extr_values = [int(extract.data),int(extract.next.data),int(extract.next.next.data)]
    min1 = int(destination)
    if int(destination) in extr_values:
        if sm(int(destination)-1) in extr_values:
            if sm(int(destination)-2) in extr_values:
                destination = str(sm(int(destination)-3))
            else:
                destination = str(sm(int(destination)-2))
        else:
            destination = str(sm(int(destination)-1))
    while current.data != destination:
        current = current.next
    endpoint = current.next
    current.next = extract
    current.next.next.next.next = endpoint
    current = start.next

#print(cups)
print(onenode.data)
print(onenode.next.data)
print(onenode.next.next.data)
