#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint - the function prints all elments of a list
 * @h: pointer
 * Return: ...
 */

size_t print_dlistint(const dlistint_t *h)
{
    #include "lists.h"
/**
 * print_dlistint - prints the elements of a list
 * @h: head of the lis
 * Return: number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	unsigned int i = 0;

	if (h == NULL)
		return (i);
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		i++;
	}
	return (i);
}
