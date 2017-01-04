/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Making a 'deque' class that supports pushing to the front
 *  and to the back as well as popping from either end. Also makes an iterator
 *  available.
 ******************************************************************************/

import java.util.Iterator;

// implements a deque using a doubly-linked list
public class Deque<Item> implements Iterable<Item> {
    private Node first = null;
    private Node last = null;
    private int size = 0;

    private class Node {
        private Item item;
        private Node next;
        private Node prev;
    }

    // is the deque empty? 
    public boolean isEmpty() {
        return size == 0;
    }

    // return the number of items on the deque
    public int size() {
        return size;
    }

    // add the item to the front
    public void addFirst(Item item) {
        verifyAdd(item);
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
        if (size > 0) oldfirst.prev = first;
        else last = first;
        size++;
    }

    // add the item to the end
    public void addLast(Item item) {
        verifyAdd(item);
        Node oldlast = last;
        last = new Node();
        last.item = item;
        last.prev = oldlast;
        if (size > 0) oldlast.next = last;
        else first = last;
        size++;
    }

    private void verifyAdd(Item item) {
        if (item == null) throw new java.lang.NullPointerException();
    }

    // remove and return the item from the front
    public Item removeFirst() {
        verifyRemove();
        Item item = first.item;
        size--;
        if (size > 0) {
            first = first.next;
            first.prev = null;
        }
        return item;
    }

    // remove and return the item from the end
    public Item removeLast() {
        verifyRemove();
        Item item = last.item;
        size--;
        if (size > 0) {
            last = last.prev;
            last.next = null;
        }
        return item;
    }

    private void verifyRemove() {
        if (size == 0) throw new java.util.NoSuchElementException();
    }

    // return an iterator over items in order from front to end
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
        private Node current = first;

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

        public Item next() {
            if (!(hasNext())) throw new java.util.NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    // unit testing
    public static void main(String[] args) {
    }
}