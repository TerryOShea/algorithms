/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Finds (using a brute-force algorithm with n^4 complexity) line
 *  segments with four points in a collection of points.
 ******************************************************************************/

import java.util.Arrays;

public class BruteCollinearPoints {

    private LineSegment[] lines;
    private int numberOfLines;

    // finds all line segments containing 4 points
    public BruteCollinearPoints(Point[] pts) {
        Point[] points = pts.clone();
        int lg = points.length;
        if (lg == 0) throw new java.lang.IllegalArgumentException();

        Arrays.sort(points);

        for (int i = 0; i < lg; i++) {
            if (points[i] == null) throw new java.lang.IllegalArgumentException();
            if (i < lg - 1 && points[i].compareTo(points[i+1]) == 0) throw new java.lang.IllegalArgumentException();
        }

        lines = new LineSegment[1];
        numberOfLines = 0;

        for (int p = 0; p < lg - 3; p++) {
            for (int q = p + 1; q < lg - 2; q++) {
                double s1 = points[p].slopeTo(points[q]);
                for (int r = q + 1; r < lg - 1; r++) {
                    double s2 = points[p].slopeTo(points[r]);
                    for (int s = r + 1; s < lg; s++) {
                        double s3 = points[p].slopeTo(points[s]);
                        if (s1 == s3 && s2 == s3) {
                            lines[numberOfLines++] = new LineSegment(points[p], points[s]);
                            if (numberOfLines == lines.length) resizeLines(2);
                        }
                    }
                }
            }
        }

        if (numberOfLines < lines.length) resizeLines(1); // remove extra space at the array end
    }

    // since we don't know how many line segments there will be, the array holding
    // the line segments resizes dynamically
    private void resizeLines(int mult) {
        LineSegment[] newLines = new LineSegment[numberOfLines * mult];
        for (int i = 0; i < numberOfLines; i++) {
            newLines[i] = lines[i];
        }
        lines = newLines;
    }

    // the number of line segments
    public int numberOfSegments() {
        return numberOfLines;
    }

    // the line segments
    public LineSegment[] segments() {
        LineSegment[] copy = lines.clone();
        return copy;
    }
}