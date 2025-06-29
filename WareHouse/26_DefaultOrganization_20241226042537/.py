The highest priority comment is that the GUI class is missing the necessary import statements for the required classes. This will result in compilation errors when trying to use classes such as JFrame, JButton, and JOptionPane.
To fix this, add the following import statements at the top of the GUI class:
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
Once these import statements are added, the GUI class should compile without any errors.