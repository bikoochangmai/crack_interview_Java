import java.util.*;
public class AtmDemo {
 record Withdrawal(long id,int amount,Map<Integer,Integer> notes){Withdrawal{notes=Map.copyOf(notes);}}
 record Attempt(int amount,Withdrawal result){}
 static class Atm {
  private final String owner;private int balance;private final Map<Integer,Integer> cash;private final Map<String,Attempt> done=new HashMap<>();private long sequence;
  Atm(String owner,int balance,Map<Integer,Integer> cash){this.owner=owner;this.balance=balance;this.cash=new HashMap<>(cash);if(balance<0||cash.entrySet().stream().anyMatch(e->e.getKey()<=0||e.getValue()<0))throw new IllegalArgumentException();}
  synchronized Withdrawal withdraw(String authenticatedSubject,String key,int amount){
   if(!owner.equals(authenticatedSubject))throw new SecurityException("not account owner");
   if(key==null||key.isBlank()||amount<=0)throw new IllegalArgumentException();
   Attempt old=done.get(key);if(old!=null){if(old.amount()!=amount)throw new IllegalArgumentException("key payload mismatch");return old.result();}
   if(amount>balance)throw new IllegalStateException("insufficient balance");
   var denominations=cash.keySet().stream().sorted(Comparator.reverseOrder()).toList();Map<Integer,Integer> plan=new HashMap<>();
   if(!plan(denominations,0,amount,plan))throw new IllegalStateException("cannot dispense exact amount");
   balance-=amount;plan.forEach((d,n)->cash.put(d,cash.get(d)-n));
   Withdrawal result=new Withdrawal(++sequence,amount,plan);done.put(key,new Attempt(amount,result));return result;
  }
  private boolean plan(List<Integer> denominations,int index,int remaining,Map<Integer,Integer> result){
   if(remaining==0)return true;if(index==denominations.size())return false;int d=denominations.get(index);
   for(int n=Math.min(cash.get(d),remaining/d);n>=0;n--){if(n==0)result.remove(d);else result.put(d,n);if(plan(denominations,index+1,remaining-n*d,result))return true;}
   result.remove(d);return false;
  }
  synchronized int balance(){return balance;}
 }
 public static void main(String[] args){
  Atm atm=new Atm("alice",1000,Map.of(500,1,200,3));
  Withdrawal w=atm.withdraw("alice","w81",600);if(!w.notes().equals(Map.of(200,3))||atm.balance()!=400)throw new AssertionError();
  if(atm.withdraw("alice","w81",600)!=w||atm.balance()!=400)throw new AssertionError();
  try{atm.withdraw("bob","w82",100);throw new AssertionError();}catch(SecurityException expected){}
  try{atm.withdraw("alice","w81",200);throw new AssertionError();}catch(IllegalArgumentException expected){}
  try{atm.withdraw("alice","w83",100);throw new AssertionError();}catch(IllegalStateException expected){}
  if(atm.balance()!=400)throw new AssertionError();
  System.out.println("PASS: bounded-note backtracking, owner check, replay, conflict and no-change failure");
 }
}
