#include <iostream>
using namespace std;

struct node
{
    int value;
    node *left, *right;
};

node *createNode(int value)
{
    node *newNode = new node;
    newNode->value = value;
    newNode->left = newNode->right = NULL;
    return newNode;
}

node *insertBST(node *root, int value)
{
    if (root == NULL)
    {
        return createNode(value);
    }
    if (value < root->value)
        root->left = insertBST(root->left, value);
    else
        root->right = insertBST(root->right, value);
}

void printPreoder(node *root)
{
    if (root == NULL)
        return;
    cout << root->value << ' ';
    printPreoder(root->left);
    printPreoder(root->right);
}

void printInorder(node *root)
{
    if (root == NULL)
        return;
    printInorder(root->left);
    cout << root->value << ' ';
    printInorder(root->right);
}

void printPostorder(node *root)
{
    if (root == NULL)
        return;
    printPostorder(root->left);
    printPostorder(root->right);
    cout << root->value << ' ';
}

int main()
{
    node *root;
    root = insertBST(root, 4);
    insertBST(root, 2);
    insertBST(root, 1);
    insertBST(root, 3);
    insertBST(root, 4);
    insertBST(root, 5);
    insertBST(root, 6);
    printInorder(root);
    return 0;
}