
import java.util.Scanner;

public class RepeatingBreakingAndRemembering {

    public static void main(String[] args) {

        // This exercise is worth five exercise points, and it is
        // gradually extended part by part.

        // If you want, you can send this exercise to the server
        // when it's just partially done. In that case the server will complain about
        // the parts you haven't done, but you'll get points for the finished parts.

        Scanner scanner = new Scanner(System.in);
        int sumNumber = 0;
        int numNumber = 0;
        int evenNumber = 0;
        int oddNumber = 0;

        System.out.println("Give numbers:");
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == -1) {
                System.out.println("Thx! Bye!");
                break;
            } else {
                if (number % 2 == 0) {
                    evenNumber++;
                } else {
                    oddNumber++;
                }
                sumNumber += number;
                numNumber++;
            }
        }
        System.out.println("Sum: " + sumNumber);
        System.out.println("Numbers: " + numNumber);

        if (numNumber > 0) {
            double avgNumber = (double) sumNumber / numNumber;
            System.out.println("Average: " + avgNumber);
        } else {
            System.out.println("Average: 0.0");
        }

        System.out.println("Even: " + evenNumber);
        System.out.println("Odd: " + oddNumber);
    }
}
