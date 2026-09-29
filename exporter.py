import csv

class ReportExporter:
    @staticmethod
    def export_expenses_to_csv(expenses_data, file_path="exports/monthly_report.csv"):
        """Exports expenses to CSV file using standard file handling."""
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Expense ID", "Payer ID", "Amount (INR)", "Description"])
            for row in expenses_data:
                writer.writerow(row)
        print(f"\n[+] Export successful! Saved to {file_path}")

    @staticmethod
    def log_action(message, log_path="data/activity_log.txt"):
        """Appends system events into a plain text file."""
        with open(log_path, mode="a", encoding="utf-8") as log_file:
            log_file.write(f"{message}\n")
