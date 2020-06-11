/* Class Code @ https://algs4.cs.princeton.edu/15uf/ */

import java.util.Scanner;
import java.io.File; // file io class 



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



	public static void main(String[] args) throws Exception {
		
		Scanner input = new Scanner(new File(args[0])); //get file name from command-line argument (Execution: java UF input.txt)

		int N = input.nextInt(); // user gives the number of objects
		UF uf = new UF(N); // creating UF object; initialize union-find array/tree with N objects 

		while (input.hasNext()) {
			int p = input.nextInt(); // reading two pairs of objects 
			int q = input.nextInt();

			// // only if p and q are not already connected, union them
			// if (!uf.connected(p, q)) {  
				// uf.union(p, q);
				// System.out.println(p + " " + q);
			// }
		}
	}
}