/**
 * This class represents the graphical user interface of the application.
 * It creates a window with a button and handles button click events.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI extends JFrame {
    private JButton button;
    private EventManager eventManager;
    public GUI() {
        // Set up the window
        setTitle("Board Game Event Planner");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Create Event");
        // Add action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                createEvent();
            }
        });
        // Add the button to the window
        add(button);
        // Initialize the event manager
        eventManager = new EventManager();
    }
    public void start() {
        // Show the window
        setVisible(true);
    }
    /**
     * Creates a new event.
     */
    private void createEvent() {
        // Show a dialog to get event details from the user
        String eventName = JOptionPane.showInputDialog(this, "Enter event name:");
        // Check if the user cancels the input dialog or leaves it empty
        if (eventName == null || eventName.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Event creation canceled or event name is empty.");
            return; // Exit the method without creating an event
        }
        String eventDate = JOptionPane.showInputDialog(this, "Enter event date:");
        if (eventDate == null || eventDate.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Event creation canceled or event date is empty.");
            return;
        }
        String eventLocation = JOptionPane.showInputDialog(this, "Enter event location:");
        if (eventLocation == null || eventLocation.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Event creation canceled or event location is empty.");
            return;
        }
        // Create a new event
        Event event = new Event(eventName, eventDate, eventLocation);
        // Add the event to the event manager
        eventManager.addEvent(event);
        // Display the event details
        String message = "Event Name: " + eventName + "\nEvent Date: " + eventDate + "\nEvent Location: " + eventLocation;
        JOptionPane.showMessageDialog(this, message);
    }
}