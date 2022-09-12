package kyu8.Return_Negative.test;

import kyu8.Return_Negative.Kata;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertTrue;

class KataTest {

    @Test
    void makeNegative() {
        int x = 5;
        int my_res = -5;
        Kata kata = new Kata();
        int fact_res = kata.makeNegative(x);
        assertTrue(my_res==fact_res, "Test Done");
//message - сообщение которое будет выведенено если тетст не пройдет
    }
}