import java.util.Scanner;
import java.io.File; // file io class 

public class QuickUnionUF
{
	// Properties
	private int[] id; 
	private int size;

	// constructor
	public QuickUnionUF(int n)
	{
		size = n;
		id = new int[n];

		for (int i = 0; i < size; i++)
			id[i] = i;
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

	public void union(int p, int q)
	{
		int child = root(p);
		int parent = root(q);

		id[child] = parent;
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

		while (input.hasNext()) 
		{
			int p = input.nextInt(); // reading two pairs of objects 
			int q = input.nextInt();
			System.out.println(p + " " + q);

			quuf.union(p, q);
		}
		System.out.println("---------------");
		System.out.println(quuf.toString());

		// find whether two numbers are connected
		System.out.println("---------------");
		System.out.println(quuf.toString(3, 8));
		System.out.println(quuf.toString(1, 8));
		System.out.println(quuf.toString(6, 7));

	}
}