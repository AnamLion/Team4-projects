# backup.py
import os
import shutil
import datetime

class BackupManager:
    def __init__(self, backup_dir="backups", files_to_backup=["library.xlsx", "users.xlsx"]):
        self.backup_dir = backup_dir
        self.files_to_backup = files_to_backup

    def ensure_backup_dir(self):
        """Ensures the main backup directory exists."""
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)

    def backup_data(self):
        """Creates a timestamped backup of the data files."""
        self.ensure_backup_dir()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        current_backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")
        
        try:
            os.makedirs(current_backup_path)
            files_backed_up = 0
            for filename in self.files_to_backup:
                if os.path.exists(filename):
                    shutil.copy2(filename, current_backup_path)
                    files_backed_up += 1
                else:
                    print(f"WARNING {filename} not found, skipping.")
            
            if files_backed_up > 0:
                print(f"\nSUCCESS Backup created at: {current_backup_path}")
            else:
                print("\nERROR No files were found to backup.")
        except Exception as e:
            print(f"\nERROR Failed to create backup: {e}")

    def list_backups(self):
        """Returns a list of available backup folders, sorted newest first."""
        self.ensure_backup_dir()
        backups = [d for d in os.listdir(self.backup_dir) if os.path.isdir(os.path.join(self.backup_dir, d))]
        backups.sort(reverse=True)
        return backups

    def restore_data(self):
        """Restores data files from a selected backup."""
        backups = self.list_backups()
        if not backups:
            print("\nINFO No backups available to restore.")
            return

        print("\nAvailable Backups:")
        for idx, folder_name in enumerate(backups):
            print(f"{idx + 1}. {folder_name}")
        
        choice = input("\nEnter backup number to restore (or 'c' to cancel): ")
        if choice.lower() == 'c':
            return

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(backups):
                selected_backup = backups[idx]
                source_path = os.path.join(self.backup_dir, selected_backup)
                
                confirm = input(f"Are you sure you want to restore from '{selected_backup}'? \nThis will OVERWRITE current data. (y/n): ")
                if confirm.lower() != 'y':
                    print("[INFO] Restore cancelled.")
                    return

                print("Restoring...")
                restored_count = 0
                for filename in self.files_to_backup:
                    source_file = os.path.join(source_path, filename)
                    if os.path.exists(source_file):
                        shutil.copy2(source_file, ".")
                        print(f" - Restored {filename}")
                        restored_count += 1
                
                if restored_count > 0:
                    print("\n[SUCCESS] Restore complete.")
                else:
                    print("\n[WARNING] No valid data files found in this backup.")
            else:
                print("[ERROR] Invalid selection.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")
        except Exception as e:
            print(f"\n[ERROR] Restore failed: {e}")

    def backup_menu(self):
        """Displays the backup sub-menu."""
        while True:
            print("\nBACKUP & RESTORE MENU")
            print("1. Create Backup")
            print("2. Restore Data")
            print("3. List Backups")
            print("4. Back to Main Menu")
            
            choice = input("Enter choice: ")
            if choice == "1":
                self.backup_data()
            elif choice == "2":
                self.restore_data()
            elif choice == "3":
                backups = self.list_backups()
                if backups:
                    print("\nExisting Backups:")
                    for b in backups:
                        print(f" - {b}")
                else:
                    print("\n[INFO] No backups found.")
            elif choice == "4":
                break
            else:
                print("[ERROR] Invalid choice.")
