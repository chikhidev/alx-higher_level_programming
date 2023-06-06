#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it.
 * @list: list
 * Return: int
 */

int check_cycle(listint_t *list)
{
    listint_t *slow_ptr, *fast_ptr;

    if (list == NULL || list->next == NULL)
        return 0;

    slow_ptr = list;
    fast_ptr = list->next;

    while (slow_ptr != fast_ptr) {
        if (fast_ptr == NULL || fast_ptr->next == NULL) {
            return 0;
        }
        slow_ptr = slow_ptr->next;
        fast_ptr = fast_ptr->next->next;
    }

    return 1;
}
