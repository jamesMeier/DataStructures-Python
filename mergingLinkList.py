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

    def bubble_sort_exdata(self):
        # initialise our end
        end = None
        # the outer while loop corresponds to a pass of the bubblesort
        # this outer loop stops when end refers to the second node in the list
        while end != self.start.link:
            # this is what happens in a pass of the bubble sort

            # taken a reference p and initialised it to start
            p = self.start
            # this inner loop runs until p.link become equal to end
            while p.link != end:
                # each iteration q becomes p.link(refering to the node after to p)
                q = p.link
                # comparing the values of p & q/ if p is greater than q then ----
                if p.info > q.info:
                    # ---- swap these values
                    p.info, q.info = q.info, p.info
                # after each iteration we are moving p forward
                p = p.link
            # at the end of each iteration this end reference is assigend a new value that becomes our new end of unsorted elements
            end = p
    # Will merge one sorted single link list with this "list2" sorted link list that is sent as an argument

    def merge1(self, list2):
        # allocate new single link list
        merge_list = SingleLinkedList()
        # create a merge list by allocating new nodes
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    # p1 p2 are references to the first nodes of the sorted list that are to be merged
    def _merge1(self, p1, p2):
        # compare p1 & p2 whichever is smaller we allocate a new node in the merged linked list
        if p1.info <= p2.info:
            # start M refers to first node of merged list and is returned form this method
            startM = Node(p1.info)
            # move p1 forward
            p1 = p1.link
        else:
            # do the same with p2 info and p2
            startM = Node(p2.info)
            p2 = p2.link
        # reference pm = to startM now Pm is always the most recent node added to merge list thefore the last node
        pM = startM

        while p1 is not None and p2 is not None:
            # compare info
            if p1.info <= p2.info:
                # and the smaller info, as a node to the end of the merged list
                pM.link = Node(p1.info)
                # move p1 on
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            # move pm on to refer to latest node added to merge list
            pM = pM.link

        # if second list has finished and elements left in first list
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link

        # if second list has finished and elements left in first list
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    def merge2(self, list2):
        # allocate new single link list
        merge_list = SingleLinkedList()
        # create a merge list by allocating new nodes
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        # cretaes first Node of our merge list
        if p1.info <= p2.info:

            startM = p1
            p1 = p1.link

        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                # insert node after pm
                pM.link = p1
                # move both pm and p1 forward
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link
        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

############################################################################################


list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1.create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

print("First line - ")
list1.display_list()
print("second line - ")
list2.display_list()

list3 = list1.merge1(list2)
print("merged list -")
list3.display_list()

print("First line - ")
list1.display_list()
print("second line - ")
list2.display_list()

list3 = list1.merge2(list2)
print("merged list -")
list3.display_list()
print("First line - ")
list1.display_list()
print("second line - ")
list2.display_list()
