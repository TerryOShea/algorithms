/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Running trials using the Percolation class to determine
 *  what percent of cells are usually open when a system percolates and 
 *  calculating related statistics (mean, stddev, confidence interval)
 ******************************************************************************/

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

public class PercolationStats {
    private double mean; 
    private double stddev; 
    private double confidenceLo; 
    private double confidenceHi;
    
    // array to store the results of each trial
    private double[] results;
    
    // perform trials independent experiments on an n-by-n grid
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) { 
            throw new java.lang.IllegalArgumentException(); 
        }
        
        results = new double[trials];
        
        // for each trial, records what % of cells were open when the system percolated
        for (int i = 0; i < trials; i++) {
            Percolation p = new Percolation(n);

            while (!p.percolates()) {
                int row = StdRandom.uniform(1, n+1);
                int col = StdRandom.uniform(1, n+1);
                p.open(row, col);
            }
            
            results[i] = (float) p.numberOfOpenSites()/(n*n);
        }
        
        mean = StdStats.mean(results);
        stddev = StdStats.stddev(results);
        double margOfError = 1.96*stddev/Math.sqrt(trials);
        confidenceLo = mean + margOfError;
        confidenceHi = mean - margOfError;
    }
    
    // sample mean of percolation threshold
    public double mean() {
        return mean;
    }
    
    // sample standard deviation of percolation threshold
    public double stddev() {
        return stddev;
    }
    
    // low endpoint of 95% confidence interval
    public double confidenceLo() {
        return confidenceLo;
    }
    
    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return confidenceHi;
    }
    
    // test client
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);
        PercolationStats p = new PercolationStats(n, trials);
        System.out.println("mean                    = " + p.mean());
        System.out.println("stddev                  = " + p.stddev());
        System.out.println("95% confidence interval = " + p.confidenceLo() + ", "
                               + p.confidenceHi());
    }
}