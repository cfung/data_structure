
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    /*
    Start raversing through the array using binary search.
    Follow the steps below:
    i. Take two pointers low and high with low at oth index and high at n-1th index.
    ii. Go for middle element, if it matches with the key, then sucess, else, check if the middle element is greater of less than the key.
    iii. If middle element is less than key, then low will be jumped to mid+1, and high will remain same.
    iv. If middle element is greater than key, then low will remain same and high will come down to mid-1.
    Steps in 2 will continue till element is found or low <= high.
    If element is found, print 1, else print -1.
    */
    static int search(int arr[], int n, int x)  
    {  
        int start = 0;
        int end = n - 1;
        while (start <= end) {
            
            int mid = (start + end) / 2;
            //System.out.println("what is mid.." + mid);
            if (arr[mid] == x) {
                return mid;
            }
            else if (arr[mid] < x) {
                start = mid + 1;
            } 
            else if (arr[mid] > x){
                end = mid - 1;
            }
            
        }
        
        // return -1 if the element is not found  
        return -1;  
    }  
	public static void main (String[] args) throws IOException {
		//code
		int[] arr = new int[10000000];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		
		StringBuffer sb = new StringBuffer();
		
		while (t > 0)  
        {  
  
            // to read multiple integers line  
            String line = br.readLine();  
            String[] strs = line.trim().split("\\s+");  
            
            int numArray = Integer.parseInt(strs[0]);
            int numSearch = Integer.parseInt(strs[1]);
        
            String arrayLine = br.readLine();
            String[] strs2 = arrayLine.trim().split("\\s+"); 
            
            // Input the array  
            for (int i = 0; i < numArray ; i++)  
                arr[i] = Integer.parseInt(strs2[i]);  
  
            // Input the element to be searched  
            //int x = Integer.parseInt(br.readLine());  
  
            // Compute and print result  
            sb.append(search(arr, numArray, numSearch)+"\n"); 
  
            t--;  
        } 
          
        System.out.print(sb); 
	}
}