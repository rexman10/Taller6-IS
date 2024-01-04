import io
import sys
from behave import *
from main import *

# Step 1: Given the to-do list is empty 
@given('the to-do list is empty') 
def step_impl(context): 
    # Set the to-do list as an empty list 
    global to_do_list 
    to_do_list = [] 
 
# Step 2: When the user adds a task "Buy groceries" 
@when('the user adds a task "{task}"') 
def step_impl(context, task): 
    # Add the task to the to-do list 
    global to_do_list 
    to_do_list.append(task) 
 
# Step 3: Then the to-do list should contain "Buy groceries" 
@then('the to-do list should contain "{task}"') 
def step_impl(context, task): 
    # Check if the task is in the to-do list 
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'




@given('the to-do list contains tasks "{task1}" and "{task2}"')
def step_to_do_list_contains_tasks(context, task1, task2):
    context.to_do_list = [task1, task2]
    context.captured_output = io.StringIO()
    sys.stdout = context.captured_output

@when('the user lists all tasks')
def step_impl(context):
    list_tasks(context.to_do_list)
    sys.stdout = sys.__stdout__
    context.captured_output.seek(0)

@then('the output should print the string {printed_tasks}')
def step_impl(context, printed_tasks):
    expected_output = printed_tasks.strip() if context.text else ""  # Use an empty string if context.text is None
    expected_output_with_newlines = expected_output.replace("\\n", "\n")
    
    # Access captured stdout and compare it with the expected output
    actual_output = context.captured_output.getvalue().strip()
    assert actual_output == expected_output_with_newlines, f"Expected: {expected_output} Actual:\n{actual_output}"


@given('the to-do list contains tasks and statuses')
def step_impl(context):
    prepare_List()
    context.to_do_list = tasks
    context.statuses = status

# When step: Mark a task as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    mark_completed(task)

# Then step: Check if the to-do list shows the task as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    indice = search_task(task)
    task_status = context.statuses[indice]
    assert task_status == "Completed", f"Task '{task}' status is '{task_status}', expected 'Completed'"



# When step: Mark a task as completed
@when('the user marks task "{task}" as in progress')
def step_impl(context, task):
    mark_inProgress(task)

# Then step: Check if the to-do list shows the task as in progress
@then('the to-do list should show task "{task}" as in progress')
def step_impl(context, task):
    indice = search_task(task)
    task_status = context.statuses[indice]
    assert task_status == "In Progress", f"Task '{task}' status is '{task_status}', expected 'In Progress'"


# Given step: The to-do list contains tasks
@given('the to-do list contains tasks')
def step_impl(context):
    prepare_List()
    context.to_do_list = tasks
    context.statuses = status

# When step: Remove a task from the to-do list
@when('the user removes {task} from the to-do list')
def step_impl(context, task):
    context.task_to_remove = task
    index = 0
    for i in range(len(context.to_do_list)):
        if context.to_do_list[i] == task:
            index = i
    context.to_do_list.remove(tasks[index])
    context.statuses.remove(status[index])
    tasks.remove(tasks[index])
    status.remove(status[index])

# Then step: Check if the to-do list does not contain the task
@then('the to-do list should no longer contain that task')
def step_impl(context):
    assert len(context.to_do_list) == len(tasks), f"Expected to-do list without {context.task_to_remove}, got {context.to_do_list}"



# When step: Clear the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    clear_todo_list()
    context.to_do_list = tasks
    context.statuses = status

# Then step: Check if the to-do list is empty
@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.to_do_list) == 0, f"Expected empty to-do list, got {context.to_do_list}"