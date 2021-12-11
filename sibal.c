#include <stdio.h>
#include <stdlib.h>

typedef struct Node *nPtr;
struct Node {
    int value;
    nPtr next;
};

void print(nPtr list);

int main()
{
    nPtr n1 = malloc(sizeof *n1);
    nPtr n2 = malloc(sizeof *n2);

    n1->value = 4;
    n1->next = n2;
    n2->value = 5;
    n2->next = NULL;

    print(n1);
    return 0;
}

void print(nPtr list)
{
    nPtr p;
    p = list;
    while (p != NULL)
    {
        printf("%d ", p->value);
        p = p->next;
    }
}

/*
#include <stdio.h>
#include <stdlib.h>

typedef struct node *nptr;
typedef struct node{
	int data;
	nptr link;
} NODE;

void Insert(nptr*,int);
void PrintAll(nptr);

nptr head;

int main()
{
	int i, A[10]={3,9,8,2,5,10,7,1,4,6};
	
	head=NULL;
	
	for(i=0;i<10;i++)
	{
		Insert(head,A[i]);
	}
	
	PrintAll(head);
	
	nptr temp;
	temp=head;
	while(temp!=NULL)
	{
		head=head->link;
		free(temp);
		temp=head;
	}
	
	return 0;
}

void Insert(nptr *pPre, int n)
{
	nptr pNew=(nptr)malloc(sizeof(nptr));
	pNew->data=n;
	pNew->link=NULL;
	
	if(pPre==NULL)
	{
		head=pNew;
	}
	else
	{
		nptr temp=head;
		while(temp->link!=NULL)
		{
			temp=temp->link;
		}
		temp->link=pNew;
	}
	
	return;
}

void PrintAll(nptr head)
{
	nptr p;
    p = head;
    while (p != NULL)
    {
        printf("%d ", p->data);
        p=p->link;
    }
	printf("\n");
	
	return;
}


*/
