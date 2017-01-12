/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Finds (using a sorting-based algorithm with n^2*logn 
 *  complexity) line segments with four or more points in a collection of points.
 ******************************************************************************/

import java.util.Comparator;
import java.util.Arrays;

public class FastCollinearPoints {

    private LineSegment[] lines;
    private int numberOfLines;

    // finds all line segments containing 4 or more points
    public FastCollinearPoints(Point[] pts) {
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
            Comparator<Point> c = points[p].slopeOrder();
            Arrays.sort(points, p+1, lg, c); // sorts rest of points based on their slope with points[p]

            int startIndex = p+1;
            while (startIndex < lg-2) {
                double s1 = points[p].slopeTo(points[startIndex]);
                int endIndex = startIndex + 1;

                while (endIndex < lg && s1 == points[p].slopeTo(points[endIndex])) {
                    endIndex++;
                }

                // if there are 3 or more points with the same slope with points[p]
                if (endIndex - startIndex >= 3) {
                    Point[] pointsInLine = new Point[endIndex - startIndex + 1];
                    pointsInLine[0] = points[p];
                    for (int i = 0; i < endIndex - startIndex; i++) {
                        pointsInLine[i+1] = points[startIndex + i];
                    }
                    Arrays.sort(pointsInLine);

                    lines[numberOfLines++] = new LineSegment(pointsInLine[0], pointsInLine[pointsInLine.length - 1]);
                    if (numberOfLines == lines.length) resizeLines(2);
                }
                startIndex += endIndex - startIndex;
            }
            Arrays.sort(points, p+1, lg); // remove extra space at the array end
        }
        resizeLines(1);
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