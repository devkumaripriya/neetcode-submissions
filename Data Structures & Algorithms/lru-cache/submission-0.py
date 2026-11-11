class Node:

    def __init__(self, key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:       

    def __init__(self, capacity: int) -> int:
        self.capacity = capacity
        self.cache={}

        #Dummy head and tail
        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head
    #Remove a node from the linked list
    def remove(self,node):
        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node

    # Add node just after head
    def add(self,node):
        node.prev=self.head
        node.next = self.head.next

        self.head.next.prev=node
        self.head.next=node
    
    #Get value
    def get(self,key:int)->int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        #Mark as recently used'
        self.remove(node)
        self.add(node)

        return node.value
    #Insert or update value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.cache[key]=node
        self.add(node)

        if len(self.cache)>self.capacity:
            #Remove least recently used nodes
            lru=self.tail.prev
            self.remove (lru)
            del self.cache[lru.key]

