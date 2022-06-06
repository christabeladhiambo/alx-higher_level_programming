#include "lists.h"
#include <stdio.h>

/**
* reverse_list - Reverse a linked list
*
* @head: The first elem of the elem of the linked list
*
* Return: The new first elem of the reverse linked list (aka the last)
*/
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *cur = *head;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	cur = prev;
	return (cur);
}

/**
* is_palindrome - Check if a given linked-list is a palindrome or not
*
* @head: The given linked list
*
* Return: 0 if not, 1 if it
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;

	if (*head == NULL)
		return (1);

	while (fast->next != NULL && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	slow = reverse_list(&slow);
	fast = *head;

	while (slow && fast)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
return (1);
}
