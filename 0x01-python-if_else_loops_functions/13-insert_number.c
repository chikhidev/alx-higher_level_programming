#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: head
 * @number: number
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return NULL;

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return new;
	}

	while (runner->next != NULL && runner->next->n < number)
		runner = runner->next;

	new->next = runner->next;
	runner->next = new;

	return new;
}

