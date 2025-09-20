class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int numlength=numbers.length;
        double sum=0;
        
        for(int i=0;i<numlength;i++){
            sum+= numbers[i];
        }
        answer=sum/numlength;
        return answer;
    }
}