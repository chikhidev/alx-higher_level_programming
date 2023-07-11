#!/usr/bin/python3
''' Module: 1-my_list
'''


class MyList(list):
    ''' Represents MyList
    '''

    def print_sorted(self):
        '''
        prints the list
        '''
        print(sorted(self))
