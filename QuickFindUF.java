import java.util.Scanner;
import java.io.File; // file io class 

public class QuickFindUF
{
	// Properties
	private int[] id; // create array here in order to be accessible accross functions 
	private int size;

	// Constructors 
	public QuickFindUF(int n)
	{
		size = n;
		id = new int[n];

		for (int i = 0; i < n; i++) // initialize an array with N entries, O(N)
			id[i] = i;  // [0, 1, 2, 3, 4, ...]
	}

	public boolean connected(int p, int q) 
	{
		return id[p] == id[q]; // 2 * O(1)
	}

	public void union(int p, int q)
	{
		int idp = id[p];
		int idq = id[q];

		for (int i = 0; i < size; i++)
		{
			if (id[i] == idp) // change all entries that are same with idp to idq
				id[i] = idq;
		}
	}

	//toString method
	@Override
	public String toString()
	{
		String output = "[";

		for (int i = 0; i < size; i++)
			output += id[i] + ", ";

		output += "]";

		return output;
	}



	public static void main(String[] args) throws Exception
	{
		Scanner input = new Scanner(new File(args[0])); //get file name from command-line argument (on terminal: java filename inputfile.txt)

		int n = input.nextInt(); // user gives the number of objects
		QuickFindUF qfuf = new QuickFindUF(n); // creating QuickFindUF object


		while (input.hasNext()) 
		{
			int p = input.nextInt(); // reading two pairs of objects 
			int q = input.nextInt();
			System.out.println(p + " " + q);

			qfuf.union(p, q);
		}
		System.out.println("---------------");

		System.out.println(qfuf.toString());

	}
}