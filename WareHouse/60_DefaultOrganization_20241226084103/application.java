import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import javax.swing.JOptionPane;
public class Application {
    private List<String> dictionaryWords;
    public Application() {
        try {
            dictionaryWords = Files.readAllLines(Paths.get("dictionary.txt"));
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Error reading dictionary file");
            System.exit(1);
        }
    }
    public List<String> generateWords(String availableLetters) {
        List<String> validWords = new ArrayList<>();
        for (String word : dictionaryWords) {
            if (isValidWord(word, availableLetters)) {
                validWords.add(word);
            }
        }
        return validWords;
    }
    private boolean isValidWord(String word, String availableLetters) {
        int[] letterCount = new int[26];
        for (char c : availableLetters.toCharArray()) {
            letterCount[c - 'a']++;
        }
        for (char c : word.toCharArray()) {
            if (letterCount[c - 'a'] == 0) {
                return false;
            }
            letterCount[c - 'a']--;
        }
        return true;
    }
}