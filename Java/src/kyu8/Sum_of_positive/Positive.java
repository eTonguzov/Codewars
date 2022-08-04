package kyu8.Sum_of_positive;
//You get an array of numbers, return the sum of all of the positives ones.
//        Example [1,-4,7,12] => 1 + 7 + 12 = 20
//        Note: if there is nothing to sum, the sum is default to 0.
public class Positive {
    public static void main(String[] args) {
        //int[] massive = new int[]{1,2,3};//создали массив и сразу же заполнили его значниями
        System.out.println(sum(new int[]{1,2,3}));
    }
    public static int sum(int[] arr) {
        int count = 0;
        for (int i : arr) {
            if (i > 0) {
                count+=i;
            }
        }
        return count;
    }
}
