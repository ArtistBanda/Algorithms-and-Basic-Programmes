#include <iostream>
using namespace std;

class node
{
    int value;
    node *next;
};

node *createNode(int value)
{
    node *n1 = new node;
    n1->value = value;
    n1->next = NULL;
    return n1;
}

class LinkedList
{
    node *head;

public:
    LinkedList() { head = NULL; }
    void insertBeginning(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            return;
        }
        n1->next = head;
        head = n1;
    }
    void insertEnd(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            return;
        }
        node *ptr = head;
        while (ptr->next != NULL)
            ptr = ptr->next;
        ptr->next = n1;
    }
    void insertBetween(int value, int loc)
    {
        node *n1 = createNode(value);
        if (head == NULL)
        {
            head = n1;
            return;
        }
        node *prev_ptr = head, *cur_ptr = head;
        for (int i = 1; i <= loc; i++)
        {
            prev_ptr = cur_ptr;
            cur_ptr = cur_ptr->next;
        }
        prev_ptr->next = n1;
        n1->next = cur_ptr;
    }
    void deleteBeginning()
    {
        node *temp;
        if (head == NULL)
            cout << "UnderFlow\n";
        else
        {
            temp = head;
            head = head->next;
            free(temp);
        }
    }
    void deleteMiddle(int delValue)
    {
        if (head == NULL)
        {
            cout << "UnderFlow\n";
            return;
        }
        else
        {
            node *temp1 = head, *temp2 = head;
            while (temp1->value != delValue)
            {
                if (temp1->next == NULL)
                {
                    cout << "value node found\n";
                    return;
                }
                temp2 = temp1;
                temp1 = temp1->next;
            }
            temp2->next = temp1->next;
            free(temp1);
        }
    }
    void deleteEnd()
    {
        if (head == NULL)
            cout << "UnderFlow\n";
        else
        {
            node *temp1 = head, *temp2 = head;
            if (head->next == NULL)
            {
                head = NULL;
                free(temp1);
                return;
            }
            while (temp1->next != NULL)
            {
                temp2 = temp1;
                temp1 = temp1->next;
            }
            temp2->next = NULL;
            free(temp1);
        }
    }
    void displayAll()
    {
        if (head == NULL)
            cout << "UnderFlow";
        else
        {
            node *ptr = head;
            while (ptr != NULL)
            {
                cout << ptr->value << "->";
                ptr = ptr->next;
            }
            cout << endl;
        }
    }
};

int main()
{
    LinkedList L;
    L.insertBeginning(2);
    L.insertBeginning(1);
    L.displayAll();
    L.insertEnd(3);
    L.insertEnd(4);
    L.insertBetween(5, 2);
    L.displayAll();
    L.deleteBeginning();
    L.deleteEnd();
    L.displayAll();
    L.deleteMiddle(3);
    L.displayAll();
    return 0;
}
