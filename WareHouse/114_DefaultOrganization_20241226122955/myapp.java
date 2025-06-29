import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import feedback.FeedbackCollector;
import feedback.FeedbackCategorizer;
import feedback.SentimentAnalyzer;
import feedback.ReportGenerator;
import java.util.List;
public class MyApp extends Application {
    private FeedbackCollector feedbackCollector;
    private FeedbackCategorizer feedbackCategorizer;
    private SentimentAnalyzer sentimentAnalyzer;
    private ReportGenerator reportGenerator;
    @Override
    public void start(Stage primaryStage) {
        // Create the main layout
        VBox root = new VBox();
        // Set up the scene
        Scene scene = new Scene(root, 800, 600);
        // Set the scene on the primary stage
        primaryStage.setScene(scene);
        primaryStage.setTitle("Product Feedback Analyzer");
        // Initialize the components
        feedbackCollector = new FeedbackCollector();
        feedbackCategorizer = new FeedbackCategorizer();
        sentimentAnalyzer = new SentimentAnalyzer();
        reportGenerator = new ReportGenerator();
        // Collect feedback
        feedbackCollector.collectFeedback();
        // Get feedback data
        List<FeedbackCollector.Feedback> feedbackData = feedbackCollector.getFeedbackData();
        // Categorize feedback
        feedbackCategorizer.categorizeFeedback(feedbackData);
        // Analyze sentiment
        sentimentAnalyzer.analyzeSentiment(feedbackData);
        // Generate reports
        reportGenerator.generateReports(feedbackData, sentimentAnalyzer.getSentiment());
        // Add UI components and logic here
        primaryStage.show();
    }
}