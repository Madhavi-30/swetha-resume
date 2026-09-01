"""Generate an ATS-friendly single-column resume PDF for Swetha Gali."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)

OUTPUT = "Swetha_Gali_Resume.pdf"

DARK = HexColor("#1a1a1a")
ACCENT = HexColor("#000000")

styles = getSampleStyleSheet()

name_style = ParagraphStyle(
    "Name", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=20, leading=24, alignment=TA_CENTER, textColor=DARK, spaceAfter=2,
)
title_style = ParagraphStyle(
    "TitleLine", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=DARK, spaceAfter=2,
)
contact_style = ParagraphStyle(
    "Contact", parent=styles["Normal"], fontName="Helvetica",
    fontSize=9.5, leading=13, alignment=TA_CENTER, textColor=DARK, spaceAfter=1,
)
section_style = ParagraphStyle(
    "Section", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=11.5, leading=14, textColor=ACCENT, spaceBefore=10, spaceAfter=3,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=13.5, textColor=DARK, alignment=TA_LEFT, spaceAfter=3,
)
sub_style = ParagraphStyle(
    "Sub", parent=styles["Normal"], fontName="Helvetica-Bold",
    fontSize=10, leading=13, textColor=DARK, spaceBefore=4, spaceAfter=1,
)
sub_italic = ParagraphStyle(
    "SubItalic", parent=styles["Normal"], fontName="Helvetica-Oblique",
    fontSize=9.5, leading=12.5, textColor=DARK, spaceAfter=2,
)
bullet_style = ParagraphStyle(
    "Bullet", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=13.5, textColor=DARK, spaceAfter=2,
)


def hr():
    return HRFlowable(width="100%", thickness=0.8, color=DARK,
                      spaceBefore=2, spaceAfter=4, lineCap="round")


def section(title):
    return [Paragraph(title, section_style), hr()]


def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, bullet_style), leftIndent=6, value="•")
         for t in items],
        bulletType="bullet", start="•", leftIndent=14, bulletFontSize=9,
        spaceBefore=0, spaceAfter=0,
    )


doc = SimpleDocTemplate(
    OUTPUT, pagesize=letter,
    leftMargin=0.7 * inch, rightMargin=0.7 * inch,
    topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    title="Swetha Gali - Resume", author="Swetha Gali",
)

story = []

# Header
story.append(Paragraph("SWETHA GALI", name_style))
story.append(Paragraph("Junior Python Developer", title_style))
story.append(Paragraph("Bengaluru, Karnataka &nbsp;|&nbsp; +91-8008046293 &nbsp;|&nbsp; galiswetha2003@gmail.com", contact_style))
story.append(Paragraph(
    'LinkedIn: linkedin.com/in/swetha-reddy-gali-5176b7314 &nbsp;|&nbsp; GitHub: github.com/swetha-67',
    contact_style))
story.append(Spacer(1, 4))

# Summary
story += section("PROFESSIONAL SUMMARY")
story.append(Paragraph(
    "Computer Science Engineering graduate with strong foundational knowledge in Python, SQL, "
    "OOP, DBMS, REST APIs, HTML and CSS. Hands-on experience developing academic projects "
    "involving web applications, backend functionality and database integration. Seeking a "
    "Junior Python Developer role to apply programming skills and build scalable software solutions.",
    body_style))

# Technical Skills
story += section("TECHNICAL SKILLS")
skills = [
    "<b>Programming:</b> Python, Java",
    "<b>Web Technologies:</b> HTML, CSS, JavaScript",
    "<b>Backend:</b> Python, REST APIs, Django/Flask",
    "<b>Databases:</b> MySQL, SQL, MongoDB",
    "<b>Tools:</b> Git, GitHub, VS Code",
    "<b>Core Concepts:</b> OOP, Data Structures, DBMS, CRUD Operations, Exception Handling",
]
for s in skills:
    story.append(Paragraph(s, body_style))

# Projects
story += section("PROJECTS")

story.append(Paragraph("E-Commerce Web Application", sub_style))
story.append(Paragraph("Technologies: Python, Django/Flask, REST API, MySQL, HTML, CSS, JavaScript", sub_italic))
story.append(bullets([
    "Developed an e-commerce web application with product browsing, user management, cart and order functionality.",
    "Implemented backend APIs and database operations for managing products, users and orders.",
    "Integrated frontend components with backend services to support smooth application workflows.",
]))

story.append(Paragraph("Student Dashboard Mobile Application", sub_style))
story.append(Paragraph("Technologies: Python, REST API, MySQL/MongoDB", sub_italic))
story.append(bullets([
    "Developed backend functionality for a student dashboard application to manage student-related information.",
    "Implemented API-based communication for retrieving and managing student data.",
    "Designed database operations for efficient storage and retrieval of application data.",
]))

# Education
story += section("EDUCATION")
story.append(Paragraph("Bachelor of Technology (B.Tech) &ndash; Computer Science &amp; Engineering", sub_style))
story.append(Paragraph("Sri Venkateshwara Institute of Technology (SVIT) &nbsp;|&nbsp; 2025", sub_italic))

# Certifications
story += section("CERTIFICATIONS")
story.append(bullets([
    "Python Programming",
    "SQL / Database Management",
    "Web Development",
    "Git &amp; GitHub",
]))

# Soft Skills
story += section("SOFT SKILLS")
story.append(Paragraph(
    "Problem Solving &nbsp;•&nbsp; Communication &nbsp;•&nbsp; Team Collaboration "
    "&nbsp;•&nbsp; Quick Learning &nbsp;•&nbsp; Adaptability", body_style))

doc.build(story)
print("Wrote", OUTPUT)
