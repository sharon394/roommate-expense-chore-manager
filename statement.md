# Problem Statement & System Design: Roomie Harmony

## 🎯 Problem Statement

Living with roommates often introduces friction around shared responsibilities and financial management. Common challenges include:
1. **Inequitable Chore Distribution**: Unclear chore assignments lead to unequal workloads or forgotten household tasks.
2. **Opaque Expense Tracking**: Difficulty tracking who paid for shared household supplies (e.g., groceries, utility bills) and calculating fair settlements.
3. **Lack of Transparency & Auditability**: Absence of simple records showing recent system activities, assigned duties, or financial transactions.

**Roomie Harmony** solves these challenges by providing a centralized CLI application that automates fair task rotation, manages persistent financial records, provides undo safety mechanisms, and enables data exports[cite: 1, 2, 3, 5].

---

## 💡 System Design & Architecture

The application is built using modular Python code separated into data access, domain models, custom data structures, and file export components[cite: 1, 2, 3, 4, 5].
