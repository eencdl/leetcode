package main;

/**
 * Created by don on 5/31/14.
 */
public class WordSearch {
    //This is like the robot question, except we need visited
    public boolean exist(char[][] board, String word) {
        //Try all possible starting point
        boolean[][] visited = new boolean[board.length][board[0].length];
        for(int i=0; i<board[0].length; i++) {
            for(int j=0; j<board.length;j++) {
                if(search(board,visited,j,i,word,0))
                    return true;
            }
        }
        return false;

    }

    public boolean search(char[][] board, boolean[][] visited, int y, int x,String word, int wIdx) {
        //base conditions


        //If the current element not match
        if(board[y][x]  != word.charAt(wIdx))
            return false;

        //Means char match
        //If we match the whole word
        if(wIdx == word.length()-1)
            return true;


        //so continue to examine next char
        visited[y][x] = true;


        // IMPORTANT !!
        // You have to ONLY RETURN if success, that way in case of false
        // situation it will try another direction
        // i.e. if ( try one direction && search( that direction ) )
        //        return true;
        //
        //     if ( try another direction && search ( another direction ) )
        //        return true;
        //
        // DO NOT DO THE FOLLOWING, it is NOT THE SAME
        //
        //     if ( try one direction )
        //         return search ( that direction );
        //
        //     if ( try another direction )
        //         return search ( another direction );
        //
        // The major problem with above is that in case of false,
        // It shall not continue to try another direction
        // The way you put "return" is crucial and need deep consideration


        //go left
        if(x-1 >= 0 && !visited[y][x-1] && search(board,visited,y,x-1,word,wIdx+1)) {
            return true; //only return if true, else explore other condition
        }

        //go right
        if(x+1 < board[0].length && !visited[y][x+1] && search(board,visited,y,x+1,word,wIdx+1)){
            return true;
        }

        //go up
        if(y-1 >= 0 && !visited[y-1][x]&& search(board,visited,y-1,x,word,wIdx+1)) {
            return true;
        }

        //go down
        if(y+1 < board.length && !visited[y+1][x] && search(board,visited,y+1,x,word,wIdx+1)){
            return true;
        }


        //Must erase the path if unsuccessful
        visited[y][x] = false;

        return false;
    }


}
