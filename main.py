import sys
import os

# Ensure modules directory is discoverable
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# NEW IMPORTS (For single-folder setup)
from db_manager import DatabaseManager
from structures import ActionStack, ChoreQueue
from exporter import ReportExporter

def display_menu():
    print("\n==========================================")
    print("      ROOMIE HARMONY - CLI MANAGER       ")
    print("==========================================")
    print("1. Register Roommate")
    print("2. Add Shared Expense")
    print("3. Assign Chore (Queue System)")
    print("4. Complete Chore")
    print("5. View All Chores")
    print("6. Undo Last Action (Stack System)")
    print("7. Export Financial Report (CSV)")
    print("8. Exit")
    print("==========================================")

def main():
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    os.makedirs("exports", exist_ok=True)

    db = DatabaseManager()
    undo_stack = ActionStack()
    chore_queue = ChoreQueue()

    # Load initial roommates into queue
    users = db.get_all_users()
    for user in users:
        chore_queue.enqueue(user[1])

    while True:
        display_menu()
        choice = input("Enter option (1-8): ").strip()

        if choice == '1':
            name = input("Enter Roommate Name: ").strip()
            if name:
                db.add_user(name)
                chore_queue.enqueue(name)
                undo_stack.push(("USER", name))
                ReportExporter.log_action(f"Added User: {name}")
                print(f"[Success] Added {name} to system.")

        elif choice == '2':
            users = db.get_all_users()
            if not users:
                print("[!] Register roommates first.")
                continue
            print("\nRoommates:")
            for u in users:
                print(f"ID: {u[0]} | Name: {u[1]}")
            try:
                payer_id = int(input("Enter Payer ID: "))
                amount = float(input("Enter Expense Amount: "))
                desc = input("Enter Description: ")
                db.add_expense(payer_id, amount, desc)
                undo_stack.push(("EXPENSE", desc))
                ReportExporter.log_action(f"Added Expense: {desc} ({amount})")
                print("[Success] Expense Recorded.")
            except ValueError:
                print("[Error] Invalid numeric input.")

        elif choice == '3':
            if chore_queue.is_empty():
                print("[!] Register roommates to assign chores.")
                continue
            chore_name = input("Enter Chore Description: ").strip()
            try:
                weight = int(input("Enter Effort Weight (1-5): "))
            except ValueError:
                weight = 1
            
            assigned_user = chore_queue.rotate()
            db.add_chore(chore_name, assigned_user, weight)
            print(f"[Success] '{chore_name}' assigned to {assigned_user}!")

        elif choice == '4':
            chores = db.get_chores()
            print("\nPending Chores:")
            for c in chores:
                if not c[4]:  # If not completed
                    print(f"Chore ID: {c[0]} | {c[1]} (Assigned to: {c[2]})")
            try:
                c_id = int(input("Enter Chore ID to mark completed: "))
                db.mark_chore_done(c_id)
                print("[Success] Chore marked as completed.")
            except ValueError:
                print("[Error] Invalid input.")

        elif choice == '5':
            chores = db.get_chores()
            print("\n--- CHORE LIST ---")
            for c in chores:
                status = "Done" if c[4] else "Pending"
                print(f"[{status}] ID {c[0]}: {c[1]} -> Assigned: {c[2]} (Weight: {c[3]})")

        elif choice == '6':
            last_action = undo_stack.pop()
            if last_action:
                print(f"[Undo] Reverted last recorded action: {last_action}")
            else:
                print("[!] No actions to undo.")

        elif choice == '7':
            cursor = db.conn.cursor()
            cursor.execute("SELECT * FROM expenses")
            data = cursor.fetchall()
            ReportExporter.export_expenses_to_csv(data)

        elif choice == '8':
            db.close()
            print("Exiting RoomieHarmony. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()
