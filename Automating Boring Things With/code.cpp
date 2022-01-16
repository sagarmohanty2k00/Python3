#include<bits/stdc++.h>
using namespace std;

vector<int> insertion_sort(vector<int> arr, int n) {
    for (int i=1; i<n; i++) {
        int key = arr[i];
        int j = i;

        while (j > 0 and arr[j-1] > key) {
            arr[j] = arr[j-1];
            j--;
        }

        arr[j] = key;
    }
    
    return arr;
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];    // pivot
    int i = (low - 1);  // Index of smaller element
 
    for (int j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

vector<int> quick_sort(vector<int> arr, int low, int high) {}

int main()
{
    // code here
    vector<int> arr = {5, 4, 4, 3, 2, 1};

    vector<int> arr1 = insertion_sort(arr, 6);

    for (int i: arr1) cout << i << " ";
    cout << endl;
    return 0;
}