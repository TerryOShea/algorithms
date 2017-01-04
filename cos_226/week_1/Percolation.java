/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Modeling Percolation using an N-by-N grid and Union-Find data 
 *                structures to determine the threshold. 
 ******************************************************************************/

import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private WeightedQuickUnionUF wquf;
    private boolean[] openArray;
    private int sideLength;
    private int numOpenSites;
    
    // create n-by-n grid with all sites blocked
    public Percolation(int n) {
        if (n <= 0) { 
            throw new java.lang.IllegalArgumentException(); 
        }
        openArray = new boolean[n*n + 2];
        wquf = new WeightedQuickUnionUF(n*n + 2);
        sideLength = n;
        numOpenSites = 0;
        
        openArray[0] = true;
        openArray[n*n + 1] = true;
    }
    
    // open site (row, col) if it is not open already
    public void open(int row, int col) {
        verifyCoords(row, col);
        if (!isOpen(row, col)) {
            int thisIndex = sideLength*(row-1) + col;
            openArray[thisIndex] = true;
            numOpenSites += 1;
            if (row == 1) {
                wquf.union(thisIndex, 0);
            }
            if (row == sideLength) {
                wquf.union(thisIndex, sideLength*sideLength + 1);
            }
            if (row > 1 && isOpen(row-1, col)) { 
                wquf.union(thisIndex, thisIndex - sideLength); 
            }
            if (row <= sideLength - 1 && isOpen(row+1, col)) { 
                wquf.union(thisIndex, thisIndex + sideLength); 
            }
            if (col > 1 && isOpen(row, col-1)) { 
                wquf.union(thisIndex, thisIndex - 1); 
            }
            if (col <= sideLength - 1 && isOpen(row, col+1)) { 
                wquf.union(thisIndex, thisIndex + 1); 
            }
        }
    }
    
    private void verifyCoords(int row, int col) {
        if (row < 1 || col < 1 || row > sideLength || col > sideLength) {
            throw new java.lang.IndexOutOfBoundsException();
        }
    }
    
    // is site (row, col) open?
    public boolean isOpen(int row, int col) {
        return openArray[sideLength*(row-1) + col];
    }
    
    // is site (row, col) full? 
    public boolean isFull(int row, int col) {
        return wquf.connected(0, sideLength*(row-1) + col);
    }
    
    public int numberOfOpenSites() {
        return numOpenSites;
    }
    
    public boolean percolates() {
        return wquf.connected(0, sideLength*sideLength + 1);
    }
}