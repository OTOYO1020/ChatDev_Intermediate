/**
 * This is the main class that initializes the GUI and starts the application.
 */
public class Main {
    public static void main(String[] args) {
        FinancialDocumentManager manager = new FinancialDocumentManager();
        GUI gui = new GUI(manager);
        gui.start();
    }
}