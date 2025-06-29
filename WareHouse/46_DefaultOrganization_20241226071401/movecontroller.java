'''
This class handles the move tracking functionality.
'''
package com.example.demo;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
@Controller
public class MoveController {
    @GetMapping("/moves")
    public String moves(Model model) {
        // Add any required logic here
        return "moves";
    }
    @PostMapping("/track")
    public String trackMove(@RequestParam("move") String move, Model model) {
        // Process the move and perform necessary actions
        // Add any required logic here
        model.addAttribute("result", "Move tracked successfully!");
        return "moves";
    }
}