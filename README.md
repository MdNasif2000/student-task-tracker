<h1 text-align = "center"> Student Task Tracker <h1/>

![Banner](banner.png)

A lightweight Python console application for managing daily tasks. Built using Object-Oriented Programming (OOP), persistent JSON storage, and standard Python modules.

---

## Features

- Add new tasks (title + description) with created timestamp  
- View all saved tasks with IDs and timestamps  
- Update task title and/or description — records updated timestamp  
- Delete tasks with confirmation  
- Persistent storage using a JSON file (`src/tasks.json`)  
- Unique numeric ID generation for each task  
- Robust error handling for file operations and user input

---

## Installation

### Prerequisites

- Python 3.8 or newer is recommended.

No external packages are required — the application only uses Python standard library modules (`json`, `datetime`, `random`).

### Clone the repository

```bash
git clone https://github.com/<your-username>/student-task-tracker.git
cd student-task-tracker
```

---

## How to run

Run the application from the project root:

```bash
python src/main.py
```

You will see a menu:

```
===== Student Task Tracker =====

1. Add New Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Exit
```

Choose an option by entering the corresponding number.

### Notes

- Tasks are saved automatically to `src/tasks.json` after all operations.
- `tasks.json` will be created automatically if it doesn't exist.
- Do **not** commit `src/tasks.json` to version control; it holds local data.

---


## Data Storage Format (tasks.json)

Tasks are stored in JSON array form. Example:

```json
[
    {
        "id": 123456,
        "title": "Study Python",
        "description": "Finish module requests",
        "created_at": "YYYY-MM-DD HH:MM:SS",
        "updated_at": "YYYY-MM-DD HH:MM:SS"
    }
]
```

`updated_at` is present only if the task has been updated.


## License

This project is licensed under the MIT License — a permissive open-source license that allows personal and commercial use, modification, and distribution.
See the LICENSE file for full details.
