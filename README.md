# Requisition Management system

# About project:
I make a project of Python called a "Requisition Management system" that helps to the staff members to submit requests for the items and calculates the cost of it, and lets an admin (me)  to reject or approved the request of its decision.
After that, the system shows all requests and give a summary upon how many were approved, pending, or not approved.
The aim of this projectis to show how software design principles and  how pattern can be used in real code. This helps to make the programe easy to read, simple to use, and ready for future improvements

#Design principles used:
1. Encapsulation:
   All logic is positioned within a class called 'requestsystem'. Everything related to requisitions-staff info, item cost, approval status-is also stored and managed in one place.

    Why important: It keeps the program organized and reduces error in other parts of the code.
2. Abstraction:
   users interact with simple function like staff_info() or requisition_details() without needing to understand the inner workings.
   why important : It hides the complexity and makes the system easier to use and extend.
3. Single Responsibility Principle:
   In this each method in the class has one clear work.
   user_info() it creates a new request
   requisition_details() it aadd items and calculates it total price
   respond_requisition() it shows approval status.
   display_requisition() it show the request details.
   requisition_statistics() it provide a summary.
   why important:- it is easier to maintain, test, understand.
4. Reusability and Modularity:
    Functions are modular and reusable. The system could be adapted for a website or connectd to a database in the future.

# Design Patterns:
Factory Pattern:In this pattern every time a new requisition is made, the system creates it using a method, like a small factory.
Work flow: The program follows a clear process : create reruest - add item - respond - display - summarize.
These
