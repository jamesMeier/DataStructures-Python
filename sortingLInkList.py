class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:

    def __init__(self):
        self.start = None
    # is empty

    def display_list(self):
        if self.start is None:
            print('list is empty')
            return
        else:
            print("list is :    ")
            p = self.start
            # start at first link
            while p is not None:
                print(p.info, "", end='')
                # print the information side of the node
                p = p.link
                # p now points at the next node
                # and repeat until hitting th final node
            print()
            # displays list
    #

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("number of nodes in list: ", n)

    def search(self, x):
        position = 1
        # START at 1 and then increment with each p.link
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is at postion", position)
                # before returning we print this message to indicate where x is
                return True
                # we check each node to see if the info is equal to x
                # and return
                position += 1
                p = p.link
        else:
            print(x, "not found in list")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter number of nodes : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print("not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # if list is empty
        if self.start is None:
            print("list is empty")
            return
        # if x is first node new node is to inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        # find reference to predecessor of node containg x
        p = self.start
        while p is not None:
            if p.link.info == x:
                break
            p = p.link
        if p is None:
            print("not present in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p = self.start
        i = 1
        while i < k and p is not None:  # find k-1 reference
            p = p.link
            i += 1
        if p is None:
            print("can only insert upto position", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("list is empty")
            return
            # delete first node
        if self.start.info == x:
            self.start = self.start.link
            return

        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print("element", x, "not in list")
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):

        if self.start is None:
            return

        # if list is only one node
        if self.start.link is None:
            self.start = None
            return

        # find reference of second last node
        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        #prev is none
        prev = None
        #p refers to the next node
        p = self.start
        #while p is not equal to none run this loop
        while p is not None:
            #next refers to the the node 1 kth position up form p
            next = p.link
            #p.link is now equal to none
            p.link = prev
            #prev is now equal to p which is the node we're currently on
            prev = p
            #p = next so we move p onto the next node we're referring to
            p = next
            #we now repeat this process until p.link becomes none/therefore next none/ p then becomes none
            #p will then become none ending the loop

        #start will then point to prev which is the last node we iterated on making it the new first node.
        self.start = prev

    def bubble_sort_exdata(self):
        #initialise our end
        end = None
        #the outer while loop corresponds to a pass of the bubblesort
        #this outer loop stops when end refers to the second node in the list
        while end != self.start.link:
            #this is what happens in a pass of the bubble sort

            #taken a reference p and initialised it to start
            p=self.start
            #this inner loop runs until p.link become equal to end
            while p.link!=end:
                #each iteration q becomes p.link(refering to the node after to p)
                q=p.link
                #comparing the values of p & q/ if p is greater than q then ----
                if p.info>q.info:
                    #---- swap these values
                    p.info,q.info=q.info,p.info
                #after each iteration we are moving p forward
                p=p.link
            #at the end of each iteration this end reference is assigend a new value that becomes our new end of unsorted elements
            end = p

    def bubble_sort_exlinks(self):
        end = None
        while end != self.start.link:
            #extra reference r that will always be behind reference p
            r = p = self.start
            while p.link != end:
                q=p.link
                if p.info>q.info:
                    #change postions of the nodes referred to by p and q// and we need the extra reference r
                    p.link = q.link
                    q.link = p
                    #if p is not the first node then ---
                    if p!=self.start:
                        #-- r link refers to q
                        r.link=q
                    #if p refers to first node we have to update start
                    else:
                        #and make it the the node that is referred to by q
                        self.start = q
                    #exchange values of p & q
                    p,q= q,p
                #set up the next pass
                r=p
                p=p.link
            end = p

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort_rec(self, listStart):
        pass

    def _divide_list(self, p):
        pass

################################################################################


list = SingleLinkedList()

list.create_list()

while True:
    print("1.Display")
    print("2.count number of nodes")
    print("3.Search for element")
    print("4.insert in empty/beginning of list")
    print("5.insert node at end")
    print("6.insert node after specified node")
    print("7.insert node before specified node")
    print("8.insert node at given position")
    print("9.Delete first node")
    print("10.delete last node")
    print("11.delete any node")
    print("12.reverse the list")
    print("13.bubble sort by exchanging data")
    print("14.bubble sort by exchanging links")
    print("15.MergeSort")
    print("16. insert cycle")
    print("17. detect cycle")
    print("18. remove cycle")
    print("19. quit")

    option = int(input("Enter choice: "))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("enter element to be searched : "))
        list.search(data)
    elif option == 4:
        data = int(input("enter element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("enter element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("enter element to be inserted : "))
        x = int(input("enter element after which to insert : "))
        list.insert_after(data, x)
    elif option == 7:
        data = int(input("enter element to be inserted : "))
        x = int(input("enter element before which to insert : "))
        list.insert_before(data, x)
    elif option == 8:
        data = int(input("enter element to be inserted : "))
        k = int(input("enter the position at which to insert : "))
        list.insert_at_position(data, k)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        data = int(input("enter element to be deleted : "))
        list.delete_node(data)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.MergeSort()
    elif option == 16:
        data = int(input("enter element at which cycle has to be inserted : "))
        list.insert_cycle(data)
    elif option == 17:
        if list.has_cycle():
            print("list has cycle")
        else:
            print("list hasn't a cycle")
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("wrong option")
    print()
