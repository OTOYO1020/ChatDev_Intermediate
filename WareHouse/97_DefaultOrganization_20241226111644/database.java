import java.sql.*;
import java.util.ArrayList;
import java.util.List;
/**
 * This class handles the database operations for the web application.
 */
public class Database {
    private Connection connection;
    public Database() {
        connection = null;
    }
    public void connect() throws SQLException {
        if (connection == null || connection.isClosed()) {
            // Replace "jdbc:mysql://localhost:3306/database_name" with your database connection URL
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/database_name", "username", "password");
            System.out.println("Connected to the database");
        }
    }
    public void disconnect() throws SQLException {
        if (connection != null && !connection.isClosed()) {
            connection.close();
            System.out.println("Disconnected from the database");
        }
    }
    public void createExpense(String expense, String category) {
        try {
            String query = "INSERT INTO expenses (expense, category) VALUES (?, ?)";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, expense);
            statement.setString(2, category);
            statement.executeUpdate();
            System.out.println("Expense created: " + expense + " - " + category);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public List<String> getExpenses() {
        List<String> expenses = new ArrayList<>();
        try {
            String query = "SELECT * FROM expenses";
            Statement statement = connection.createStatement();
            ResultSet resultSet = statement.executeQuery(query);
            while (resultSet.next()) {
                String expense = resultSet.getString("expense");
                String category = resultSet.getString("category");
                expenses.add(expense + " - " + category);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return expenses;
    }
    public void updateExpense(String expense, String category) {
        try {
            String query = "UPDATE expenses SET category = ? WHERE expense = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, category);
            statement.setString(2, expense);
            statement.executeUpdate();
            System.out.println("Expense updated: " + expense + " - " + category);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public void deleteExpense(String expense) {
        try {
            String query = "DELETE FROM expenses WHERE expense = ?";
            PreparedStatement statement = connection.prepareStatement(query);
            statement.setString(1, expense);
            statement.executeUpdate();
            System.out.println("Expense deleted: " + expense);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}