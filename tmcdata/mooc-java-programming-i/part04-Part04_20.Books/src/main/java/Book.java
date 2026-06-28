public class Book {
  private String title;
  private int pages;
  private int year;

  public Book(String bookTitle, int numberOfPages, int publicationYear) {
    this.title = bookTitle;
    this.pages = numberOfPages;
    this.year = publicationYear;
  }

  public String getTitle() {
    return this.title;
  }

  public int getPages() {
    return this.pages;
  }

  public int year() {
    return this.year;
  }

  @Override
  public String toString() {
    return this.title + ", " + this.pages + " pages, " + this.year;
  }
}
