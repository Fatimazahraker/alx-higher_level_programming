#include "lists.h"

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <stddef.h>

/**
 * reverse_listint - linkeclist reversed
 * @head: head
 * Return: pointer
 */

void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - check palindrome
 * @head: head
 * Return: 1 if true or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
