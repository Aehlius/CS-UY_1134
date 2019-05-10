import DLL


def flattened_linked_lst(lnk_lst):
    output_lst = DLL.DLL()
    curr_node = lnk_lst._header.next
    while curr_node.next is not None:
        if isinstance(curr_node.data, DLL.DLL):
            temp_lst = flattened_linked_lst(curr_node.data)
            output_lst._trailer.prior.next, temp_lst._header.next.prior = temp_lst._header.next, output_lst._trailer.prior
            output_lst._trailer = temp_lst._trailer
            #temp_node = temp_lst._header.next
            #while temp_node.next is not None:
            #    output_lst.add_tail(temp_node.data)
            #    temp_node = temp_node.next
        else:
            output_lst.add_tail(curr_node.data)
        curr_node = curr_node.next
    return output_lst


if __name__ == '__main__':
    lnk_lst1 = DLL.DLL()
    lnk_lst1.add_head(4)
    elem2 = DLL.DLL()
    elem3 = DLL.DLL()
    elem3.add_head(3)
    elem2.add_head(elem3)
    elem2.add_head(2)
    lnk_lst1.add_head(elem2)
    lnk_lst1.add_head(1)
    lnk_lst2 = flattened_linked_lst(lnk_lst1)
    print (lnk_lst1)
    print (lnk_lst2)