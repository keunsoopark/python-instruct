package sync;

public class Main {

    public static void main(String [] args) {
        syncBlackBean();
    }

    private static void syncBlackBean() {
        String dishStatus = "full";

        deliverBlackBean();
        syncEatBlackBean();
        toNextPlace();
    }

    private static void deliverBlackBean() {
        System.out.println("Dish status as delivering: " + dishStatus);
    }

    private static void syncEatBlackBean() {
        String dishStatus = restTemplate.getForObject("http://localhost:3000/eat-noodle-2sec",
                String.class);
        System.out.println("Dish status after eating: " + dishStatus);
    }

    private static void toNextPlace() {
        System.out.printf("Dish status while moving: " + dishStatus);
    }

}
