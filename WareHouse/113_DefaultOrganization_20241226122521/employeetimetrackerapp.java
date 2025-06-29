/**
 * This class represents the Employee Time Tracker application.
 * It initializes the GUI and provides functionality for managing employee working hours and attendance.
 */
import com.yourpackage.GUI;
import com.yourpackage.DataStorage;
public class EmployeeTimeTrackerApp {
    private GUI gui;
    private DataStorage dataStorage;
    public EmployeeTimeTrackerApp() {
        dataStorage = new DataStorage();
        gui = new GUI(dataStorage);
    }
    public void startApplication() {
        gui.startApplication();
    }
}