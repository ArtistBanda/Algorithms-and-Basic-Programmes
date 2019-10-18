#include <iostream>
using namespace std;

struct node
{
    int value;
    node *next;
    node *prev;
};

node *createNode(int value)
{
    node *n1 = new node;
    n1->value = value;
    n1->next = NULL;
    n1->prev = NULL;
    return n1;
}

class DoublyLinkedList
{
    node *head;

public:
    DoublyLinkedList() { head = NULL; }
    void insertBeginning(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
            head = n1;
        else
        {
            n1->next = head;
            head->prev = n1;
            head = n1;
        }
    }
    void insertEnd(int value)
    {
        node *n1 = createNode(value);
        if (head == NULL)
            head = n1;
        else
        {
            node *ptr = head;
            while (ptr->next != NULL)
                ptr = ptr->next;
            ptr->next = n1;
            n1->prev = ptr;
        }
    }
    void insertMiddle(int value, int loc)
    {
        node *n1 = createNode(value);
        if (head == NULL)
            head = n1;
        else
        {
            node *cur_ptr = head, *prev_ptr = head;
            for (int i = 0; i < loc; i++)
            {
                prev_ptr = cur_ptr;
                cur_ptr = cur_ptr->next;
            }
            prev_ptr->next = n1;
            n1->prev = prev_ptr;
            n1->next = cur_ptr;
            cur_ptr->prev = n1;
        }
    }
    void deleteFirst()
    {
        node *temp = head;
        head = head->next;
        head->prev = NULL;
        free(temp);
    }
    void deleteMiddle(int delVal)
    {
        node *ptr = head;
        while (ptr->value != delVal)
            ptr = ptr->next;
        ptr->prev->next = ptr->next;
        ptr->next->prev = ptr->prev;
        free(ptr);
    }
    void deleteEnd()
    {
        if (head == NULL)
        {
            cout << "UnderFlow\n";
            return;
        }
        node *ptr = head;
        while (ptr->next != NULL)
            ptr = ptr->next;
        node *temp = ptr;
        ptr->prev->next = NULL;
        free(ptr);
    }
    void displayAll()
    {
        node *ptr = head;
        if (head == NULL)
        {
            cout << "UnderFlow\n";
            return;
        }
        while (ptr != NULL)
        {
            cout << ptr->value << "->";
            ptr = ptr->next;
        }
        cout << endl;
    }
};

int main()
{
    DoublyLinkedList DLL;
    DLL.insertBeginning(1);
    DLL.insertBeginning(2);
    DLL.insertBeginning(3);
    DLL.displayAll();
    DLL.insertEnd(4);
    DLL.insertEnd(5);
    DLL.displayAll();
    DLL.insertMiddle(6, 2);
    DLL.displayAll();
    DLL.deleteFirst();
    DLL.deleteEnd();
    DLL.displayAll();
    DLL.deleteMiddle(6);
    DLL.displayAll();
    return 0;
}