#!/usr/bin/env python
# -*- coding: utf-8 -*-
todo_file = open("todo.txt", "w+")

print "Welcome to the TODO task management program."

todo_dict = {}

while True:
    task = raw_input("Please enter a TODO task: ")
    print "Your task is: " + task
      # ya no ponemos el append porque deja de ser una lista
    status = raw_input("Was the task completed yet? (yes/no) ")
    if status == "yes":
        todo_dict[task] = True  # this is how we add a key-value pair into a dict
    else:
        todo_dict[task] = False

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break

print "All tasks: "
todo_file.write("TODAS LAS TAREAS:\n") #es lo que se escribe en el txt
print "Completed tasks:"
todo_file.write("TAREAS COMPLETADAS:\n") #es lo que se escribe en el txt
for item in todo_dict:
    if todo_dict[item] is True:
        print "- " + item
        todo_file.write("- " + item + "\n") #es lo que se escribe en el txt

todo_file.write("\n")
print "Incomplete tasks:"
todo_file.write("TAREAS INCOMPLETAS:\n") #es lo que se escribe en el txt
for item in todo_dict:
    if todo_dict[item] is False:
        print "- " + item
        todo_file.write("- " + item + "\n") #es lo que se escribe en el txt
print "END"

todo_file.close()