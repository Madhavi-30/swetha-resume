"""Generate an ATS-friendly resume PDF for Swetha Gali (Software Engineer / Java Full Stack)."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)

OUTPUT = "Swetha_Gali_Resume_SoftwareEngineer.pdf"

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
    fontSize=11.5, leading=13, textColor=ACCENT, spaceBefore=6, spaceAfter=2,
)
body_style = ParagraphStyle(
    "Body", parent=styles["Normal"], fontName="Helvetica",
    fontSize=10, leading=12.8, textColor=DARK, alignment=TA_LEFT, spaceAfter=2,
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
    fontSize=10, leading=12.8, textColor=DARK, spaceAfter=1,
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
    topMargin=0.45 * inch, bottomMargin=0.45 * inch,
    title="Swetha Gali - Software Engineer Resume", author="Swetha Gali",
)

story = []

# Header
story.append(Paragraph("SWETHA GALI", name_style))
story.append(Paragraph("Software Engineer &nbsp;|&nbsp; Java Full Stack Developer", title_style))
story.append(Paragraph("Bengaluru, India &nbsp;|&nbsp; +91-8008046293 &nbsp;|&nbsp; galiswetha2003@gmail.com", contact_style))
story.append(Paragraph(
    "LinkedIn: linkedin.com/in/swetha-reddy-gali-5176b7314 &nbsp;|&nbsp; GitHub: github.com/swetha-67",
    contact_style))
story.append(Spacer(1, 4))

# Summary
story += section("PROFESSIONAL SUMMARY")
story.append(Paragraph(
    "Computer Science graduate with hands-on experience in Java Full Stack development through "
    "internship and academic projects. Skilled in Java, MySQL, HTML, CSS, and JavaScript "
    "fundamentals. Strong understanding of object-oriented programming, database concepts, and "
    "web development. Quick learner with good problem-solving and adaptability skills, seeking an "
    "entry-level Software Engineer opportunity.",
    body_style))

# Technical Skills
story += section("TECHNICAL SKILLS")
skills = [
    "<b>Programming:</b> Java, Python",
    "<b>Web Technologies:</b> HTML5, CSS3, JavaScript",
    "<b>Database:</b> MySQL",
    "<b>Core Concepts:</b> OOP, DBMS, SQL, Data Structures",
    "<b>Tools:</b> Git, GitHub, Eclipse/IntelliJ IDEA",
]
for s in skills:
    story.append(Paragraph(s, body_style))

# Education
story += section("EDUCATION")
story.append(Paragraph("B.Tech &ndash; Computer Science and Engineering", sub_style))
story.append(Paragraph("Sri Venkateswara Institute of Technology &nbsp;|&nbsp; 2021 &ndash; 2025 &nbsp;|&nbsp; CGPA: 84", sub_italic))

# Internship
story += section("INTERNSHIP")
story.append(Paragraph("Java Full Stack Development Intern", sub_style))
story.append(Paragraph("SkillDzire", sub_italic))
story.append(bullets([
    "Developed responsive web pages using HTML, CSS, and JavaScript.",
    "Worked with Java programming and object-oriented programming concepts.",
    "Practiced database operations using MySQL and SQL queries.",
    "Gained exposure to frontend and backend development workflows.",
]))

# Projects
story += section("PROJECTS")

story.append(Paragraph("Student Dashboard Mobile Application", sub_style))
story.append(Paragraph("Role: Backend Developer", sub_italic))
story.append(bullets([
    "Developed backend functionality for a student dashboard application.",
    "Worked with database operations for storing and retrieving student information.",
    "Implemented features to support student data management.",
]))

story.append(Paragraph("E-Commerce Web Application", sub_style))
story.append(bullets([
    "Developed an e-commerce website with user-friendly web pages.",
    "Implemented product listing and basic shopping functionality.",
    "Used HTML, CSS, JavaScript, Java, and MySQL concepts.",
    "Focused on responsive design and simple user navigation.",
]))

# Certifications
story += section("CERTIFICATIONS")
story.append(bullets([
    "Certified in Cloud Computing &ndash; NPTEL",
    "Java Full Stack Web Development Certification &ndash; TAP Academy",
]))

# Soft Skills
story += section("SOFT SKILLS")
story.append(Paragraph(
    "Problem Solving &nbsp;•&nbsp; Quick Learning &nbsp;•&nbsp; Adaptability "
    "&nbsp;•&nbsp; Communication &nbsp;•&nbsp; Teamwork", body_style))

# Interests
story += section("INTERESTS")
story.append(Paragraph("Photography", body_style))

doc.build(story)
print("Wrote", OUTPUT)
