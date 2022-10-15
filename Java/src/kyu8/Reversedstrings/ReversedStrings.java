package kyu8.Reversedstrings;

//Description:
//Complete the solution so that it reverses the string passed into it.
//
//        'world'  =>  'dlrow'
//        'word'   =>  'drow'
public class ReversedStrings {
    public static void main(String[] args) {
        System.out.println(solution("12345"));

    }
    public static String solution(String str) {
        char[] list = str.toCharArray();//разбиваем строку в массив Char
        for(int i = 0; i < list.length/2; i++){
            char temp = list[i];//временная переменная
            list[i] = list[list.length-i-1];//на первое место попадает последний элемент
            list[list.length-i-1] = temp;//а на последнее первый
            }
        String revers = "";
        for(char ch: list){
            revers = revers + ch;
        }

        return revers;
    }

}