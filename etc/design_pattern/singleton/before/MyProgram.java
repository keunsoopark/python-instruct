package singleton.before;

public class MyProgram {
    
    public static void main (String[] args) {
        new FirstPage().setAndPrintSettings();
        new SecondPage().printSettings();
    }
}