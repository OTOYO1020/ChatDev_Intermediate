public class GUI extends JFrame implements ActionListener {
    private JButton button;
    private JLabel label;
    /**
     * Constructor to initialize the GUI.
     */
    public GUI() {
        // Set the title of the GUI window
        setTitle("Application");
        // Set the size of the GUI window
        setSize(300, 200);
        // Set the layout manager of the GUI window
        setLayout(new FlowLayout());
        // Create a button
        button = new JButton("Click me");
        // Add action listener to the button
        button.addActionListener(this);
        // Create a label
        label = new JLabel("Hello, World!");
        // Add the button and label to the GUI window
        add(button);
        add(label);
        // Set the default close operation of the GUI window
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    /**
     * Method to start the GUI.
     */
    public void start() {
        // Make the GUI window visible
        setVisible(true);
    }
    /**
     * Method to handle button click event.
     */
    @Override
    public void actionPerformed(ActionEvent e) {
        // Change the text of the label when the button is clicked
        label.setText("Button clicked");
    }
}