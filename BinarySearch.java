import java.util.Arrays;

public class BinarySearch 
{
	// // this class should not be instantiated
	// private BinarySearch (){ }

	public static int binarySerch (int[] l, int find)
	{
		int lower = 0;
		int upper = l.length - 1;
		
		while (lower <= upper)
		{	
			int mid = lower + ((upper - lower) / 2);
			System.out.println("(" + lower + "," + upper + "," + mid + ")" );

			if (find == l[mid])
				return mid;


			if (find < l[mid])
				upper = mid - 1;
			if (find > l[mid])
				lower = mid + 1;

		}

		// when Find doesn't exist in the L
		return -1;
	}

	public static String toString(int[] a)
	{
		String output = "a = [";

		for (int i = 0; i < a.length; i++)
			output += a[i] + ", ";

		output += "]";

		return output;
	}
	
	public static void main(String[] args)
	{
		// int[] a = new int[]{1, 3, 4, 5, 7, 11, 14, 16}; // even length
		int[] a = new int[]{1, 3, 4, 5, 7, 11, 14, 16, 18}; // odd length

		for (int i = 0; i < 20; i ++)
		{
			System.out.println("i = " + i + " idx = " + binarySerch(a, i));
		}

		/* Items to fix/improve after first design
			1. (0, 7) --> 3, (3, 7) --> 2 // need to add lower
			2. when two indices cross
			3. when mid is already the number I need to find --> stop searching
			4. right side search only, still need to include mid?
			+ recursive
		*/

	} 
}