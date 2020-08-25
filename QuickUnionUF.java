import java.util.Scanner;
import java.io.File; // file io class 

public class QuickUnionUF
{
	// Properties
	private int[] id; 
	private int size;
	private int [] height;


	// constructor
	public QuickUnionUF(int n)
	{
		id = new int[n];
		size = n;
		height = new int[n];

		for (int i = 0; i < size; i++)
		{
			id[i] = i;
			height[i] = 1;
		}
	}

	public int root(int i)
	{
		// traverse up in the tree until to find id[i]==i
		while (id[i] != i)
			i = id[i]; // entry i is parent node of id[i]

		return i;
	}

	public boolean find(int p, int q)
	{
		return root(p) == root (q);
	}

	// Version 2: 
	// avoid problem of creating deep tree
	public void union(int p, int q)
	{
		int rootp = root(p);
		int rootq = root(q);

		// when two number are not connected already
		if (rootp != rootq)
		{
			if (height[rootp] < height[rootq]) // when p is smaller tree
			{	
				id[rootp] = rootq; // root of p gets attached to root of q
				height[rootq] += height[rootp]; // reflect the size increase of the bigger tree
			}
			else // when q is smaller tree or same as p
			{
				id[rootq] = rootp; // root of q gets attached to root of p
				height[rootp] += height[rootq];
			}
		}
	}

	// Version 1: union O(N), find O(N)
	// public void union(int p, int q)
	// {
	// 	int child = root(p);
	// 	int parent = root(q);

	// 	id[child] = parent;
	// }


	//toString method
	public String toStringId()
	{
		String output = "id = [";

		for (int i = 0; i < size; i++)
			output += id[i] + ", ";

		output += "]";

		return output;
	}

	public String toStringHeight()
	{
		String output = "height = [";

		for (int i = 0; i < size; i++)
			output += height[i] + ", ";

		output += "]";

		return output;
	}

	public String toString(int p, int q)
	{
		String output = "Are " + p + " and " + q + " connected? ";
		output += find(p, q);

		return output;
	}



	public static void main(String[] args) throws Exception
	{
		Scanner input = new Scanner(new File(args[0]));
		
		int n = input.nextInt();
		QuickUnionUF quuf = new QuickUnionUF(n); // creat QuickUnionUF object

		System.out.println(quuf.toStringHeight());

		while (input.hasNext()) 
		{
			int p = input.nextInt(); // reading two pairs of objects 
			int q = input.nextInt();
			System.out.println(p + " " + q);

			quuf.union(p, q);
		}
		System.out.println("---------------");
		System.out.println(quuf.toStringId());
		System.out.println(quuf.toStringHeight());


		// find whether two numbers are connected
		System.out.println("---------------");
		System.out.println(quuf.toString(3, 8));
		System.out.println(quuf.toString(1, 8));
		System.out.println(quuf.toString(6, 7));

	}
}