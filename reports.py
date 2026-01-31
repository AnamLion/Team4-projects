# reports.py
from datetime import datetime

class ReportGenerator:
    def __init__(self, storage):
        self.storage = storage
        self.trans_sheet = "Transactions"
        self.due_days = 7
        self.fine_per_day = 10

    def view_active_issues(self):
        """Shows a list of all books that are currently issued."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.trans_sheet)

        print("\nACTIVE ISSUED BOOKS\n")
        found = False
        count = 0
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            trans_id, mem_id, book_id, issue_date, return_date, fine = row
            if return_date is None or return_date == "":
                print(f"Trans ID: {trans_id} | Member: {mem_id} | Book: {book_id} | Issued: {issue_date}")
                found = True
                count += 1

        if not found:
            print("[INFO] No active issued books found (All returned).")
        else:
            print(f"\nTotal Books Currently Issued: {count}")
        print()

    def view_overdue_books(self):
        """Shows books that have exceeded the due limit and are still with the member."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.trans_sheet)

        print("\nOVERDUE (LATE) BOOKS\n")
        found = False
        today = datetime.today()
        total_estimated_fine = 0

        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            trans_id, mem_id, book_id, issue_date_raw, return_date, fine = row

            if return_date is None or return_date == "":
                try:
                    if isinstance(issue_date_raw, datetime):
                        issue_date = issue_date_raw
                    elif isinstance(issue_date_raw, str):
                        issue_date = datetime.strptime(issue_date_raw, "%Y-%m-%d")
                    else:
                        continue
                    
                    days_passed = (today - issue_date).days
                    if days_passed > self.due_days:
                        extra_days = days_passed - self.due_days
                        estimated_fine = extra_days * self.fine_per_day
                        total_estimated_fine += estimated_fine
                        print(f"LATE! Member: {mem_id} | Book: {book_id} | Days Late: {extra_days} | Est. Fine: ₹{estimated_fine}")
                        found = True
                except ValueError:
                    continue

        if not found:
            print("No overdue books found.")
        else:
            print(f"Total Estimated Fine: ₹{total_estimated_fine}")
        print()

    def view_total_fine(self):
        """Calculates the total fine collected from returned books."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.trans_sheet)

        total_fine = 0
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            fine = row[5]
            if fine is not None and isinstance(fine, (int, float)):
                total_fine += fine

        print(f"\nTOTAL FINE COLLECTED")
        print(f"Total Amount: ₹{total_fine}")
        print("------------------------------\n")

    def reports_menu(self):
        """Displays the Reports menu."""
        while True:
            print("REPORTS MENU")
            print("1. View Active Issues (Books with members)")
            print("2. View Overdue Books (Late list)")
            print("3. View Total Fine Collected")
            print("4. Back to Main Menu")

            choice = input("Enter choice: ")
            if choice == "1":
                self.view_active_issues()
            elif choice == "2":
                self.view_overdue_books()
            elif choice == "3":
                self.view_total_fine()
            elif choice == "4":
                break
            else:
                print("\n Invalid choice. Try again.\n")