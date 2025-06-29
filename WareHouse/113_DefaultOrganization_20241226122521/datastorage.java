import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;
/**
 * This class represents the data storage for the Employee Time Tracker application.
 * It provides methods for saving the logged working hours and time off requests to the database or file system.
 */
public class DataStorage {
    private String dbUrl;
    private String dbUsername;
    private String dbPassword;
    public DataStorage() {
        loadConfiguration();
    }
    private void loadConfiguration() {
        Properties properties = new Properties();
        try (FileInputStream fis = new FileInputStream("config.properties")) {
            properties.load(fis);
            dbUrl = properties.getProperty("db.url");
            dbUsername = properties.getProperty("db.username");
            dbPassword = properties.getProperty("db.password");
        } catch (IOException e) {
            System.out.println("Error loading configuration: " + e.getMessage());
        }
    }
    public void saveWorkingHours(String workingHours) {
        try {
            Connection connection = DriverManager.getConnection(dbUrl, dbUsername, dbPassword);
            PreparedStatement statement = connection.prepareStatement("INSERT INTO working_hours (hours) VALUES (?)");
            statement.setString(1, workingHours);
            statement.executeUpdate();
            statement.close();
            connection.close();
            System.out.println("Working hours saved: " + workingHours);
        } catch (SQLException e) {
            System.out.println("Error saving working hours: " + e.getMessage());
        }
    }
    public void saveTimeOffRequest(String timeOff) {
        try {
            Connection connection = DriverManager.getConnection(dbUrl, dbUsername, dbPassword);
            PreparedStatement statement = connection.prepareStatement("INSERT INTO time_off_requests (request) VALUES (?)");
            statement.setString(1, timeOff);
            statement.executeUpdate();
            statement.close();
            connection.close();
            System.out.println("Time off request saved: " + timeOff);
        } catch (SQLException e) {
            System.out.println("Error saving time off request: " + e.getMessage());
        }
    }
}