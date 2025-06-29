import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JTextField nameField;
    private JTextField quantityField;
    private JTextField conditionField;
    private JTextArea collectionArea;
    private JButton addButton;
    private JButton removeButton;
    private JButton searchButton;
    private CardCollection cardCollection;
    public GUI() {
        // Create the main window
        frame = new JFrame("Card Collection Tracker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create text fields
        nameField = new JTextField(20);
        quantityField = new JTextField(5);
        conditionField = new JTextField(10);
        // Create buttons
        addButton = new JButton("Add Card");
        removeButton = new JButton("Remove Card");
        searchButton = new JButton("Search Card");
        // Create collection area
        collectionArea = new JTextArea(10, 30);
        collectionArea.setEditable(false);
        // Create a panel for input fields and buttons
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new FlowLayout());
        inputPanel.add(new JLabel("Name:"));
        inputPanel.add(nameField);
        inputPanel.add(new JLabel("Quantity:"));
        inputPanel.add(quantityField);
        inputPanel.add(new JLabel("Condition:"));
        inputPanel.add(conditionField);
        inputPanel.add(addButton);
        inputPanel.add(removeButton);
        inputPanel.add(searchButton);
        // Add the input panel and collection area to the main window
        frame.getContentPane().add(inputPanel, BorderLayout.NORTH);
        frame.getContentPane().add(new JScrollPane(collectionArea), BorderLayout.CENTER);
        // Create a new card collection
        cardCollection = new CardCollection();
        // Add action listeners for the buttons
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addCard();
                updateCollectionArea();
            }
        });
        removeButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                removeCard();
                updateCollectionArea();
            }
        });
        searchButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                searchCard();
                updateCollectionArea();
            }
        });
        // Update the collection area with existing cards
        updateCollectionArea();
    }
    public void start() {
        // Show the main window
        frame.setVisible(true);
    }
    private void addCard() {
        String name = nameField.getText();
        String quantityText = quantityField.getText();
        String condition = conditionField.getText();
        // Validate quantity input
        try {
            int quantity = Integer.parseInt(quantityText);
            // Create a new card with the provided details
            Card card = new Card(name, quantity, condition);
            // Add the card to the collection
            cardCollection.addCard(card);
            // Clear the input fields
            nameField.setText("");
            quantityField.setText("");
            conditionField.setText("");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(frame, "Invalid quantity input. Please enter a valid integer.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    private void removeCard() {
        String name = nameField.getText();
        // Remove the card from the collection
        cardCollection.removeCard(name);
        // Clear the input fields
        nameField.setText("");
        quantityField.setText("");
        conditionField.setText("");
    }
    private void searchCard() {
        String name = nameField.getText();
        // Search for the card in the collection
        Card card = cardCollection.searchCard(name);
        if (card != null) {
            // Display the card details
            nameField.setText(card.getName());
            quantityField.setText(String.valueOf(card.getQuantity()));
            conditionField.setText(card.getCondition());
        } else {
            // Clear the input fields
            nameField.setText("");
            quantityField.setText("");
            conditionField.setText("");
        }
    }
    private void updateCollectionArea() {
        // Clear the collection area
        collectionArea.setText("");
        // Get the card collection
        ArrayList<Card> cards = cardCollection.getCardCollection();
        // Display each card in the collection
        for (Card card : cards) {
            collectionArea.append(card.getName() + " - Quantity: " + card.getQuantity() + " - Condition: " + card.getCondition() + "\n");
        }
    }
}