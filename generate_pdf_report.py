from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import pandas as pd

# Load the summary CSV
df = pd.read_csv("breach_summary_report.csv")

# Create PDF
doc = SimpleDocTemplate("breach_summary_report.pdf", pagesize=A4)
elements = []

styles = getSampleStyleSheet()
title = Paragraph("Breach Summary Report", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 12))

# Convert DataFrame to list of lists (including headers)
data = [df.columns.tolist()] + df.values.tolist()

# Create table
table = Table(data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
]))

elements.append(table)

# Build PDF
doc.build(elements)
print("✅ PDF report saved as 'breach_summary_report.pdf'")

