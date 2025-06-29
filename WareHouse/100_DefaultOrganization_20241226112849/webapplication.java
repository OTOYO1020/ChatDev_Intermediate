import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
@SpringBootApplication
@Controller
public class WebApplication {
    private ComplaintManager complaintManager;
    public WebApplication() {
        this.complaintManager = new ComplaintManager();
    }
    public static void main(String[] args) {
        SpringApplication.run(WebApplication.class, args);
    }
    @RequestMapping("/")
    public String home(Model model) {
        model.addAttribute("message", "Hello, World!");
        return "index";
    }
    @GetMapping("/complaints")
    public String getComplaints(Model model) {
        model.addAttribute("complaints", complaintManager.getAllComplaints());
        return "complaints";
    }
    @PostMapping("/complaints")
    public String submitComplaint(@RequestParam("description") String description,
                                  @RequestParam("severity") Severity severity) {
        complaintManager.createComplaint(description, severity);
        return "redirect:/complaints";
    }
}