package adapter.commandExample;

public class Robot {

    public enum Direction { LEFT, RIGHT };

    public void moveForward (int space) {
        System.out.println(space + " 칸 전진");
    }
    public void turn (Direction _direction) {
        System.out.println(
                (_direction == Direction.LEFT ? "left" : "right") + "으로 방향전환"
        );
    }
    public void pickup() {
        System.out.println("pick up a stuff on front");
    }
}
