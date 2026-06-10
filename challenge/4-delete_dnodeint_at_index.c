#include "lists.h"
#include <stdlib.h>

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *saved_head = *head;
    unsigned int i = 0;

    if (*head == NULL)
        return (-1);

    while (saved_head != NULL && i < index)
    {
        saved_head = saved_head->next;
        i++;
    }

    if (saved_head == NULL)
        return (-1);

    if (*head == saved_head)
        *head = saved_head->next;

    if (saved_head->next != NULL)
        saved_head->next->prev = saved_head->prev;

    if (saved_head->prev != NULL)
        saved_head->prev->next = saved_head->next;

    free(saved_head);
    return (1);
}
