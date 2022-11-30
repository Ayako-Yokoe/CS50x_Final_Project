# My To-Do List

## About this app

My To-Do List is a fully customizable to-do list. Once a user plans tasks with their priorities and due dates, it automatically displays them in order by their priorities and due dates. It handles uncompleted tasks as well. It carries them over to the following day.<br>
This app will help you save time and energy because you don't need to re-create a new to-do list. You don't need to keep old to-do lists that contain uncompleted tasks and start over by creating a new one. You can focus on your tasks because you don't have to think of their priorities and due dates once you start today's tasks. You can work on and complete each task from the top of the list.

## Technologies used

- Python
- Flask
- Jinja
- SQLite3
- Tailwind CSS

## Contents

[Demonstration Video](https://www.youtube.com/watch?v=ZXRNvVoVqCE&t=43s)

**todo/index.html**<br>
This is a Plan Page and contains a form at the top with the input of a new task, a day, a due date, and a priority, where a due date and a priority are optional. Below it, all stored data of tasks are displayed, if any. This page is responsive. For a tablet and a larger screen size, each task is displayed in a single line, and the edit and the delete buttons have the labels "EDIT" and "DELETE." For the mobile device, those edit and delete buttons are displayed with icons for a better user experience.<br>

**todo/edit.html**<br>
The edit button on the Plan Page (index.html) redirects to this edit.html. This page is simplified, and only the chosen task is displayed. Once the edit button is clicked, it redirects back to the Plan Page.<br>

**list/list.html**<br>
This page shows all to-do lists when rendered. A user selects a day, and all tasks for the day are displayed with an edit button, a delete button, and a completed/uncompleted button. Below the list, there are two buttons. One is a "Plan More" button, and the other is a " Let's Call It A Day" button. The Plan More button redirects to the planning page, where you can add more tasks. The Let's Call It A Day button handles completed or uncompleted tasks. If a task is completed, the data is removed from the database. If not, the task is carried over to the following day.
This page is responsive. For a tablet and a larger screen size, each task is displayed in a single line, and the edit, the delete, and the complete/uncompleted buttons have the labels "EDIT," "DELETE," and "COMPLETE/UNCOMPLETED." For the mobile device, those edit and delete buttons are displayed with icons, and the complete/uncompleted with a check mark for a better user experience.<br>

## License

[CS50x](https://cs50.harvard.edu/x/2022/)
[Flask](https://flask.palletsprojects.com/en/2.2.x/)
[Tailwind CSS](https://tailwindcss.com/)
