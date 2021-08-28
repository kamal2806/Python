class Node:
    def _init_(self,value):
        self.data = value
        self.next = None
    
    
class LL:
    def _init_(self):
        self.head = None


    def add (self, value):
        # create a new node
        new_node = Node(value)

        #point to head
        new_node.next = self.head

        #reasign head
        self.head = new_node


    def add_tail(self,value):

        new_node = Node(value)

        if self.head is None:
            self.head =  new_node
        else:
            temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node


    def add_after(self,after,value):

        temp = self.head

        while temp is not None:
            if temp.data == after:
                break
            temp = temp.next

        if temp is None:
            print("Not found")
        else:
            new_node= Node(value)

        new_node.next = temp.next
        temp.next = new_node


    def remove_tail(self):
        if self.head is None:
            print("List empty")
        else:
            temp = self.head
        if temp.next is None:
            self.head = None
        else:
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None


    def remove_head(self):
        if self.head  is None:
            print("Empty")
        else:
            self.head = self.head.next


    def remove(self,value):

        if self.head.data == value:
            return self.remove_head()

        temp = self.head  

        while temp.next is not None:
            if temp.next.data == value:
                break
            temp = temp.next

        if temp.next is None:
            print("Not there")
        else:
            temp.next = temp.next.next                                    


    def traverse(self):

        temp = self.head
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next


    def search(self,value):

        temp = self.head
        pos = 0

        while temp is not None:
            if temp.data == value:
                return pos
            pos+=1
            temp = temp.next


        return "Not found"


    def replace_max(self,value):

        max = self.head
        temp = self.head

        while temp is not None:
            if temp.data> max.data:
                max = temp
            temp = temp.next

        max.data = value

    def sumAlternateNode(head):
        count = 0
        sum = 0
        while (head != None):
            if (count % 2 != 0):
                sum = sum + head.data
            count = count + 1
            head = head.next
        return sum      


    def reverse(self):

        prev_node = None
        curr_node = self.head

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node


    def change_sentence(self):

        temp = self.head

        while temp is not None:

            if temp.data == '*'or temp.data =='/':
                temp.data = ' '

            if temp.next.data == '*' or temp.next.data == '/':
                temp.next.next.data = temp.next.next.data.upper()
                temp.next = temp.next.next

            temp = temp.next