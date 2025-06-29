'''
This is the main class that starts the BudgetTrackerLite application.
'''
import javax.swing.*;
import java.awt.*;
public class Main {
    public static void main(String[] args) {
        DataManager dataManager = new DataManager();
        GUI gui = new GUI(dataManager);
        Controller controller = new Controller(gui, dataManager);
        gui.show();
    }
}