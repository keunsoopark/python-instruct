package strategy.before;

public class SearchButton {

    private MyProgram myProgram;

    public SearchButton (MyProgram _myProgram) {
        myProgram = _myProgram;
    }

    public void onClick () {
        if (myProgram.mode = Mode.ALL) {
            System.out.println("SEARCH ALL");
        } else if (myProgram.mode == Mode.IMAGE) {
            System.out.printf("SEARCH IMAGE");
        } else if (myProgram.mode == Mode.NEWS) {
            System.out.println("SEARCH NEWS");
        } else if (myProgram.mode = Mode.MAP) {
            System.out.println("SEARCH MAP");
        }
    }
}
