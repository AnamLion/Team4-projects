# members.py
from models import Member

class MemberManager:
    def __init__(self, storage):
        self.storage = storage
        self.sheet_name = "Members"

    def generate_member_id(self, ws):
        """Generates a simple incremental Member ID."""
        last_row = ws.max_row
        if last_row <= 1:
            return 1001  # Start from 1001
        last_id = ws.cell(row=last_row, column=1).value
        try:
            return int(last_id) + 1
        except (TypeError, ValueError):
            return 1001

    def add_member(self):
        """Adds a new library member to Excel."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        name = input("Enter Member Name: ")
        phone = input("Enter Phone Number: ")

        member_id = self.generate_member_id(ws)
        member = Member(member_id, name, phone)

        ws.append([
            member.member_id,
            member.name,
            member.phone,
            member.books_issued
        ])

        self.storage.save_workbook(wb)
        print(f"\n[SUCCESS] Member added successfully.")
        print(f"Member ID: {member.member_id}\n")

    def view_members(self):
        """Displays all members in a readable format."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        print("\nLIBRARY MEMBERS\n")
        if ws.max_row <= 1:
            print("[INFO] No members found.\n")
            return

        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            member_id, name, phone, books_issued = row
            print(f"ID: {member_id} | Name: {name} | Phone: {phone} | Books Issued: {books_issued}")
        print()

    def search_member(self):
        """Searches for a member by MemberID."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        search_id = input("Enter Member ID to search: ")
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            member_id, name, phone, books_issued = row
            if str(member_id) == search_id:
                print("\nMember Found:")
                print(f"ID: {member_id} | Name: {name} | Phone: {phone} | Books Issued: {books_issued}\n")
                return

        print("\n[INFO] Member not found.\n")

    def delete_member(self):
        """Deletes a member ONLY if they have no active issued books."""
        wb = self.storage.get_workbook()
        ws = self.storage.get_sheet(wb, self.sheet_name)

        delete_id = input("Enter Member ID to delete: ")

        # 1. Check for Active Transactions
        if "Transactions" in wb.sheetnames:
            ws_trans = wb["Transactions"]
            for row in ws_trans.iter_rows(min_row=2, values_only=True):
                if not any(row): continue
                t_mem_id = str(row[1])
                t_return_date = row[4]
                if t_mem_id == delete_id and (t_return_date is None or t_return_date == ""):
                    print(f"\n[ERROR] Cannot delete Member {delete_id}. They still have a book issued!")
                    return

        # 2. Proceed with deletion
        found = False
        rows_to_keep = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            if not any(row): continue
            member_id = str(row[0])
            if member_id != delete_id:
                rows_to_keep.append(row)
            else:
                found = True

        if not found:
            print("\n[ERROR] Member not found.\n")
            return

        # Clear and Rewrite
        ws.delete_rows(2, ws.max_row)
        for row in rows_to_keep:
            ws.append(list(row))

        try:
            self.storage.save_workbook(wb)
            print("\n[SUCCESS] Member deleted successfully.\n")
        except PermissionError:
            print("\n[ERROR] Close 'library.xlsx' and try again!")

    def members_menu(self):
        """Displays the Members menu and routes user choices."""
        while True:
            print("MEMBERS MENU")
            print("1. Add Member")
            print("2. View Members")
            print("3. Search Member")
            print("4. Delete Member")
            print("5. Back to Main Menu")

            choice = input("Enter choice: ")
            if choice == "1":
                self.add_member()
            elif choice == "2":
                self.view_members()
            elif choice == "3":
                self.search_member()
            elif choice == "4":
                self.delete_member()
            elif choice == "5":
                break
            else:
                print("\n[ERROR] Invalid choice. Try again.\n")
