#include "lists.h"
#include <stdio.h>

int check_palindrome(int *list_of_int, int stop);


/* OTHER VERSION OF THIS EXO | SAME TIME AND SPACE COMPELEXITY */
/*
* THIS ONLY DIFF IS THAT AN ARRAY IS USE TO COMPARE IS THIS IS A
* PALYNDROME
*/

/*
* THAT STORE IN THE MEMORY 4 TIMES N BYTES (WHERE N IS THE NUMBER
* OF ELEM IN THE LINKED LIST
*/

/*
* SIMPLE WAY TO WRITE AND UNDERSTAND AND OLSO USABLE IS THE LINKED
* LIST IS SHORT
*/


/**
* is_palindrome - Check if a given linked-list is a palindrome or not
*
* @head: The given linked list
*
* Return: 0 if not, 1 if it
*/
int is_palindrome(listint_t **head)
{
	listint_t *browse = *head;
	int *int_from_list = NULL;
	int len_list = 0, i = 0;

	if (browse == NULL)
		return (1);
	while (browse != NULL)
	{
		len_list++;
		browse = browse->next;
	}

	int_from_list = malloc(sizeof(int) * len_list);
	if (!int_from_list)
		return (0);
	browse = *head;
	while (browse != NULL)
	{
		int_from_list[i] = browse->n;
		browse = browse->next;
		i++;
	}
	return (check_palindrome(int_from_list, i));
}


/**
* check_palindrome - Check if a array of number is a palindrome or not
*
* @list_of_int: The list of number to check
* @stop: The end of the list
*
* Return: 0 is not, 1 if it.
*/
int check_palindrome(int *list_of_int, int stop)
{
	int j, middle = (stop / 2);

	for (j = 0, stop -= 1; j < middle; j++, stop--)
	{
		if (list_of_int[j] != list_of_int[stop])
		{
			free(list_of_int);
			return (0);
		}
	}
	free(list_of_int);
	return (1);
}
