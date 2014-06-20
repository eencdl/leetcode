package main;

import java.util.Random;

/**
 there is an stream of in put integers
 if you have to return k number with equal probability


 */
public class ReservoirSampling {
    //In some case you don't know the length of the input
    //stream
    public int[] getRandom(int[] stream, int k) {

        int[] stored = new int[k];

        //initialize
        //store first k elements
        for(int i=0; i<k;i++) {
            stored[i] = stream[i];
        }

        Random r = new Random();
        for(int i=k; i<stream.length;i++) {
            int ran = r.nextInt(i);
            
            //replace reservoir if less than k
            if(ran < k) {
                stored[ran] = stream[i];
            }
        }
        return stored;
    }

}
