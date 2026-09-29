# Project Statement - Roomie Harmony

## Problem Statement
Shared living among roommates often leads to friction over financial transparency and non-uniform division of household chores. Manual tracking leads to miscommunication, unequal work distribution, and lost expense records. There is a need for a lightweight, transparent system that automates chore distribution fairly and keeps a clear record of shared expenses without requiring complex setups or heavy applications.

## Scope of the Project
Roomie Harmony provides a lightweight, local CLI application focused on solving daily flat management problems[cite: 3]. 
The scope includes:
* Managing user profiles for household members[cite: 1, 3].
* Recording shared financial transactions with export functionality[cite: 1, 2, 3].
* Assigning chores through custom algorithmic rotation rules[cite: 3, 5].
* Reverting recent mistakes using stack-based history tracking[cite: 3, 5].

*Out of Scope:* Real-time cloud sync, payment gateway integration, and multi-tenant web/mobile frontends.

## Target Users
* University students sharing apartments or hostel rooms.
* Working professionals living in shared accommodations.
* Small households seeking a transparent way to divide duties and expenses.

## High-Level Features
* **User & Household Management:** Add and store roommate details locally using SQLite[cite: 1, 3].
* **Expense Recording & CSV Export:** Track spending per user and generate downloadable CSV financial summaries[cite: 1, 2, 3].
* **Round-Robin Chore Queue:** Distribute chores fairly among roommates using a FIFO queue structure[cite: 3, 5].
* **Stack-Based Action Undo:** Maintain an internal stack to easily undo recent actions[cite: 3, 5].
* **Persistent Storage & Logging:** Save application data to an SQLite database (`data/app_database.db`) and write activity logs to `data/activity_log.txt`[cite: 1, 2, 3].
