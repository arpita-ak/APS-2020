#include<stdio.h>
#include<stdlib.h>

typedef struct bst
{
    int data;
    struct bst *left;
    struct bst *right;
}BST;

BST *insert_bst(BST *root)
{
    BST *newnode;
    newnode=(BST *)malloc(sizeof(BST));
    if(newnode==NULL)
    {
        printf("Memory failed\n");
        return root;
    }
    printf("Enter tree data\n");
    scanf("%d",&newnode->data);
    newnode->left=NULL;
    newnode->right=NULL;

    if(root==NULL)
    {
        return newnode;
    }
    BST *prev=NULL,*curr=root;
    while(curr!=NULL)
    {
        prev=curr;
        if(curr->data > newnode->data)
           curr=curr->left;
        else
            curr=curr->right;
    }
    if(prev->data > newnode->data)
        prev->left=newnode;
    else
        prev->right=newnode;
    return root;
}

void inorder(BST *root)
{
    if(root!=NULL)
    {
        inorder(root->left);
        printf("%d ",root->data);
        inorder(root->right);
    }
}

BST *delete_bst(BST *root)
{
    if(root==NULL)
    {
        printf("Empty tree\n");
        return root;
    }
    int data;
    printf("Enter delete item\n");
    scanf("%d",&data);

    BST *parent,*curr,*succ,*p;
    curr=root;
    parent=NULL;
    while(curr!=NULL && curr->data!=data)
    {
        parent=curr;
        if(curr->data > data)
            curr=curr->left;
        else
            curr=curr->right;
    }
    if(curr==NULL)
    {
        printf("Item not found\n");
        return root;
    }

    if(curr->left==NULL)
       p=curr->right;
    else if(curr->right==NULL)
        p=curr->left;
    else
    {
        succ=curr->right;
        while(succ->left!=NULL)
            succ=succ->left;

        succ->left=curr->left;
        p=curr->right;
    }

    if(parent==NULL)
    {
        free(curr);
        return p;
    }

    if(p==curr->left)
        parent->left=p;
    else
        parent->right=p;

    free(curr);
    return root;
}


int main()
{
    BST *root=NULL;
    int choice;
    do
    {
        printf("\n1->Insert\n2->Delete\n3->Inorder traversal\n4->Exit\n");
        printf("Enter choice\n");
        scanf("%d",&choice);
        switch(choice)
        {
          case 1:
                 root=insert_bst(root);
                 break;
          case 2:
                 root=delete_bst(root);
                 break;
          case 3:
                 inorder(root);
                 break;
          case 4:
                break;
          default:
              printf("Enter the valid choice\n");
        }
    }while(choice!=4);
}
