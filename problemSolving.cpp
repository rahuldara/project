
#include<iostream>
# include <math.h>
using namespace std;
void Solution(int arr[], int arr_size)
{
    int l, r, min_sum, sum, min_l, min_r;
	if(arr_size < 2)
	{
		cout<< "enter valid array";
		return;
	}

	min_l = 0;
	min_r = 1;
	min_sum = arr[0] + arr[1];
	
	for(l = 0; l < arr_size - 1; l++)
	{
		for(r = l + 1; r < arr_size; r++)
		{
		sum = arr[l] + arr[r];
		if(abs(min_sum) > abs(sum))
		{
			min_sum = sum;
			min_l = l;
			min_r = r;
		}
		}
	}
	cout << "The two elements whose sum is close to zero are "<< arr[min_l] << " " << arr[min_r];
}


int main()

{
int arr_size;
cout<<"ente array size";
cin>>arr_size;
int arr[arr_size];
for(int i=0;i<arr_size;i++){
	cout<<"Enter the elements";
	cin>>arr[i];
}
  Solution(arr, arr_size);
	return 0;
}
