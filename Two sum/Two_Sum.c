//Two sum 
#include<stdio.h>
int main()
{
    int n=7;
    int arr[]={1, 5, 7, 10, 13, 18, 22};
    int x=18,res=0;
    int l=0,r=n-1;
    while(l<=r)
    {
        if(arr[l]+arr[r]==x)
        {
            res=1;
            break;
        }
        else if(arr[l]+arr[r]<x)
            l++;
        else
            r--;
    }
}