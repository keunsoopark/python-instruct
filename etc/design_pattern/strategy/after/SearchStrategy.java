package strategy.after;

interface SearchStrategy() {
    public void search();
}

class SearchStrategyAll implements SearchStrategy {
    public void search() {
        System.out.println("SEARCH ALL");
    }
}

class SearchStrategyImage implements SearchStrategy {
    public void search() {
        System.out.println("SEARCH IMAGE");
    }
}

class SearchStrategyNews implements SearchStrategy {
    public void serach() {
        System.out.println("SEARCH NEWS");
    }
}

class SearchStrategyMap implements SearchStrategy {
    public void search() {
        System.out.println("SEARCH MAP");
    }
}
