"""
Author: Amelia Cortez
Date Written: 7/12/24
Assignment: Finale Project
This is a module of the reimbursement generator GUI that will generate reports with Word
"""

from docxtpl import DocxTemplate

doc = DocxTemplate("reimbursement_template.docx")

expense_list = [[3, "Breakfast Per Diem", 16.00, 48.00],
                [3, "Lunch Per Diem", 24.00, 72.00],
                [2, "Dinner Per Diem", 26.00, 52.00]]

doc.render({"name":"amelia",
            "location":"PHM 2025",
            "expense_list": expense_list,
            "total":9})
doc.save("new_reimbursement.docx")