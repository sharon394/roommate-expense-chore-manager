# roommate-expense-chore-manager
Roomie Harmony is a Python-based command-line interface (CLI) application designed to streamline shared living management for flatmates and roommates. It simplifies daily household co-living challenges—such as splitting expenses and assigning chores fairly—by leveraging core computer science principles and data structures.
# Roomie Harmony 🏠

**Roomie Harmony** is a Python-based Command-Line Interface (CLI) application designed to streamline shared household management for roommates and flatmates. It simplifies daily co-living management by automating fair chore rotation, tracking shared financial expenses, maintaining activity logs, and exporting report files.

---

## 🚀 Key Features

- **Fair Chore Queueing**: Automates chore distribution using a round-robin rotation algorithm to ensure equitable task assignment among roommates.
- **Shared Expense Tracker**: Records payments and expense details tied to individual roommates in a centralized database.
- **Undo Functionality**: Implements an action stack to allow users to reverse recent operations seamlessly.
- **Financial CSV Export**: Generates readable CSV financial reports for expense reviews and bookkeeping.
- **Persistent Storage**: Utilizes SQLite for reliable, multi-table local data storage across sessions.
- **Activity Logging**: Maintains plain-text activity logs recording system operations.

---

## 🛠️ Technology Stack & Core Concepts

- **Language**: Python 3.x
- **Database**: SQLite3
- **Data Structures**:
  - **Queue (`ChoreQueue`)**: For round-robin chore assignment.
  - **Stack (`ActionStack`)**: For execution tracking and LIFO undo functionality.
- **File I/O**: Native Python CSV and text handling for logging and exports.

---

## 📁 Repository Structure

```text
.
├── main.py           # Application entry point and CLI menu interface
├── db_manager.py     # SQLite database connection and operations
├── models.py         # Data models (User, Expense, Chore)
├── structures.py     # Custom data structures (ActionStack, ChoreQueue)
├── exporter.py       # CSV reporting and text activity logging
├── data/             # Local database and system logs directory
└── exports/          # Generated CSV reports directory
