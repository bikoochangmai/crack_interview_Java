import java.util.*;
public class TicTacToeDemo {
 enum Mark {X,O}
 enum State {IN_PROGRESS,X_WON,O_WON,DRAW}
 static class Game {
  private final Mark[][] board=new Mark[3][3];private Mark turn=Mark.X;private State state=State.IN_PROGRESS;private int moves;
  synchronized State move(Mark player,int row,int col){
   Objects.requireNonNull(player);
   if(state!=State.IN_PROGRESS)throw new IllegalStateException("game over");
   if(player!=turn)throw new IllegalArgumentException("wrong turn");
   if(row<0||row>=3||col<0||col>=3||board[row][col]!=null)throw new IllegalArgumentException("invalid cell");
   board[row][col]=player;moves++;
   boolean rowWin=true,colWin=true,diag=true,anti=true;
   for(int i=0;i<3;i++){rowWin&=board[row][i]==player;colWin&=board[i][col]==player;diag&=board[i][i]==player;anti&=board[i][2-i]==player;}
   if(rowWin||colWin||diag||anti)state=player==Mark.X?State.X_WON:State.O_WON;
   else if(moves==9)state=State.DRAW;else turn=turn==Mark.X?Mark.O:Mark.X;
   return state;
  }
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  Game win=new Game();
  try{win.move(Mark.O,0,0);throw new AssertionError();}catch(IllegalArgumentException expected){}
  win.move(Mark.X,0,0);
  try{win.move(Mark.O,0,0);throw new AssertionError();}catch(IllegalArgumentException expected){}
  win.move(Mark.O,1,0);win.move(Mark.X,0,1);win.move(Mark.O,1,1);check(win.move(Mark.X,0,2)==State.X_WON);
  try{win.move(Mark.O,2,2);throw new AssertionError();}catch(IllegalStateException expected){}
  Game draw=new Game();int[][] cells={{0,0},{0,1},{0,2},{1,1},{1,0},{1,2},{2,1},{2,0},{2,2}};
  State result=null;for(int i=0;i<cells.length;i++)result=draw.move(i%2==0?Mark.X:Mark.O,cells[i][0],cells[i][1]);check(result==State.DRAW);
  Game diagonal=new Game();diagonal.move(Mark.X,0,0);diagonal.move(Mark.O,0,1);diagonal.move(Mark.X,1,1);diagonal.move(Mark.O,0,2);check(diagonal.move(Mark.X,2,2)==State.X_WON);
  try{new Game().move(Mark.X,-1,0);throw new AssertionError();}catch(IllegalArgumentException expected){}
  System.out.println("PASS: turn, occupied/out-of-range cells, row/diagonal wins, draw and terminal state");
 }
}
