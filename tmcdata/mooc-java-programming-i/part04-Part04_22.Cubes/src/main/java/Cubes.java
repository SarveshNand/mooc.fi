
import java.util.Scanner;

public class Cubes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String value = scanner.nextLine();
            if (value.equals("end")) {
                break;
            }
            int number = Integer.valueOf(value);
            int cube = number * number * number;
            System.out.println(cube);
        }
        scanner.close();
    }
}