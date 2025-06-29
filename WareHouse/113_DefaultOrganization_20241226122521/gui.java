import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import com.yourpackage.DataStorage;
/**
 * This class represents the graphical user interface of the web application.
 * It creates a window with components for logging working hours, recording time off, and requesting leave.
 * It also handles user interactions and performs the necessary actions.
 */
public class GUI extends JFrame {
    private JTextField workingHoursTextField;
    private JButton logHoursButton;
    private JTextField timeOffTextField;
    private JButton requestTimeOffButton;
    private DataStorage dataStorage;
    public GUI(DataStorage dataStorage) {
        this.dataStorage = dataStorage;
        setTitle("Employee Time Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Components for logging working hours
        JLabel workingHoursLabel = new JLabel("Working Hours:");
        workingHoursTextField = new JTextField(10);
        logHoursButton = new JButton("Log Hours");
        logHoursButton.addActionListener(new LogHoursButtonClickListener());
        // Components for requesting time off
        JLabel timeOffLabel = new JLabel("Time Off:");
        timeOffTextField = new JTextField(10);
        requestTimeOffButton = new JButton("Request Time Off");
        requestTimeOffButton.addActionListener(new RequestTimeOffButtonClickListener());
        // Add components to the window
        add(workingHoursLabel);
        add(workingHoursTextField);
        add(logHoursButton);
        add(timeOffLabel);
        add(timeOffTextField);
        add(requestTimeOffButton);
    }
    public void startApplication() {
        setVisible(true);
    }
    private class LogHoursButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String workingHours = workingHoursTextField.getText();
            dataStorage.saveWorkingHours(workingHours);
            JOptionPane.showMessageDialog(null, "Working hours logged: " + workingHours);
        }
    }
    private class RequestTimeOffButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String timeOff = timeOffTextField.getText();
            dataStorage.saveTimeOffRequest(timeOff);
            JOptionPane.showMessageDialog(null, "Time off requested: " + timeOff);
        }
    }
}