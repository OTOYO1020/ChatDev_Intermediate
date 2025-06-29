import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;
/**
 * This class represents the GUI for the Business Task Scheduler application.
 * It extends JFrame and includes the necessary components and functionality for creating tasks,
 * assigning them to team members, setting deadlines, tracking progress, and displaying notifications.
 */
public class GUI extends JFrame implements ActionListener {
    private JLabel titleLabel;
    private JButton createTaskButton;
    private JButton assignTaskButton;
    private JButton setDeadlineButton;
    private JButton trackProgressButton;
    private List<Task> taskList;
    private List<String> teamMemberList;
    /**
     * Constructor for the GUI class.
     * Initializes the GUI components and sets up the layout.
     */
    public GUI() {
        // Set the title of the frame
        setTitle("Business Task Scheduler");
        // Set the layout to FlowLayout
        setLayout(new FlowLayout());
        // Create and add the title label
        titleLabel = new JLabel("Business Task Scheduler");
        add(titleLabel);
        // Create and add the create task button
        createTaskButton = new JButton("Create Task");
        add(createTaskButton);
        // Create and add the assign task button
        assignTaskButton = new JButton("Assign Task");
        add(assignTaskButton);
        // Create and add the set deadline button
        setDeadlineButton = new JButton("Set Deadline");
        add(setDeadlineButton);
        // Create and add the track progress button
        trackProgressButton = new JButton("Track Progress");
        add(trackProgressButton);
        // Set the default close operation
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Set the size of the frame
        setSize(300, 200);
        // Set the visibility of the frame
        setVisible(true);
        // Initialize the task list and team member list
        taskList = new ArrayList<>();
        teamMemberList = new ArrayList<>();
    }
    /**
     * Method to start the application.
     * Adds action listeners to the buttons.
     */
    public void start() {
        // Add action listener to the create task button
        createTaskButton.addActionListener(this);
        // Add action listener to the assign task button
        assignTaskButton.addActionListener(this);
        // Add action listener to the set deadline button
        setDeadlineButton.addActionListener(this);
        // Add action listener to the track progress button
        trackProgressButton.addActionListener(this);
    }
    /**
     * Method to handle button clicks.
     * Implements the functionality for each button.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == createTaskButton) {
            // Prompt the user to enter task details
            String taskName = JOptionPane.showInputDialog(this, "Enter task name:");
            String taskDescription = JOptionPane.showInputDialog(this, "Enter task description:");
            // Create a new task object with the entered details
            Task task = new Task(taskName, taskDescription);
            // Add the task to the task list
            taskList.add(task);
            // Display the list of created tasks
            displayTasks();
            JOptionPane.showMessageDialog(this, "Task created successfully.");
        } else if (e.getSource() == assignTaskButton) {
            // Prompt the user to select a team member
            String teamMember = JOptionPane.showInputDialog(this, "Select a team member:");
            // Assign the task to the selected team member
            assignTask(teamMember);
            // Display the assigned tasks
            displayAssignedTasks();
            JOptionPane.showMessageDialog(this, "Task assigned to " + teamMember + " successfully.");
        } else if (e.getSource() == setDeadlineButton) {
            // Prompt the user to enter a deadline
            String deadline = JOptionPane.showInputDialog(this, "Enter task deadline:");
            // Set the deadline for the selected task
            setDeadline(deadline);
            // Display the deadlines
            displayDeadlines();
            JOptionPane.showMessageDialog(this, "Deadline set to " + deadline + " successfully.");
        } else if (e.getSource() == trackProgressButton) {
            // Track progress functionality
            trackProgress();
        }
    }
    /**
     * Method to display the list of created tasks.
     */
    private void displayTasks() {
        StringBuilder sb = new StringBuilder();
        sb.append("Created Tasks:\n");
        for (Task task : taskList) {
            sb.append(task.getName()).append(": ").append(task.getDescription()).append("\n");
        }
        JOptionPane.showMessageDialog(this, sb.toString());
    }
    /**
     * Method to assign a task to a team member.
     *
     * @param teamMember The team member to assign the task to
     */
    private void assignTask(String teamMember) {
        teamMemberList.add(teamMember);
    }
    /**
     * Method to display the list of assigned tasks.
     */
    private void displayAssignedTasks() {
        StringBuilder sb = new StringBuilder();
        sb.append("Assigned Tasks:\n");
        for (int i = 0; i < taskList.size(); i++) {
            Task task = taskList.get(i);
            String teamMember = teamMemberList.get(i);
            sb.append(task.getName()).append(": ").append(task.getDescription()).append(" (Assigned to: ").append(teamMember).append(")\n");
        }
        JOptionPane.showMessageDialog(this, sb.toString());
    }
    /**
     * Method to set the deadline for a task.
     *
     * @param deadline The deadline for the task
     */
    private void setDeadline(String deadline) {
        for (Task task : taskList) {
            task.setDeadline(deadline);
        }
    }
    /**
     * Method to display the list of deadlines.
     */
    private void displayDeadlines() {
        StringBuilder sb = new StringBuilder();
        sb.append("Task Deadlines:\n");
        for (Task task : taskList) {
            sb.append(task.getName()).append(": ").append(task.getDeadline()).append("\n");
        }
        JOptionPane.showMessageDialog(this, sb.toString());
    }
    /**
     * Method to track the progress of a task.
     */
    private void trackProgress() {
        // Prompt the user to select a task
        String taskName = JOptionPane.showInputDialog(this, "Select a task:");
        // Find the task in the taskList
        Task selectedTask = null;
        for (Task task : taskList) {
            if (task.getName().equals(taskName)) {
                selectedTask = task;
                break;
            }
        }
        // Prompt the user to enter the progress percentage
        String progressString = JOptionPane.showInputDialog(this, "Enter progress percentage:");
        int progress = Integer.parseInt(progressString);
        // Update the progress of the selected task
        selectedTask.setProgress(progress);
        // Display the updated progress
        displayProgress();
        JOptionPane.showMessageDialog(this, "Progress updated successfully.");
    }
    /**
     * Method to display the progress of each task.
     */
    private void displayProgress() {
        StringBuilder sb = new StringBuilder();
        sb.append("Task Progress:\n");
        for (Task task : taskList) {
            sb.append(task.getName()).append(": ").append(task.getProgress()).append("%\n");
        }
        JOptionPane.showMessageDialog(this, sb.toString());
    }
}