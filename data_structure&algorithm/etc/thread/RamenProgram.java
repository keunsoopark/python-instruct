public class RamenProgram {

    public static void main(String args[]) {
        try {
            RamenCook ramenCook = new RamenCook(Integer.parseInt(args[0]));
            new Thread (ramenCook, "A").start();
            new Thread (ramenCook, "B").start();
            new Thread (ramenCook, "C").start();
            new Thread (ramenCook, "D").start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

// "Runnable" interface => There should be "run" function in the class
// "run" function contains the tasks running in thread.
class RamenCook implements Runnable {
    private int ramenCount;
    private String[] burners = {"_", "_", "_", "_"};

    // constructor
    public RamenCook(int count) {
        ramenCount = count;
    }

    // "@Override" for overriding "run" function from "Runnable" interface.
    @Override
    public void run() {
        while (ramenCount > 0) {

            synchronized(this) {
                ramenCount--;
                System.out.println(
                    Thread.currentThread().getName()
                    + ": "+ ramenCount + " of ramen left"
                );
            }

            for (int i = 0; i < burners.length; i++) {
                if (!burners[i].equals("_")) continue;

                synchronized(this) {
                    // if (burners[i].equals("_")) {
                        burners[i] = Thread.currentThread().getName();
                        System.out.println(
                            "           "
                            + Thread.currentThread().getName()
                            + ": [" + (i + 1) + "] burner ON"
                        );
                        showBurners();
                    // }
                }

                try {
                    Thread.sleep(2000);
                } catch (Exception e) {
                    e.printStackTrace();
                }

                synchronized(this) {
                    burners[i] = "_";
                    System.out.println(
                            "           "
                            + Thread.currentThread().getName()
                            + ": [" + (i + 1) + "] burner OFF"
                        );
                        showBurners();
                }
                break;
            }

            try {
                Thread.sleep(Math.round(1000 * Math.random()));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private void showBurners() {
        String stringToPrint
            = "                                     ";
        for (int i = 0; i < burners.length; i++) {
            stringToPrint += (" " + burners[i]);
        }
        System.out.println(stringToPrint);
    }
}
