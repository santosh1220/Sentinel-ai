from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


output_path = Path("data/security_policy.pdf")
output_path.parent.mkdir(parents=True, exist_ok=True)

pdf = canvas.Canvas(str(output_path), pagesize=letter)

# Page 1
pdf.setFont("Helvetica", 14)
pdf.drawString(72, 740, "SentinelAI Sample Security Policy")
pdf.setFont("Helvetica", 11)
pdf.drawString(
    72,
    700,
    "Employees must report phishing emails to the security team immediately.",
)
pdf.showPage()

# Page 
pdf.setFont("Helvetica", 14)
pdf.drawString(72, 740, "Incident Reporting")
pdf.setFont("Helvetica", 11)
pdf.drawString(
    72,
    700,
    "Security incidents must be reported to the SOC within 30 minutes.",
)
pdf.save()

print(f"Created PDF: {output_path}")