#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - ftn to check if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0 and 1 if there is.
 * 
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
   	 listint_t *fast = list;

   	 while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return 1;
        }
    }

    return 0;

}
