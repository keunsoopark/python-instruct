package async;

public class Main {

    public static void Main(String [] args) {
        asyncBlackBean();
    }

    private static void asyncBlackBean() {
        String dishStatus = "full";

        deliverBlackBean();
        asyncEatBlackBean();
        toNextPlace();
    }

    private static void deliverBlackBean() {
        System.out.println("Dish status as delivering: " + dishStatus);
    }

    private static void asyncEatBlackBean() {
        ListenableFuture<ResponseEntity<String>> entity
                = asyncRestTemplate.getForEntity("http://localhost:3000/eat-noodle-2sec",
                String.class);

        entity.addCallback(
            result -> {
                dishStatus = result.getBody();
                System.out.println("Dish status after eating: " + dishStatus);
            }, e -> e.printStackTrace());
    }

    private static void toNextPlace() {
        System.out.printf("Dish status while moving: " + dishStatus);
    }
}
