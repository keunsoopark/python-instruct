package strategy.after;

public class MyProgram {

    private SearchButton searchButton = new SearchButton(this);

    public void setModeAll() {
        searchButton.setSearchStrategy(new SearchStrategyAll());
    }
    public void setModeImage() {
        searchButton.setSearchStrategy(new SearchStrategyImage());
    }
    public void setModeNews() {
        searchButton.setSearchStrategy(new SearchStrategyNews());
    }
    public void setModeMap() {
        searchButton.setSearchStrategy(new SearchStrategyMap());
    }

    public void testProgram() {
        searchButton.onClick();     // SEARCH ALL

        setModeImage();
        searchButton.onClick();     // SEARCH IMAGE

        setModeNews();
        searchButton.onClick();     // SEARCH NEWS

        setModeMap();
        searchButton.onClick();     // SEARCH MAP
    }
}
