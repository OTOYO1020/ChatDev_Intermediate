public class GUI extends JFrame {
    public GUI() {
        // Set frame properties
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 200);
        setLocationRelativeTo(null); // Center the frame on the screen
    }
    public void start() {
        // Add components to the frame
        JLabel label = new JLabel("Welcome to the Board Game Scenarios!");
        JButton button = new JButton("Start");
        add(label);
        add(button);
        // Set layout manager
        setLayout(new FlowLayout());
        // Display the frame
        setVisible(true);
    }
}