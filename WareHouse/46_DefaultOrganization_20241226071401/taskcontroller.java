'''
This class handles the task submission and processing.
'''
package com.example.demo;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
@Controller
public class TaskController {
    @GetMapping("/")
    public String home() {
        return "index";
    }
    @PostMapping("/submit")
    public String submitTask(@RequestParam("taskDetails") String taskDetails, Model model) {
        // Process the task details and perform necessary actions
        // Add any required logic here
        // For now, we will just display the task details
        model.addAttribute("taskDetails", taskDetails);
        return "result";
    }
}