#include "lists.h"

/**
 * check_cycle - check in a list have a loop
 * @list: list
 * Return: 1 is success or 0
 */

int check_cycle(listint_t *list)
{
	listint_t *chain1, *chain2;

	if (!list)
	{
		return (0);
	}
	chain1 = list;
	chain2 = list->next;
	while (chain1 && chain2 && chain2->next)
	{
		if (chain1 == chain2)
		{
			return (1);
		}
		chain1 = chain1->next;
		chain2 = chain2->next->next;
	}
	return (0);
}
