/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Testing the randomized queue class implementation: read in 
 *  strings from a file, enqueue each string to a RandomizedQueue, then use an
 *  iterator to return k random items in the queue. 
 ******************************************************************************/

import java.util.Iterator;
import edu.princeton.cs.algs4.StdIn;

public class Permutation {
    public static void main(String[] args) {
        int k = Integer.parseInt(args[0]);
        RandomizedQueue<String> rq = new RandomizedQueue<String>();
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            rq.enqueue(s);
        }
        Iterator<String> it = rq.iterator();
        for (int i = 0; i < k; i++) {
            System.out.println(it.next());
        }
    }
}