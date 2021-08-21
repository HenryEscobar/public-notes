import logging
import random

# Return the element that is the M away from the end.
#   assume linked list and can't reverse string


def random_list_of_ints(N,max_num=1000):
    return(random.sample(range(1,max_num),N))
    

def find_mth_element(m, input_list):
    max_index=len(input_list)
    if m >= max_index:
        return('nil')
    m_index=max_index - m -1
    print(m_index)
    return(input_list[m_index])
        

if __name__ == '__main__':
    my_list=random_list_of_ints(20)
    print(my_list)

    m=random.randint(0,len(my_list))
    m=19

    counter=-1
    for i in range(0,len(my_list)):
        print("[ {i:3} {m:3} ]   {v}".format(i=i,m=len(my_list)-i, v=my_list[i]))

    mth_element=find_mth_element(m, my_list)
    print("The M-th element {m} for the list is: {ans}\n".format(m=m, ans=mth_element))
    

    
