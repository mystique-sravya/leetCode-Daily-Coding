class Solution {
    public int[][] merge(int[][] intervals) {
         if (intervals == null||intervals.length <= 1) {
            return intervals;
        }
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        List<int[]> merged=new ArrayList<>();
        int [] curr=intervals[0];
        for(int i=1;i<intervals.length;i++){
            int[] next = intervals[i];
            if (curr[1]>=next[0]){
                curr[1]=Math.max(curr[1],next[1]);
            }
            else{
                merged.add(curr);
                curr=next;
            }
        }
        merged.add(curr);
        int[][] ans=new int[merged.size()][2];
        for (int i=0; i<merged.size();i++) {
            ans[i]=merged.get(i);
        }
        return ans;
    }
}