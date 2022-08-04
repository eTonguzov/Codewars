package kyu8.Even_or_Odd;

//Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

public class EvenOrOdd {
    public static void main(String[] args) {
        System.out.println(even_or_odd(6));
    }
    public static String even_or_odd(int number) {
        if(number%2==0){
            return "Odd";
        }
        else return "Even";

    }
}