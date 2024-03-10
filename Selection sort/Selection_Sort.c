//Selection sort
#include<stdio.h>
int main()
{ 
    int n=7;
    int arr[]={-2,2,5,1,4,3,-1};
    for(int i=0;i<n-1;i++)
    {
        int minindex=i;
        for(int j=i+1;j<n;j++)
            if(arr[j] < arr[minindex])
                 minindex=j;
        if( minindex!=i)
        {
            int temp=arr[minindex];
            int temp1=arr[i];
            arr[i]=temp;
            arr[minindex]=temp1;
        }
    }
}