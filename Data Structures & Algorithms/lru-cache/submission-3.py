class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(-2, -2)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lookup = {}
        self.capacity = capacity        

    def get(self, key: int) -> int:
        print('-------------')
        node = self.lookup.get(key)
        if not node:
            return -1
        print('get:', node.key, '=>', node.value)

        self.isolate_node(node)

        self.add_node_end(node)
                
        self.printL()
        print('-------------')
        return node.value
        
    def printL(self):
        temp = self.head
        arr = ['HEAD']
        while temp:
            if temp.value > 0:
                arr.append(temp.value)
            temp = temp.next
        arr.append('TAIL')
        print()
        print(arr)
    
    def isolate_node(self, node):
        print('before isolation', self.printL())
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        print('after isolation', self.printL())
        return node


    def add_node_end(self, node):
        end_node = self.tail.prev
        end_node.next = node
        node.prev = end_node
        self.tail.prev = node
        node.next = self.tail
        return

    def del_node(self):
        del_node = self.head.next
        self.head.next = del_node.next
        del_node.next.prev = self.head
        return del_node

    def put(self, key: int, value: int) -> None:
        if key in self.lookup.keys():
            print('duplicate', key, '=>', value)
            node = self.lookup.get(key)
            self.isolate_node(node)
            self.add_node_end(node)
            node.value = value
            return

        node = Node(key, value)
        self.lookup[key] = node        
        print('put', key, '=>', value)

        self.printL()
        self.add_node_end(node)
        self.printL()

        if self.capacity > 0:
            self.capacity -= 1
        else:
            del_node = self.del_node()
            self.printL()
            print(self.lookup)
            k = del_node.key
            print('k=',k)
            del self.lookup[k]

        
        print(self.lookup)
        return

