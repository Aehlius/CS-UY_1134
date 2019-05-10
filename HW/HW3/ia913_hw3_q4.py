# the following two functions and class have been imported from Resources under NYU Classes

def list_duplicate(L):
    # this function creates a duplicate of a singly linked list
    if L is None:
        return None

    result = Node(L.data)
    last = result
    cursor = L.next

    while cursor is not None:
        last.next = Node(cursor.data)
        last = last.next
        cursor = cursor.next

    return result


# the list_print function is used entirely for test coding and has no effect on
# CompactString class outside of the main function


def list_print(L):
    if L is None:
        print('< >')
        return
    result = ['<']

    # while L.next is not None:
    while L is not None:
        result.append(str(L.data))
        L = L.next

    result.append('>')
    print(' '.join(result))


class Node:
    """
    Node: the basic object used for building linked lists.
    This version is for singly linked lists
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# code for problem 4

class CompactString:
    def __init__(self, orig_str=None):
        if orig_str is None:
            # if there is no input, the compact string is simply None
            self.comp_str = None
        else:
            # otherwise, a series of nodes is created in order to store the string
            # the letter is represented as letter, and number of time it appears is value
            letter = orig_str[0]
            value = 0
            compact_list = None
            for i in range(len(orig_str)):
                if orig_str[i] == letter:
                    value += 1
                else:
                    string_tuple = (letter, value)
                    if compact_list is None:
                        compact_list = Node(string_tuple)
                        cursor = compact_list
                    else:
                        cursor.next = Node(string_tuple)
                        cursor = cursor.next
                    letter = orig_str[i]
                    value = 1
            string_tuple = (letter, value)
            cursor.next = Node(string_tuple)
            self.comp_str = compact_list

    def __add__(self, other):
        if self is None:
            # if the first value is empty, we can simply return a copy of the second linked list
            return list_duplicate(other.comp_str)
        else:
            # otherwise, both linked lists are copied and joined
            result = CompactString()
            result.comp_str = list_duplicate(self.comp_str)
            node = result.comp_str
            other_nodes = list_duplicate(other.comp_str)
            while node.next.next is not None:
                node = node.next
            last_node = node.next
            if last_node.data[0] != other_nodes.data[0]:
                # if the last node of first list and first node of second list are not same, we can simply joine
                last_node.next = other_nodes
            else:
                # otherwise, the function needs to combine the values of two nodes so as to unify them
                letter = last_node.data[0]
                value = last_node.data[1] + other_nodes.data[1]
                node.next = Node((letter, value), other_nodes.next)
        return result

    def __lt__(self, other):
        # this function returns a True if self is lexicographically smaller than other
        node = self.comp_str
        other_node = other.comp_str
        # setting initial characters and their number of appearances
        left_char = node.data[0]
        left_val = node.data[1]
        right_char = other_node.data[0]
        right_val = other_node.data[1]
        while left_char == right_char:
            if left_val == right_val:
                # continues to check only if both sequences of same letter are equal in length
                if node.next is not None or other_node.next is not None:
                    # and if there is more values to check
                    # by updating the char and vals
                    node = node.next
                    other_node = other_node.next
                    left_char, right_char = node.data[0], other_node.data[0]
                    left_val, right_val = node.data[1], other_node.data[1]
            elif left_val < right_val:
                # if the values are different, then the next value of shorter sequence is checked
                # against curr val of longer one
                return node.next.data[0] < right_char
            else:
                return left_char < other_node.next.data[0]
        if node.next is not None and other_node.next is not None:
            # if the characters are different, then they are compared
            return left_char < right_char
        if node.next is None and other_node.next is None:
            # if one of the strings ended earlier, then the longer string is lexicographically larger
            return False
        elif node.next is not None:
            return True
        else:
            # if both strings are completed, then they are equal, and thus self is not smaller than other
            return False

    def __eq__(self, other):
        # this function checks if two strings are equal in lexicographical value
        node = self.comp_str
        other_node = other.comp_str
        # setting initial character and value variables
        left_char = node.data[0]
        left_val = node.data[1]
        right_char = other_node.data[0]
        right_val = other_node.data[1]

        while left_char == right_char and node.next is not None and other_node.next is not None:
            # the loop checks as long as both characters are equal in character and there is a node to check
            if left_val == right_val:
                node = node.next
                other_node = other_node.next
                left_char, right_char = node.data[0], other_node.data[0]
                left_val, right_val = node.data[1], other_node.data[1]
            else:
                # if the values of two strings are different, then they are not equal
                return False
        if node.next is None and other_node.next is None:
            # if one string has more nodes while the other concluded, they are not equal
            return True
        else:
            return False

    def __str__(self):
        # this function returns the string representation of self
        output = ''
        cursor = self.comp_str
        while cursor is not None:
            # the loop runs until it runs out of nodes to add to the output
            output += cursor.data[0] * cursor.data[1]
            cursor = cursor.next
        return output


# Test code


if __name__ == '__main__':
    my_string = CompactString('aaaaabbbaaa')
    list_print(my_string.comp_str)
    other_string = CompactString('aaaaaaacccaaaa')
    list_print(other_string.comp_str)
    final_string = my_string + other_string
    list_print(final_string.comp_str)
    print(my_string > other_string)
    print(other_string > my_string)
    print(my_string == other_string)
    other_string = CompactString('aaaaabbbaaa')
    print(my_string == other_string)
    print(my_string)
    print(other_string)