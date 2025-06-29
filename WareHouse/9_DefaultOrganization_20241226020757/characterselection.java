import java.util.ArrayList;
import java.util.List;
import java.util.Random;
/**
 * This class represents the character selection logic in the game.
 */
public class CharacterSelection {
    private List<Character> characters;
    public CharacterSelection() {
        characters = new ArrayList<>();
        characters.add(new Character("Character 1", 100));
        characters.add(new Character("Character 2", 150));
        characters.add(new Character("Character 3", 200));
    }
    public Character selectCharacter() {
        Random random = new Random();
        int index = random.nextInt(characters.size());
        return characters.get(index);
    }
}