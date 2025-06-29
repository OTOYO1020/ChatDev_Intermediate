public static void main(String[] args) {
    JFrame frame = new JFrame("Web Application");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setLayout(new FlowLayout());
    JButton button = new JButton("Click me");
    button.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
            JOptionPane.showMessageDialog(null, "Button clicked");
        }
    });
    frame.add(button);
    frame.pack();
    frame.setVisible(true);
}