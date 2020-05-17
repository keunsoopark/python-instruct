package singleton.after;

public class Settings {

    private Settings () {};                     // Constructor
    private static Settings settings = null;    // "static" variable!! -> Only one in a process

    public static Settings getSettings () {
        if (settings == null) {                 // If Settings is not initiated, set new Settings
            settings = new Settings();
        }
        return settings;                        // Otherwise, return already made Settings
    }

    private boolean darkMode = false;
    private int fontSize = 13;

    public boolean getDarkMode () { return darkMode; }
    public int getFontSize () { return fontSize; }

    public void setDarkMode (boolean _darkMode) {
        darkMode = _darkMode;
    }
    public void setFontSize (boolean _fontSize) {
        fontSize = _fontSize;
    }
}