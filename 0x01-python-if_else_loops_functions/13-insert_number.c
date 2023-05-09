#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(lisint_t **head, int number)
{

	
    listint_t *new_node;
    listint_t *current;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;
    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }
    current = *head;
    while (current->next != NULL)
    {
        if (current->n > number)
        {
            new_node->next = current;
            *head = new_node;
            return (new_node);
        }
        if (current->next->n > number)
        {
            new_node->next = current->next;
            current->next = new_node;
            return (new_node);
        }
        current = current->next;
    }
    current->next = new_node;
    return (new_node);
}
