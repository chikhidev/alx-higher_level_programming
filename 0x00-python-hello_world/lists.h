#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: integer
* @next: points to the next node
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

/*
 * _realloc - realloc
 * @ptr: ptr
 * @old_size: old size
 * @new_size: new size
 * Return: void
 */

void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
