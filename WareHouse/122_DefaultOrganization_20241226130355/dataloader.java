'''
This class handles the loading of items for each category.
'''
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class DataLoader {
    private Map<String, List<String>> itemsMap;
    public DataLoader() {
        itemsMap = new HashMap<>();
        itemsMap.put("literature", new ArrayList<>());
        itemsMap.put("music", new ArrayList<>());
        itemsMap.put("visual arts", new ArrayList<>());
        itemsMap.put("films", new ArrayList<>());
        // Load initial items for each category
        loadInitialItems();
    }
    /**
     * Returns a list of items for the specified category.
     */
    public List<String> getItems(String category) {
        return itemsMap.get(category);
    }
    /**
     * Loads initial items for each category.
     */
    private void loadInitialItems() {
        // Load literature items
        List<String> literatureItems = itemsMap.get("literature");
        literatureItems.add("Book 1");
        literatureItems.add("Book 2");
        literatureItems.add("Book 3");
        // Load music items
        List<String> musicItems = itemsMap.get("music");
        musicItems.add("Song 1");
        musicItems.add("Song 2");
        musicItems.add("Song 3");
        // Load visual arts items
        List<String> visualArtsItems = itemsMap.get("visual arts");
        visualArtsItems.add("Painting 1");
        visualArtsItems.add("Painting 2");
        visualArtsItems.add("Painting 3");
        // Load films items
        List<String> filmsItems = itemsMap.get("films");
        filmsItems.add("Movie 1");
        filmsItems.add("Movie 2");
        filmsItems.add("Movie 3");
    }
}