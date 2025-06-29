import java.util.HashMap;
/**
 * This class represents a rule book for games.
 */
public class RuleBook {
    private HashMap<String, String> rules;
    /**
     * Constructs a RuleBook object.
     */
    public RuleBook() {
        rules = new HashMap<>();
    }
    /**
     * Adds a rule to the rule book.
     *
     * @param ruleName        the name of the rule
     * @param ruleDescription the description of the rule
     */
    public void addRule(String ruleName, String ruleDescription) {
        rules.put(ruleName, ruleDescription);
    }
    /**
     * Returns the description of a rule.
     *
     * @param ruleName the name of the rule
     * @return the description of the rule
     */
    public String getRule(String ruleName) {
        return rules.get(ruleName);
    }
}