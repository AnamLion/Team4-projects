# main.py
from storage import LibraryStorage
from login import AuthManager
from books import BookManager
from members import MemberManager
from transactions import TransactionManager
from reports import ReportGenerator
from backup import BackupManager

class LibraryApp:
    def __init__(self):
        # Initialize Core Storage
        self.storage = LibraryStorage()
        
        # Initialize Managers
        self.auth_manager = AuthManager()
        self.book_manager = BookManager(self.storage)
        self.member_manager = MemberManager(self.storage)
        self.transaction_manager = TransactionManager(self.storage)
        self.report_generator = ReportGenerator(self.storage)
        self.backup_manager = BackupManager()

    def run(self):
        """Orchestrates the application flow."""
        while True:
            # 1. Login Phase
            user_role = self.auth_manager.login_menu()

            if user_role:
                # 2. Main Menu Phase
                self.show_main_menu(user_role)
            else:
                # Exit
                print("\n[INFO] Exiting system. Goodbye!")
                break

    def show_main_menu(self, user_role):
        """Handles the main menu routing."""
        while True:
            print(f"\nMAIN MENU ({user_role})")
            print("1. Books Menu")
            print("2. Members Menu")
            print("3. Transactions Menu")
            print("4. Reports Menu")
            print("5. Backup/Restore")
            print("6. Logout")
            
            choice = input("Enter choice: ")

            if choice == "1":
                self.book_manager.books_menu()
            elif choice == "2":
                self.member_manager.members_menu()
            elif choice == "3":
                self.transaction_manager.transactions_menu()
            elif choice == "4":
                self.report_generator.reports_menu()
            elif choice == "5":
                self.backup_manager.backup_menu()
            elif choice == "6":
                print("\nLogging out...\n")
                break
            else:
                print("\n[ERROR] Invalid choice. Please try again.\n")

if __name__ == "__main__":
    app = LibraryApp()
    app.run()
