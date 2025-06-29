import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton scanButton;
    private JButton uploadButton;
    private JButton categorizeButton;
    private JButton labelButton;
    private JButton expirationButton;
    private JButton reportButton;
    private JButton storageButton;
    private JButton retrievalButton;
    private FinancialDocumentManager manager;
    public GUI(FinancialDocumentManager manager) {
        this.manager = manager;
    }
    public void start() {
        frame = new JFrame("Financial Document Manager");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new FlowLayout());
        scanButton = new JButton("Scan Document");
        scanButton.addActionListener(new ScanButtonClickListener());
        frame.add(scanButton);
        uploadButton = new JButton("Upload Document");
        uploadButton.addActionListener(new UploadButtonClickListener());
        frame.add(uploadButton);
        categorizeButton = new JButton("Categorize Document");
        categorizeButton.addActionListener(new CategorizeButtonClickListener());
        frame.add(categorizeButton);
        labelButton = new JButton("Label Document");
        labelButton.addActionListener(new LabelButtonClickListener());
        frame.add(labelButton);
        expirationButton = new JButton("Set Expiration Date");
        expirationButton.addActionListener(new ExpirationButtonClickListener());
        frame.add(expirationButton);
        reportButton = new JButton("Generate Document Report");
        reportButton.addActionListener(new ReportButtonClickListener());
        frame.add(reportButton);
        storageButton = new JButton("Secure Storage");
        storageButton.addActionListener(new StorageButtonClickListener());
        frame.add(storageButton);
        retrievalButton = new JButton("Secure Retrieval");
        retrievalButton.addActionListener(new RetrievalButtonClickListener());
        frame.add(retrievalButton);
        frame.setVisible(true);
    }
    private class ScanButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.scanDocument();
            JOptionPane.showMessageDialog(null, "Document Scanned!");
        }
    }
    private class UploadButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.uploadDocument();
            JOptionPane.showMessageDialog(null, "Document Uploaded!");
        }
    }
    private class CategorizeButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.categorizeDocument();
            JOptionPane.showMessageDialog(null, "Document Categorized!");
        }
    }
    private class LabelButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.labelDocument();
            JOptionPane.showMessageDialog(null, "Document Labeled!");
        }
    }
    private class ExpirationButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.setExpirationDate();
            JOptionPane.showMessageDialog(null, "Expiration Date Set!");
        }
    }
    private class ReportButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.generateDocumentReport();
            JOptionPane.showMessageDialog(null, "Document Report Generated!");
        }
    }
    private class StorageButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.secureStorage();
            JOptionPane.showMessageDialog(null, "Document Securely Stored!");
        }
    }
    private class RetrievalButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            manager.secureRetrieval();
            JOptionPane.showMessageDialog(null, "Document Securely Retrieved!");
        }
    }
}