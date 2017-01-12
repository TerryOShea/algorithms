/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  A class representing a point on the x-y plane. Draws the point
 *  using StdDraw, implements a comparable interface, calculates the slope bet-
 *  ween two points, and provides a comparator based on slope.
 ******************************************************************************/

import java.util.Comparator;
import edu.princeton.cs.algs4.StdDraw;

public class Point implements Comparable<Point> {

    private final int x; // x-coordinate of this point
    private final int y; // y-coordinate of this point

    // constructs the point (x, y)
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // draws this point
    public void draw() {
        StdDraw.point(x, y);
    }

    // draws the line segment from this point to that point
    public void drawTo(Point that) {
        StdDraw.line(this.x, this.y, that.x, that.y);
    }

    // string representation
    public String toString() {
        return "(" + Integer.toString(this.x) + ", " + Integer.toString(this.y) + ")";
    }

    // compare two points by y-coordinates, breaking ties by x-coordinates
    public int compareTo(Point that) {
        if (this.y != that.y) {
            return this.y - that.y;
        }
        return this.x - that.x;
    }

    // the slope between this point and that point
    public double slopeTo(Point that) {
        if (that == null) throw new java.lang.NullPointerException();
        if (this.x == that.x) { 
            if (this.y == that.y) return Double.NEGATIVE_INFINITY;
            return Double.POSITIVE_INFINITY; 
        }
        if (this.y == that.x) return 0;
        return (this.y - that.y) * 1.0 / (this.x - that.x);
    }

    // compare two points by slopes they make with this point
    public Comparator<Point> slopeOrder() {
        return new BySlope();
    }

    private class BySlope implements Comparator<Point> {
        public int compare(Point a, Point b) {
            double s1 = Point.this.slopeTo(a);
            double s2 = Point.this.slopeTo(b);
            if (s1 < s2) return -1;
            if (s1 > s2) return 1;
            return 0;
        }
    }

    public static void main(String[] args) {
    }
}