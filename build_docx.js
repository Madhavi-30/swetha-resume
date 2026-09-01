// Generate ATS-friendly .docx versions of both resumes for Swetha Gali.
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle,
  LevelFormat, HeadingLevel,
} = require("docx");

const FONT = "Calibri";
const DARK = "1A1A1A";

// ---- helpers ---------------------------------------------------------------
function name(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 20 },
    children: [new TextRun({ text, bold: true, size: 40, font: FONT, color: DARK })],
  });
}
function centerLine(text, opts = {}) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: opts.after ?? 20 },
    children: [new TextRun({ text, size: opts.size ?? 19, font: FONT, color: DARK })],
  });
}
function section(text) {
  return new Paragraph({
    spacing: { before: 160, after: 40 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, space: 2, color: DARK } },
    children: [new TextRun({ text, bold: true, size: 23, font: FONT, color: DARK })],
  });
}
function body(runs, opts = {}) {
  const children = Array.isArray(runs) ? runs : [runs];
  return new Paragraph({
    spacing: { after: opts.after ?? 40 },
    children: children.map((r) =>
      typeof r === "string"
        ? new TextRun({ text: r, size: 20, font: FONT, color: DARK })
        : new TextRun({ size: 20, font: FONT, color: DARK, ...r })
    ),
  });
}
function subhead(text) {
  return new Paragraph({
    spacing: { before: 60, after: 10 },
    children: [new TextRun({ text, bold: true, size: 20, font: FONT, color: DARK })],
  });
}
function italicLine(text) {
  return new Paragraph({
    spacing: { after: 30 },
    children: [new TextRun({ text, italics: true, size: 19, font: FONT, color: DARK })],
  });
}
function bullet(text) {
  return new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 20 },
    children: [new TextRun({ text, size: 20, font: FONT, color: DARK })],
  });
}

const numbering = {
  config: [{
    reference: "bullets",
    levels: [{
      level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
      style: { paragraphProperties: { indent: { left: 360, hanging: 220 } } },
    }],
  }],
};

const pageProps = {
  page: {
    size: { width: 12240, height: 15840 }, // US Letter
    margin: { top: 720, bottom: 720, left: 1008, right: 1008 }, // 0.5" / 0.7"
  },
};

function build(sectionsChildren, outFile, docTitle) {
  const doc = new Document({
    creator: "Swetha Gali",
    title: docTitle,
    numbering,
    styles: { default: { document: { run: { font: FONT, color: DARK } } } },
    sections: [{ properties: pageProps, children: sectionsChildren }],
  });
  return Packer.toBuffer(doc).then((buf) => {
    fs.writeFileSync(outFile, buf);
    console.log("Wrote", outFile);
  });
}

// ---- Resume 1: Junior Python Developer -------------------------------------
function pythonResume() {
  const c = [];
  c.push(name("SWETHA GALI"));
  c.push(centerLine("Junior Python Developer"));
  c.push(centerLine("Bengaluru, Karnataka  |  +91-8008046293  |  galiswetha2003@gmail.com"));
  c.push(centerLine("LinkedIn: linkedin.com/in/swetha-reddy-gali-5176b7314  |  GitHub: github.com/swetha-67", { after: 60 }));

  c.push(section("PROFESSIONAL SUMMARY"));
  c.push(body(
    "Computer Science Engineering graduate with strong foundational knowledge in Python, SQL, " +
    "OOP, DBMS, REST APIs, HTML and CSS. Hands-on experience developing academic projects " +
    "involving web applications, backend functionality and database integration. Seeking a " +
    "Junior Python Developer role to apply programming skills and build scalable software solutions."
  ));

  c.push(section("TECHNICAL SKILLS"));
  [["Programming: ", "Python, Java"],
   ["Web Technologies: ", "HTML, CSS, JavaScript"],
   ["Backend: ", "Python, REST APIs, Django/Flask"],
   ["Databases: ", "MySQL, SQL, MongoDB"],
   ["Tools: ", "Git, GitHub, VS Code"],
   ["Core Concepts: ", "OOP, Data Structures, DBMS, CRUD Operations, Exception Handling"]]
    .forEach(([k, v]) => c.push(body([{ text: k, bold: true }, { text: v }])));

  c.push(section("PROJECTS"));
  c.push(subhead("E-Commerce Web Application"));
  c.push(italicLine("Technologies: Python, Django/Flask, REST API, MySQL, HTML, CSS, JavaScript"));
  c.push(bullet("Developed an e-commerce web application with product browsing, user management, cart and order functionality."));
  c.push(bullet("Implemented backend APIs and database operations for managing products, users and orders."));
  c.push(bullet("Integrated frontend components with backend services to support smooth application workflows."));
  c.push(subhead("Student Dashboard Mobile Application"));
  c.push(italicLine("Technologies: Python, REST API, MySQL/MongoDB"));
  c.push(bullet("Developed backend functionality for a student dashboard application to manage student-related information."));
  c.push(bullet("Implemented API-based communication for retrieving and managing student data."));
  c.push(bullet("Designed database operations for efficient storage and retrieval of application data."));

  c.push(section("EDUCATION"));
  c.push(subhead("Bachelor of Technology (B.Tech) – Computer Science & Engineering"));
  c.push(italicLine("Sri Venkateshwara Institute of Technology (SVIT)  |  2025"));

  c.push(section("CERTIFICATIONS"));
  ["Python Programming", "SQL / Database Management", "Web Development", "Git & GitHub"]
    .forEach((t) => c.push(bullet(t)));

  c.push(section("SOFT SKILLS"));
  c.push(body("Problem Solving  •  Communication  •  Team Collaboration  •  Quick Learning  •  Adaptability"));

  return build(c, "Swetha_Gali_Resume.docx", "Swetha Gali - Resume");
}

// ---- Resume 2: Software Engineer / Java Full Stack -------------------------
function seResume() {
  const c = [];
  c.push(name("SWETHA GALI"));
  c.push(centerLine("Software Engineer  |  Java Full Stack Developer"));
  c.push(centerLine("Bengaluru, India  |  +91-8008046293  |  galiswetha2003@gmail.com"));
  c.push(centerLine("LinkedIn: linkedin.com/in/swetha-reddy-gali-5176b7314  |  GitHub: github.com/swetha-67", { after: 60 }));

  c.push(section("PROFESSIONAL SUMMARY"));
  c.push(body(
    "Computer Science graduate with hands-on experience in Java Full Stack development through " +
    "internship and academic projects. Skilled in Java, MySQL, HTML, CSS, and JavaScript " +
    "fundamentals. Strong understanding of object-oriented programming, database concepts, and " +
    "web development. Quick learner with good problem-solving and adaptability skills, seeking an " +
    "entry-level Software Engineer opportunity."
  ));

  c.push(section("TECHNICAL SKILLS"));
  [["Programming: ", "Java, Python"],
   ["Web Technologies: ", "HTML5, CSS3, JavaScript"],
   ["Database: ", "MySQL"],
   ["Core Concepts: ", "OOP, DBMS, SQL, Data Structures"],
   ["Tools: ", "Git, GitHub, Eclipse/IntelliJ IDEA"]]
    .forEach(([k, v]) => c.push(body([{ text: k, bold: true }, { text: v }])));

  c.push(section("EDUCATION"));
  c.push(subhead("B.Tech – Computer Science and Engineering"));
  c.push(italicLine("Sri Venkateswara Institute of Technology  |  2021 – 2025  |  CGPA: 84"));

  c.push(section("INTERNSHIP"));
  c.push(subhead("Java Full Stack Development Intern"));
  c.push(italicLine("SkillDzire"));
  c.push(bullet("Developed responsive web pages using HTML, CSS, and JavaScript."));
  c.push(bullet("Worked with Java programming and object-oriented programming concepts."));
  c.push(bullet("Practiced database operations using MySQL and SQL queries."));
  c.push(bullet("Gained exposure to frontend and backend development workflows."));

  c.push(section("PROJECTS"));
  c.push(subhead("Student Dashboard Mobile Application"));
  c.push(italicLine("Role: Backend Developer"));
  c.push(bullet("Developed backend functionality for a student dashboard application."));
  c.push(bullet("Worked with database operations for storing and retrieving student information."));
  c.push(bullet("Implemented features to support student data management."));
  c.push(subhead("E-Commerce Web Application"));
  c.push(bullet("Developed an e-commerce website with user-friendly web pages."));
  c.push(bullet("Implemented product listing and basic shopping functionality."));
  c.push(bullet("Used HTML, CSS, JavaScript, Java, and MySQL concepts."));
  c.push(bullet("Focused on responsive design and simple user navigation."));

  c.push(section("CERTIFICATIONS"));
  c.push(bullet("Certified in Cloud Computing – NPTEL"));
  c.push(bullet("Java Full Stack Web Development Certification – TAP Academy"));

  c.push(section("SOFT SKILLS"));
  c.push(body("Problem Solving  •  Quick Learning  •  Adaptability  •  Communication  •  Teamwork"));

  c.push(section("INTERESTS"));
  c.push(body("Photography"));

  return build(c, "Swetha_Gali_Resume_SoftwareEngineer.docx", "Swetha Gali - Software Engineer Resume");
}

Promise.all([pythonResume(), seResume()]).then(() => console.log("Done."));
