import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        // implement here the program that allows the user to enter
        // book information and to examine them
        ArrayList<Book> books = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Title: ");
            String title = scanner.nextLine();
            if (title.isEmpty()) {
                break;
            }
            System.out.print("Pages: ");
            int pages = Integer.valueOf(scanner.nextLine());
            System.out.print("Publication year: ");
            int year = Integer.valueOf(scanner.nextLine());
            books.add(new Book(title, pages, year));
        }
        System.out.print("What information will be printed? ");
        String whatToPrint = scanner.nextLine();
        for (Book booklist : books) {
            if (whatToPrint.equals("everything")) {
                System.out.println(booklist);
            } else if (whatToPrint.equals("name")) {
                System.out.println(booklist.getTitle());
            }
        }
        scanner.close();
    }
}
