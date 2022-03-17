#include <stdio.h>

int i=0;
int c2d(char*);
int dhm(char*);
void sort(int[][2]);
void swap(int*, int*);

int main()
{
	FILE *ifp, *ofp;
	int res, timestamp[50][2], n, j, cnt, h, m;
	char t[8];
	
	/*
	Open file(a.txt) as read mode and return 1 if it's NULL
	*/
	ifp=fopen("a.txt", "r");
	if(ifp==NULL)
	{
		printf("input file open error!\n");
		return 1;
	}
	
	/*
	Open file(b.txt) as write mode and return 1 if it's NULL
	*/
	ofp=fopen("b.txt", "w");
	if(ofp==NULL)
	{
		printf("output file open error!\n");
		return 1;
	}
	
	/*
	Reads number plate(6 digit numbers) and the time stamp(day:hour:minute) that says when it entered and exited the parking lot from text file a.txt
	And gets two dimensional array whose first column is number plate and second column is the interval between enter time and exit time
	*/
	while(1)
	{
		res=fscanf(ifp, "%6d %s", &n, t);
		if(res==EOF)
		{
			break;
		}
		
		cnt=0;
		for(j=0;j<i;j++)
		{
			if(timestamp[j][0]==n)
			{
				cnt=1;
				break;
			}
		}
		
		if(cnt)
		{
			timestamp[j][1]=dhm(t)-timestamp[j][1];
		}
		else
		{
			timestamp[i][0]=n;
			timestamp[i][1]=dhm(t);
			i++;
		}
	}
	
	/*
	Calculate fee by hour(1000won/1hour)
	If People who stayed for more than 72hours, add a fine of 15000won along with their fee
	*/
	for(j=0;j<i;j++)
	{
		h=timestamp[j][1]/60;
		m=timestamp[j][1]%60;
		
		if(h>72 || (h==72 && m!=0))
		{
			timestamp[j][1]=15000+h*1000;
		}
		else
		{
			timestamp[j][1]=h*1000;
		}
	}
	
	/*
	Sort in descending order of cost
	*/
	sort(timestamp);
	
	/*
	Print the number plate and total amount of fee(fine included) and currency in descending order separated by tab at the output file(b.txt)
	*/
	for(j=0;j<i;j++)
	{
		fprintf(ofp, "%d\t%d\twon\n", timestamp[j][0], timestamp[j][1]);
	}
	
	/*
	Close files
	*/
	fclose(ifp);
	fclose(ofp);
	
	return 0;
}

/*
This function converts an int to string
@param
-t: The pointer which points to the string value to be converted

@return
-The function returns the 'int' value converted from the string value pointd by parameter 't'
*/
int c2d(char *t)
{
	return *t-'0';
}

/*
This function converts form of timestamp from 'day:hour:minute' to 'minute'
@param
-t: The pointer which points to the string value written as 'day:hour:minute'form to be converted

@return
-Calculate 1day/(24hour*60minute) and 1hour/60minute
-The function returns the 'int' value converted from the string value pointd by parameter 't'
*/
int dhm(char *t)
{
	return (c2d(t)*10+c2d(t+1))*24*60+(c2d(t+3)*10+c2d(t+4))*60+(c2d(t+6)*10+c2d(t+7)); 
}

/*
This function sorts array by examining two adjacent elements
@param
-t: Two dimensional array which has two columns

@return
-The function sorts the two dimensional array in descending order by value in second column
-No exact return value (void function)
*/
void sort(int t[][2])
{ 
	int p, q;
	
	for(p=0;p<i;p++)
	{
		for(q=0;q<i-1;q++)
		{
			if(t[q][1]<t[q+1][1])
			{
				swap(&t[q][0], &t[q+1][0]);
				swap(&t[q][1], &t[q+1][1]);
			}
		}
	}
	
	return;
}

/*
This function swaps two parameters
@param
-a: The pointer which points to the int value to be swapped with other parameter
-b: The pointer which points to the int value to be swapped with other parameter

@return
-The function swaps two parameters with each other
-No exact return value (void function)
*/
void swap(int *a, int *b)
{
	int temp;
	
	temp=*a;
	*a=*b;
	*b=temp;
	
	return;
}
