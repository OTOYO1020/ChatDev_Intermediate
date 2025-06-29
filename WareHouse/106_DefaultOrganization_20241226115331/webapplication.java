import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping; // Add this import statement
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
/**
 * This class represents the web application and handles the controllers and views.
 */
@SpringBootApplication
public class WebApplication {
    private List<Lead> leads;
    private Map<Integer, String> stages;
    @Autowired
    private LeadController leadController;
    public void start() {
        // Initialize the leads list
        leads = new ArrayList<>();
        // Initialize the stages map
        stages = new HashMap<>();
        stages.put(1, "Lead");
        stages.put(2, "Contacted");
        stages.put(3, "Qualified");
        stages.put(4, "Proposal");
        stages.put(5, "Closed");
        // Start the Spring Boot application
        SpringApplication.run(WebApplication.class);
    }
    /**
     * This class represents a lead or prospect.
     */
    private static class Lead {
        private String name;
        private String contact;
        private int stage;
        private String reminderDate; // Add reminderDate field
        public Lead(String name, String contact) {
            this.name = name;
            this.contact = contact;
            this.stage = 1; // Default stage is 1 (Lead)
        }
        public String getName() {
            return name;
        }
        public String getContact() {
            return contact;
        }
        public int getStage() {
            return stage;
        }
        public void setStage(int stage) {
            this.stage = stage;
        }
        public String getReminderDate() {
            return reminderDate;
        }
        public void setReminderDate(String reminderDate) {
            this.reminderDate = reminderDate;
        }
    }
    /**
     * This class represents the controller for handling web requests.
     */
    @Controller
    @RequestMapping("/") // Add this annotation to map all methods to the root URL ("/")
    public class LeadController {
        @Autowired
        public LeadController() {
        }
        @GetMapping("/")
        public String index(Model model) {
            model.addAttribute("leads", leads);
            model.addAttribute("stages", stages);
            return "index";
        }
        @PostMapping("/addLead")
        public String addLead(@RequestParam String name, @RequestParam String contact) {
            leads.add(new Lead(name, contact));
            return "redirect:/";
        }
        @PostMapping("/setReminder")
        public String setReminder(@RequestParam int leadId, @RequestParam String reminderDate) {
            Lead lead = leads.get(leadId);
            lead.setReminderDate(reminderDate);
            return "redirect:/";
        }
        @GetMapping("/monitorConversionRates")
        public String monitorConversionRates(Model model) {
            Map<String, Double> conversionRates = calculateConversionRates();
            model.addAttribute("conversionRates", conversionRates);
            return "conversionRates";
        }
        @PostMapping("/updateStage")
        public String updateStage(@RequestParam int leadId, @RequestParam int stage) {
            Lead lead = leads.get(leadId);
            lead.setStage(stage);
            return "redirect:/";
        }
        private Map<String, Double> calculateConversionRates() {
            Map<String, Double> conversionRates = new HashMap<>();
            int totalLeads = leads.size();
            for (String stage : stages.values()) {
                int leadsAtStage = countLeadsAtStage(stage);
                double conversionRate = (double) leadsAtStage / totalLeads;
                conversionRates.put(stage, conversionRate);
            }
            return conversionRates;
        }
        private int countLeadsAtStage(String stage) {
            int count = 0;
            for (Lead lead : leads) {
                if (stages.get(lead.getStage()).equals(stage)) {
                    count++;
                }
            }
            return count;
        }
    }
}