/* Class Code @ https://algs4.cs.princeton.edu/15uf/ */

import java.util.Scanner;


public class UF {

	// private int count;




	/* Constructor */
	public UF(int n) {

	}
	// public int find (int p) {

	// }
	// public int count() {
	// 	return count;

	// }
	// public boolean connected(int p, int q) {
	// 	return find(p) == find(q);
	// }



	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);

		System.out.println("Set the data structure size: ");
		int N = input.nextInt(); // user gives the number of objects
		UF uf = new UF(N); // initialize union-find array/tree with N objects 

		while (input.hasNext()) {
			// System.out.println("The first object: ");
			int p = input.nextInt();
			// System.out.println("The second object: ");
			int q = input.nextInt();

			// // only if p and q are not already connected, union them
			// if (!uf.connected(p, q)) {  
			// 	uf.union(p, q);
			// 	System.out.println(p + " " + q);
			// }
		}
	}
}