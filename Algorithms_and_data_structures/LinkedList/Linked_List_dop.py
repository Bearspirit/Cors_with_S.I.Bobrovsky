from Linked_List import *

def Linked_summ(L1, L2):
    if (L1.len() == L2.len()) and L1.len() != 0:
        sum_list = []
        node_L1 = L1.head
        node_L2 = L2.head
        while node_L1 is not None:
            sum_list.append(node_L1.value + node_L2.value)
            node_L1 = node_L1.next
            node_L2 = node_L2.next
        return sum_list
    else:
        return None
