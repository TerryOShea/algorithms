/******************************************************************************
 *  Name:    Terry O'Shea
 *  NetID:   toshea
 *
 *  Partner Name:    N/A
 *  Partner NetID:   N/A
 *  Partner Precept: N/A
 * 
 *  Description:  Making a randomized queue class that supports enqueueing and 
 *  dequeueing a random item. Also makes a (random) iterator available.
 ******************************************************************************/

import java.util.Iterator;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private Item[] s;
    private int size = 0;

    public RandomizedQueue() {
        s = (Item[]) new Object[1];
    }

    // is the queue empty?
    public boolean isEmpty() {
        return size == 0;
    }

    // return the number of items on the queue
    public int size() {
        return size;
    }

    // add the item 
    public void enqueue(Item item) {
        if (item == null) throw new java.lang.NullPointerException();
        if (size == s.length) resize(2 * s.length);
        s[size++] = item;
    }

    private void resize(int capacity) {
        Item[] copy = (Item[]) new Object[capacity];
        for (int i = 0; i < size; i++) {
            copy[i] = s[i];
        }
        s = copy;
    }

    // remove and return a random item
    public Item dequeue() {
        if (size == 0) throw new java.util.NoSuchElementException();
        int a = StdRandom.uniform(size);
        Item item = s[a];
        s[a] = s[size-1];
        s[--size] = null;
        if (size > 0 && size == s.length/4) resize(s.length/2);
        return item;
    }

    // return (but do not remove) a random item
    public Item sample() {
        if (size == 0) throw new java.util.NoSuchElementException();
        int a = StdRandom.uniform(size);
        return s[a];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        return new RandomizedQueueIterator();
    }

    private class RandomizedQueueIterator implements Iterator<Item> {

        private int index;

        private RandomizedQueueIterator() {
            index = 0;
            shuffle();
        }

        // a Fisher-Yates shuffle randomizes s in linear time
        private void shuffle() {
            for (int i = 0; i < size-1; i++) {
                int j = StdRandom.uniform(i, size);
                Item temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }

        public boolean hasNext() {
            return index < size;
        }

        public void remove() {
            throw new java.lang.UnsupportedOperationException();
        }

        public Item next() {
            if (!(hasNext())) throw new java.util.NoSuchElementException();
            return s[index++];
        }
    }

    // unit testing
    public static void main(String[] args) {
    }
}