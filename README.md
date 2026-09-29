# roommate-expense-chore-manager
# Roomie Harmony - CLI Roommate & Expense Manager

## Overview
Roomie Harmony is a command-line interface (CLI) application built in Python to help flatmates manage shared living spaces efficiently. It simplifies tracking shared expenses, distributes daily chores fairly among housemates using core data structures, and logs activity for complete transparency[cite: 1, 2, 3].

## Features
* **Roommate Registration:** Register flatmates into the system to manage expenses and assignments.
* **Shared Expense Tracking:** Log expenses with payer details, amounts (in INR), and descriptions[cite: 2, 3, 4].
* **Fair Chore Assignment:** Rotates chore assignments automatically among registered roommates using a Queue data structure.
* **Chore Status Management:** Mark assigned chores as completed and track pending items[cite: 3, 4].
* **Action Undo System:** Revert recent operations like adding users or expenses using a Stack data structure.
* **Financial Data Export:** Export recorded expenses to a CSV file for record-keeping.
* **System Logging:** Maintain an audit log of system actions in a plain text file[cite: 2, 3].

## Technologies/Tools Used
* **Programming Language:** Python 3.x[cite: 1, 2, 3, 4, 5]
* **Database:** SQLite3[cite: 1]
* **Built-in Modules:** `csv`, `os`, `sys`[cite: 2, 3]
* **Data Structures:** Custom Stack (`ActionStack`) and Queue (`ChoreQueue`) implementations[cite: 3, 5]

## Steps to Install & Run the Project

### Prerequisites
* Python 3.8 or higher installed on your system.

### Running the Application
1. Clone this repository or download the source files:
   ```bash
   git clone [https://github.com/your-username/roomie-harmony.git](https://github.com/your-username/roomie-harmony.git)
   cd roomie-harmony
