import java.util.*;
public class MockCodingDemo {
 static int[] twoSum(int[] nums,int target){
  Map<Long,Integer> seen=new HashMap<>();
  for(int i=0;i<nums.length;i++){long need=(long)target-nums[i];Integer j=seen.get(need);if(j!=null)return new int[]{j,i};seen.put((long)nums[i],i);}return new int[0];
 }
 // Precondition: nums is sorted ascending; result uses zero-based indices.
 static int[] sortedTwoSum(int[] nums,int target){int l=0,r=nums.length-1;while(l<r){long sum=(long)nums[l]+nums[r];if(sum==target)return new int[]{l,r};if(sum<target)l++;else r--;}return new int[0];}
 static List<List<Integer>> uniqueValuePairs(int[] nums,int target){
  int[] a=nums.clone();Arrays.sort(a);List<List<Integer>> out=new ArrayList<>();int l=0,r=a.length-1;
  while(l<r){long sum=(long)a[l]+a[r];if(sum<target)l++;else if(sum>target)r--;else{
   int x=a[l],y=a[r];out.add(List.of(x,y));while(l<r&&a[l]==x)l++;while(l<r&&a[r]==y)r--;
  }}return out;
 }
 static long countIndexPairs(int[] nums,int target){Map<Long,Long> counts=new HashMap<>();long result=0;for(int x:nums){result+=counts.getOrDefault((long)target-x,0L);counts.merge((long)x,1L,Long::sum);}return result;}
 static class Node {final int value;Node next;Node(int value){this.value=value;}}
 static Node cycleEntry(Node head){
  Node slow=head,fast=head;
  while(fast!=null&&fast.next!=null){slow=slow.next;fast=fast.next.next;if(slow==fast){
   Node start=head;while(start!=slow){start=start.next;slow=slow.next;}return start;
  }}return null;
 }
 static void check(boolean ok){if(!ok)throw new AssertionError();}
 public static void main(String[] args){
  check(Arrays.equals(twoSum(new int[]{3,3},6),new int[]{0,1}));check(twoSum(new int[]{Integer.MAX_VALUE,Integer.MAX_VALUE},-2).length==0);
  check(Arrays.equals(sortedTwoSum(new int[]{1,2,4,7},9),new int[]{1,3}));
  check(uniqueValuePairs(new int[]{1,1,2,2,3,3},4).equals(List.of(List.of(1,3),List.of(2,2))));check(countIndexPairs(new int[]{1,1,1,1},2)==6);
  check(cycleEntry(null)==null);Node a=new Node(1),b=new Node(1),c=new Node(3);a.next=b;b.next=c;check(cycleEntry(a)==null);c.next=b;check(cycleEntry(a)==b);
  Node self=new Node(7);self.next=self;check(cycleEntry(self)==self);
  System.out.println("PASS: Two Sum variants, overflow boundaries, duplicates, acyclic/self/prefix cycles");
 }
}
