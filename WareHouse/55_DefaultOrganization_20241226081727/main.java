'''
This class contains the main method to start the application.
'''
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import controller.Controller;
import gui.GUI;
public class Main {
    public static void main(String[] args) {
        GUI gui = new GUI();
        Controller.setGUI(gui); // Set the GUI instance in the Controller class
        gui.show();
    }
}