from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def create_pdf(report_data, output_path="benchmarks/benchmark_report.pdf"):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 14)
    c.drawString(50, height - 50, "TCP Server Benchmark Report")
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 70, f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    y = height - 100
    for line in report_data.split('\n'):
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 15

    c.save()
    print(f"✅ Benchmark report generated: {output_path}")

if __name__ == "__main__":
    with open("benchmarks/benchmark.log") as f:
        report_data = f.read()

    create_pdf(report_data)
