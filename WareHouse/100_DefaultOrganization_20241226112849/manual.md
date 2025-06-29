# Customer Complaint Management System User Manual

## Introduction

The Customer Complaint Management System is a software application developed in Java that allows businesses to efficiently manage and resolve customer complaints. It provides a user-friendly interface for customers to submit their complaints, track the progress, and communicate with the support team. The system enables support agents to receive and assign complaints to specific agents, prioritize them based on severity, and ensure timely resolution. It also offers features like automated ticket escalation, complaint status tracking, and reporting to enhance customer satisfaction.

## Installation

To install and run the Customer Complaint Management System, please follow these steps:

1. Ensure that you have Java Development Kit (JDK) installed on your system. You can download the latest version of JDK from the official Oracle website.

2. Download the project files from the provided source.

3. Extract the downloaded files to a directory of your choice.

4. Open a command prompt or terminal and navigate to the directory where you extracted the project files.

5. Build the project by running the following command:

   ```
   javac *.java
   ```

6. Once the project is successfully built, start the web application by running the following command:

   ```
   java Main
   ```

7. The web application will start running on a local server. You can access it by opening a web browser and entering the following URL:

   ```
   http://localhost:8080
   ```

## User Guide

### Customer Interface

The Customer Interface allows customers to submit their complaints, track the progress, and communicate with the support team.

1. Open a web browser and enter the following URL:

   ```
   http://localhost:8080
   ```

2. On the homepage, you will see a welcome message and a complaint submission form.

3. Fill in the description of your complaint in the "Description" field.

4. Select the severity of your complaint from the "Severity" dropdown.

5. Click the "Submit" button to submit your complaint.

6. You will be redirected to the complaints page, where you can see the list of all submitted complaints.

7. You can track the progress of your complaint by checking its status in the "Status" column.

8. If you want to communicate with the support team regarding your complaint, you can use the messaging feature provided on the complaints page.

### Support Agent Interface

The Support Agent Interface allows support agents to receive and assign complaints, prioritize them based on severity, and ensure timely resolution.

1. Open a web browser and enter the following URL:

   ```
   http://localhost:8080/complaints
   ```

2. On the complaints page, you will see the list of all submitted complaints.

3. To assign a complaint to a specific agent, click the "Assign" button next to the complaint.

4. Select the agent from the dropdown menu and click the "Assign" button.

5. The complaint will be assigned to the selected agent, and its status will be updated to "In Progress".

6. Support agents can escalate the priority of a complaint by clicking the "Escalate" button next to the complaint.

7. Escalating a complaint will update its severity to a higher level.

8. Support agents can communicate with customers regarding their complaints using the messaging feature provided on the complaints page.

## Conclusion

The Customer Complaint Management System provides an efficient way for businesses to manage and resolve customer complaints. By following the installation and user guide provided in this manual, you can easily set up and use the system to enhance customer satisfaction and improve complaint resolution processes. If you have any further questions or need assistance, please refer to the documentation or contact our support team.