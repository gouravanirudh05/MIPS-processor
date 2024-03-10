//Binary search
#include<stdio.h>
int main()
{
    int n=7;
    int arr[]={1, 5, 7, 10, 13, 18, 22};
    int ele=13;
    int res=-1;
    int l=0,r=n-1;
    while(l<=r)
    {
        int mid=(l+r)/2;
        if(arr[mid]==ele)
        {
            res=mid;
            break;
        }
        else if(arr[mid]<ele)
            l=mid+1;
        else if(arr[mid]>ele)
            r=mid-1;
    }
}