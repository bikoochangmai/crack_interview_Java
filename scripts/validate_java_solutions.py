"""Compile and run both coding variants against examples and boundary cases (JDK 17+)."""
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
# Expressions run in independent classes, so each variant uses identical fresh inputs.
CASES = [
 'Arrays.equals(s.twoSum(new int[]{2,7,11,15},9),new int[]{0,1}) && Arrays.equals(s.twoSum(new int[]{3,3},6),new int[]{0,1})',
 's.isAnagram("anagram","nagaram") && !s.isAnagram("aab","abb") && s.isAnagram("","")',
 's.containsDuplicate(new int[]{1,2,3,1}) && !s.containsDuplicate(new int[]{})',
 'groups(s.groupAnagrams(new String[]{"eat","tea","tan","ate","nat","bat"})).equals("[[ate, eat, tea], [bat], [nat, tan]]") && s.groupAnagrams(new String[]{"",""}).get(0).size()==2',
 'sorted(s.topKFrequent(new int[]{1,1,1,2,2,3},2)).equals("[1, 2]") && sorted(s.topKFrequent(new int[]{5,5},1)).equals("[5]")',
 'Arrays.equals(s.productExceptSelf(new int[]{1,2,3,4}),new int[]{24,12,8,6}) && Arrays.equals(s.productExceptSelf(new int[]{0,2,3}),new int[]{6,0,0}) && Arrays.equals(s.productExceptSelf(new int[]{0,0}),new int[]{0,0})',
 's.isPalindrome("A man, a plan, a canal: Panama") && !s.isPalindrome("race a car") && s.isPalindrome(".,")',
 'groups(s.threeSum(new int[]{-1,0,1,2,-1,-4})).equals("[[-1, -1, 2], [-1, 0, 1]]") && s.threeSum(new int[]{0,0,0,0}).size()==1',
 's.maxProfit(new int[]{7,1,5,3,6,4})==5 && s.maxProfit(new int[]{7,6,4})==0 && s.maxProfit(new int[]{})==0',
 's.lengthOfLongestSubstring("abcabcbb")==3 && s.lengthOfLongestSubstring("abba")==2 && s.lengthOfLongestSubstring("")==0',
 's.isValid("([]){}") && !s.isValid("([)]") && !s.isValid("(") && s.isValid("")',
 's.search(new int[]{-1,0,3,5,9,12},9)==4 && s.search(new int[]{},1)==-1 && s.search(new int[]{1},2)==-1',
 's.search(new int[]{4,5,6,7,0,1,2},0)==4 && s.search(new int[]{1},1)==0 && s.search(new int[]{},1)==-1',
 's.maxSubArray(new int[]{-2,1,-3,4,-1,2,1,-5,4})==6 && s.maxSubArray(new int[]{-3,-1,-2})==-1',
 's.climbStairs(4)==5 && s.climbStairs(1)==1 && s.climbStairs(2)==2',
 's.coinChange(new int[]{1,2,5},11)==3 && s.coinChange(new int[]{2},3)==-1 && s.coinChange(new int[]{2},0)==0',
 's.numIslands(new char[][]{{\'1\',\'1\',\'0\'},{\'0\',\'1\',\'0\'},{\'0\',\'0\',\'1\'}})==2 && s.numIslands(new char[][]{})==0 && s.numIslands(new char[][]{{\'1\',\'0\'},{\'0\',\'1\'}})==2',
 'intervals(s.merge(new int[][]{{1,3},{2,6},{8,10}})).equals("[[1, 6], [8, 10]]") && intervals(s.merge(new int[][]{{1,4},{4,5}})).equals("[[1, 5]]") && s.merge(new int[][]{}).length==0',
 's.findKthLargest(new int[]{3,2,1,5,6,4},2)==5 && s.findKthLargest(new int[]{3,3,2},2)==3 && s.findKthLargest(new int[]{-2,-1},2)==-2',
 's.rob(new int[]{2,7,9,3,1})==12 && s.rob(new int[]{2,1,1,2})==4 && s.rob(new int[]{})==0',
]
HELPERS = '''
 static String sorted(int[] a){Arrays.sort(a);return Arrays.toString(a);}
 static String groups(List<List<String>> a){List<String> out=new ArrayList<>();for(List<String> g:a){Collections.sort(g);out.add(g.toString());}Collections.sort(out);return out.toString();}
 static String intervals(int[][] a){Arrays.sort(a,Comparator.comparingInt(x->x[0]));return Arrays.deepToString(a);}
'''
# The same normalization supports integer triples and string anagram groups.
HELPERS = HELPERS.replace('List<List<String>> a','List<? extends List<?>> a').replace('for(List<String> g:a){Collections.sort(g);out.add(g.toString());}', 'for(List<?> g:a){List<String> copy=new ArrayList<>();for(Object x:g)copy.add(x.toString());Collections.sort(copy);out.add(copy.toString());}')

def main():
 problems=json.loads((ROOT/'data/leetcode.json').read_text(encoding='utf-8'))
 assert len(problems)==len(CASES)
 with tempfile.TemporaryDirectory(prefix='java-study-check-', dir=ROOT) as folder:
  folder=Path(folder); assert folder.resolve().parent == ROOT.resolve(); names=[]
  for p,check in zip(problems,CASES):
   for field in ('bruteCode','code'):
    name=p['id']+('Brute' if field=='bruteCode' else 'Improved');names.append(name)
    source='import java.util.*;\npublic class '+name+' {\n'+p[field]+HELPERS+'\npublic static void main(String[] args){var s=new '+name+'();if(!('+check+')) throw new AssertionError("'+name+'");}\n}'
    (folder/(name+'.java')).write_text(source,encoding='utf-8')
  subprocess.run(['javac','-encoding','UTF-8','-d',str(folder),*[str(folder/(n+'.java')) for n in names]],check=True)
  for name in names:subprocess.run(['java','-cp',str(folder),name],check=True,timeout=10)
 print(f'Passed sample and boundary checks for {len(names)} Java solution variants.')

if __name__=='__main__':main()

