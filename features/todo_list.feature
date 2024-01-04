Feature: To-do list
    Scenario: Add a task to the to-do list 
        Given the to-do list is empty 
        When the user adds a task "Buy groceries" 
        Then the to-do list should contain "Buy groceries" 

    Scenario: List all tasks in the to-do list 
        Given the to-do list contains tasks "Buy groceries" and "Pay bills"
        When the user lists all tasks 
        Then the output should print the string "Tasks:\\n- Buy groceries\\n- Pay bills"

    Scenario: Mark a task as completed 
        Given the to-do list contains tasks and statuses: 
        | Task | Status | 
        | Buy groceries | Pending | 
        When the user marks task "Buy groceries" as completed 
        Then the to-do list should show task "Buy groceries" as completed

    Scenario: Mark a task as in progress 
        Given the to-do list contains tasks and statuses: 
        | Task | Status | 
        | Buy groceries | Pending | 
        When the user marks task "Buy groceries" as in progress 
        Then the to-do list should show task "Buy groceries" as in progress 

    Scenario: Remove one task from the to-do list 
        Given the to-do list contains tasks: 
        | Task | 
        | Buy groceries | 
        | Pay bills | 
        When the user removes "Buy groceries" from the to-do list 
        Then the to-do list should no longer contain that task

    Scenario: Clear the entire to-do list 
        Given the to-do list contains tasks: 
        | Task | 
        | Buy groceries | 
        | Pay bills | 
        When the user clears the to-do list 
        Then the to-do list should be empty 
