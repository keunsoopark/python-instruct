package state;

public interface ModeState {
    public void toggle (ModeSwitch modeSwitch);
}

class ModeStateLight implements ModeState {
    public void toggle (ModeSwitch modeSwitch) {
        System.out.println("FROM LIGHT TO DARK");
        modeSwitch.setState(new ModeStateDark());
    }
}

class ModeStateDark implements ModeState {
    public void toggle (ModeSwitch modeSwitch) {
        System.out.println("FROM DARK TO LIGHT");
        modeSwitch.setState(new ModeStateLight());
    }
}
