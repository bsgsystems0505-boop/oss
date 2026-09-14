from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import (
    Candidate,
    CandidateCredential,
    CandidatePlatform,
    OverallPlatform,
)


class Command(BaseCommand):
    help = "Seed VARIANZA candidates, credentials, and platforms."

    def handle(self, *args, **options):
        candidates = [
            {
                "name": "SUAYBAGUIO, LANCE MIGUEL",
                "position": "PRESIDENT",
                "photo": "theme/images/candidates/lance.jpg",
                "hierarchy_order": 1,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 7"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 9"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 10"),
                    ("JUNIOR HIGH", "Leadership Experience", "Research Leader — Grade 8"),
                    ("JUNIOR HIGH", "Leadership Experience", "Class P.I.O — Grade 9"),
                    ("JUNIOR HIGH", "Extracurriculars", "Nucleus Research Club — Grade 7"),
                    ("SENIOR HIGH", "Academic Achievements", "With Honors — Grade 11"),
                    ("SENIOR HIGH", "Academic Achievements", "With Honors — Grade 12"),
                    ("SENIOR HIGH", "Leadership Experience", "Research Leader for Scientific Research — Grade 11"),
                    ("SENIOR HIGH", "Leadership Experience", "Research Leader for Literature Research — Grade 11"),
                    ("SENIOR HIGH", "Leadership Experience", "Research Leader for Inquiries, Investigations, and Immersion — Grade 12"),
                    ("SENIOR HIGH", "Leadership Experience", "Research Leader for Literature Research — Grade 12"),
                    ("SENIOR HIGH", "Leadership Experience", "Youth Intellectual Property Advocates Representative — Grade 12"),
                    ("SENIOR HIGH", "Extracurriculars", "Youth Intellectual Property Advocates — Grade 12"),
                    ("COLLEGE", "Academic Achievements", "Organization of Statistics Students: Parangal Veritas et Numeri — 1st Year, 1st Semester (2025)"),
                    ("COLLEGE", "Academic Achievements", "DOST Scholar"),
                    ("COLLEGE", "Leadership Experience", "Civil Welfare Training Service Representative — 1st Year, 1st Semester"),
                    ("COLLEGE", "Leadership Experience", "Class Representative — 1st Year, 2nd Semester"),
                    ("COLLEGE", "Leadership Experience", "Class Representative — 2nd Year, 1st Semester"),
                    ("COLLEGE", "Professional Experience", "Co-Founder of a Software Enterprise Services Startup"),
                    ("COLLEGE", "Professional Experience", "Developed an Inventory Management System Website for a Client Company"),
                    ("COLLEGE", "Professional Experience", "Developed an Enterprise Resource Planning (ERP) System for a Client Company"),
                    ("COLLEGE", "Volunteer Work", "Youth Outreach Technical Head in an Elderly Home"),
                ],
                "platforms": [
                    (
                        "United and Purpose-Driven Leadership",
                        "Leadership comes with clear communication. I aim to create a healthy and united planning and executive process that allows the voices of the student body and its constituents to be heard and acted upon.",
                    ),
                    (
                        "Transparent and Hands-On Presentation",
                        "The student body should provide complete and transparent documentation of meetings, activities, and funds to the organization. The students under OSS should be informed of the actions, progress, and activities of the elected officers.",
                    ),
                    (
                        "Healthy Collaborative Learning",
                        "I aim to create a space to assist struggling students through creation of learning materials to supplement learning gaps. I want to target key fundamental concepts that students may struggle to comprehend and apply in their studies.",
                    ),
                ],
            },
            {
                "name": "IBANEZ, DEXTER",
                "position": "VP-INTERNAL",
                "photo": "theme/images/candidates/dexter.jpg",
                "hierarchy_order": 2,
                "credentials": [
                    ("JUNIOR HIGH", "Achievements", "High school Grade 10 with Honors — 1st Grading to 4th Grading"),
                    ("JUNIOR HIGH", "Achievements", "Grade 10 Aralin Panlipunan Outstanding Award — Third Quarter"),
                    ("JUNIOR HIGH", "Achievements", "Aralin Panlipunan Outstanding Perseverance Award — Third Quarter, Grade 10"),
                    ("JUNIOR HIGH", "Leadership Experience", "High School Officer PRO — A.Y. 2019–2020"),
                    ("SENIOR HIGH", "Achievements", "Grade 11 With Honors — Second Semester"),
                    ("SENIOR HIGH", "Achievements", "Grade 12 With Honors — Second Semester"),
                    ("SENIOR HIGH", "Leadership Experience", "Secretary of YOUNGCURE Organization — A.Y. 2023–2024"),
                    ("SENIOR HIGH", "Leadership Experience", "Vice President of YOUNGCURE Organization — A.Y. 2024–2025"),
                    ("COLLEGE", "Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 1st Semester (2025–2026)"),
                    ("COLLEGE", "Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 2nd Semester (2025–2026)"),
                    ("COLLEGE", "Leadership Experience", "Liaison Committee of CMCSA — A.Y. 2025–2026"),
                    ("COLLEGE", "Leadership Experience", "Class Representative — PATHFIT, 1st Semester"),
                    ("COLLEGE", "Leadership Experience", "OSS Committee in Student Affairs — A.Y. 2025–2026"),
                ],
                "platforms": [
                    (
                        "Student Grievance & Project Pipeline",
                        "Establish a dedicated communication channel where students can raise concerns, provide feedback, and propose project ideas.",
                    ),
                    (
                        "Internal Leadership Empowerment",
                        "Provide training, orientations, and seminars for officers and committee members to strengthen internal leadership.",
                    ),
                    (
                        "Streamlined Department Communications",
                        "Create a centralized messaging network for announcements, schedules, and organizational updates.",
                    ),
                ],
            },
            {
                "name": "BARRON, LEONARD LUIS",
                "position": "VP-EXTERNAL",
                "photo": "theme/images/candidates/leonard.jpg",
                "hierarchy_order": 3,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — 4th Place, Science Quiz Bee"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — 1st Place, Mathematics Quiz Bee"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — Highest Departmental Examination Score in Calculus"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — Highest Departmental Examination Score in Philosophy"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — 4th Place, Sudoku Competition"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With High Honors"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — 1st Place, Mathematics Quiz Bee"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — With High Honors"),
                    ("COLLEGE", "Academic Achievements", "Participant, 29th Philippine Statistics Quiz"),
                    ("COLLEGE", "Academic Achievements", "Mandaluyong Scholar"),
                    ("COLLEGE", "Academic Achievements", "First-Year — Panelist for Grade 12 Students' Research Presentations"),
                    ("COLLEGE", "Leadership & Community", "Co-Founder of a Software Enterprise Services Startup"),
                    ("COLLEGE", "Leadership & Community", "Science and Mathematics Tutor"),
                    ("COLLEGE", "Leadership & Community", "Tutor, DOSKAN Review Sessions for DOST Students"),
                    ("COLLEGE", "Professional Experience", "Freelance Data Engineer"),
                    ("COLLEGE", "Professional Experience", "Freelance Software Engineer"),
                    ("COLLEGE", "Professional Experience", "Developed an Inventory Management System Website for a Client Company"),
                    ("COLLEGE", "Professional Experience", "Developed an Enterprise Resource Planning (ERP) System for a Client Company"),
                    ("COLLEGE", "Technical Projects", "Developed a Convolutional Neural Network (CNN) for Experimental Human Detection using Python, NumPy, and OpenCV"),
                    ("COLLEGE", "Technical Projects", "Developed a Quantum Particle Simulation using PyOpenGL and NumPy"),
                    ("COLLEGE", "Technical Projects", "Developed a Solar System Simulation using PyOpenGL and NumPy"),
                    ("COLLEGE", "Technical Projects", "Regular Competitive Programmer with experience solving problems on LeetCode and Codeforces"),
                    ("COLLEGE", "Technical Expertise", "Strong background in Programming and Statistics"),
                    ("COLLEGE", "Technical Expertise", "Experienced in Data Engineering, Software Engineering, Algorithmic Problem Solving, and Scientific Computing"),
                ],
                "platforms": [
                    (
                        "Making OSS an Academically Healthy Competitive Environment",
                        "Create a healthy, fair, and merit-based competitive environment where students can improve their skills while supporting one another.",
                    ),
                    (
                        "Meritocracy and Healthy Competition",
                        "Provide opportunities based on effort, skills, and performance while using competition to encourage improvement and collaboration.",
                    ),
                    (
                        "Practical Learning and Professional Experience",
                        "Connect students with real data, real problems, and real organizations to develop practical Statistics experience.",
                    ),
                    (
                        "Building a Culture of Knowledge",
                        "Preserve and share Statistics-related academic work through a Digital Library.",
                    ),
                ],
            },
            {
                "name": "PADERNAL, IYA FREYLIE N.",
                "position": "SECRETARY",
                "photo": "theme/images/candidates/iya.jpg",
                "hierarchy_order": 4,
                "credentials": [
                    ("JUNIOR HIGH", "Achievements", "Grade 7 — With Honors, 4th Quarter"),
                    ("JUNIOR HIGH", "Achievements", "Grade 8 — With Honors"),
                    ("JUNIOR HIGH", "Achievements", "Grade 9 — With High Honors"),
                    ("JUNIOR HIGH", "Achievements", "Grade 10 — With Honors"),
                    ("JUNIOR HIGH", "Achievements", "Grade 10 — 2nd Runner-Up, Bayle sa Kalye Competition, Parañaque City Division Festival of Talents (2023)"),
                    ("JUNIOR HIGH", "Leadership", "Grade 7 — Class Auditor"),
                    ("JUNIOR HIGH", "Club Membership", "ParSci GSP Member (2019–2020)"),
                    ("JUNIOR HIGH", "Club Membership", "ParSci Performing Arts Club Member (2022–2023)"),
                    ("SENIOR HIGH", "Achievements", "Grade 11 — With Honors"),
                    ("SENIOR HIGH", "Achievements", "Grade 11 — 2nd Runner-Up, Bayle sa Kalye Competition, Parañaque City Division Festival of Talents (2024)"),
                    ("SENIOR HIGH", "Achievements", "Grade 12 — With Honors"),
                    ("SENIOR HIGH", "Achievements", "Unang Gantimpala sa Pagsulat ng Balitang Agham at Pangkalusugan — School-Based Journalism Training Workshop and Press Conference (2024)"),
                    ("SENIOR HIGH", "Achievements", "Third Place, Science & Technology Writing Category — School-Based Journalism Training Workshop and Press Conference (2024)"),
                    ("SENIOR HIGH", "Achievements", "First Place, Collaborative & Desktop Publishing Filipino Category, Secondary Level — Division School Press Conference (2024)"),
                    ("SENIOR HIGH", "Achievements", "Regional School Press Conference Qualifier — Collaborative & Desktop Publishing Filipino Category (2025)"),
                    ("SENIOR HIGH", "Leadership", "ParSci Performing Arts Club Dance Representative (2024–2025)"),
                    ("SENIOR HIGH", "Club Membership", "ParSci Performing Arts Club Member (2023–2024)"),
                    ("SENIOR HIGH", "Club Membership", "The Momentum Club Member (2024–2025)"),
                    ("SENIOR HIGH", "Club Membership", "Ang Pintig Member (2024–2025)"),
                    ("COLLEGE", "Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 1st Semester (2025)"),
                    ("COLLEGE", "Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 2nd Semester (2026)"),
                    ("COLLEGE", "Leadership", "Reading in Philippine History Class Representative (2025)"),
                    ("COLLEGE", "Leadership", "Block Representative (2026)"),
                    ("COLLEGE", "Club Membership", "OSS Publication and Documentation Committee (2026)"),
                ],
                "platforms": [
                    (
                        "CONNECT",
                        "Create organized and accessible announcements, reminders, schedules, and updates for students.",
                    ),
                    (
                        "SECure Information",
                        "Maintain organized files, meeting minutes, event records, achievements, and an accessible repository for organizational memory.",
                    ),
                    (
                        "STAT-VOICE",
                        "Use surveys and feedback mechanisms to gather student opinions and concerns and support student-centered, data-informed decisions.",
                    ),
                    (
                        "Organized Information, Inclusive Participation",
                        "Ensure every student is informed, heard, and given opportunities to participate.",
                    ),
                ],
            },
            {
                "name": "SANTUA, ANIKA E.",
                "position": "ASST. SECRETARY",
                "photo": "theme/images/candidates/anika.jpg",
                "hierarchy_order": 5,
                "credentials": [
                    ("ELEMENTARY", "Academic Achievements", "Grade 5 — Achiever"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — English Class Top 3 Awardee"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — With Honors (2019–2020)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 8 — With Honors (2020–2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — With Honors (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — ESP Class Top 3 Awardee"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — With Honors (2022–2023)"),
                    ("JUNIOR HIGH", "Leadership", "Class President (2019–2020)"),
                    ("JUNIOR HIGH", "Leadership", "Class President (2022–2023)"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With Honors, 1st Semester"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — Top 5, Statistics and Probability"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With High Honors, 2nd Semester"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With Honors"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — With Honor, Both Semesters"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — With High Honors, ABM (2024–2025)"),
                    ("SENIOR HIGH", "Leadership", "Class Secretary (2023–2024)"),
                    ("SENIOR HIGH", "Leadership", "Research Leader (2025)"),
                ],
                "platforms": [
                    (
                        "Secure & Private Records",
                        "Maintain safe and private organizational records with reliable backups.",
                    ),
                    (
                        "Order and Better Results",
                        "Maintain clear notes, accurate records, understandable messages, and smoother organizational processes.",
                    ),
                    (
                        "Steady Help for the Team",
                        "Provide dependable support through accurate, timely work, teamwork, and follow-through.",
                    ),
                    (
                        "POWER OF YOUR VOICE",
                        "Ensure student ideas are checked, discussed, and used so that student voices help shape rules and community decisions.",
                    ),
                ],
            },
            {
                "name": "MAGALLANES, GERALYN P.",
                "position": "TREASURER",
                "photo": "theme/images/candidates/geralyn.jpg",
                "hierarchy_order": 6,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 8 — With Honors (S.Y. 2020–2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Digimath Quiz Bee Participant"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Top 1 (S.Y. 2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — With High Honors (S.Y. 2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "1st Placer — Grade 9 Science Quiz Bee"),
                    ("JUNIOR HIGH", "Academic Achievements", "Research Defense — Best Group Presenter (S.Y. 2022–2023)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — With High Honors (S.Y. 2022–2023)"),
                    ("JUNIOR HIGH", "Academic Achievements", "STE Program Completer"),
                    ("JUNIOR HIGH", "Academic Achievements", "Pasig City Scholar"),
                    ("JUNIOR HIGH", "Extracurricular", "Community Based DRRM Seminar Participant"),
                    ("JUNIOR HIGH", "Extracurricular", "Fire Safety Hour Seminar Participant"),
                    ("JUNIOR HIGH", "Extracurricular", "GlobalSurge Camping Participant"),
                    ("JUNIOR HIGH", "Extracurricular", "3-Day Capability Building for BERT & DRRR Team Camping Participant"),
                    ("JUNIOR HIGH", "Leadership", "RHS GSP Member (S.Y. 2019–2020)"),
                    ("JUNIOR HIGH", "Leadership", "Zonta Club Member (S.Y. 2020–2021)"),
                    ("JUNIOR HIGH", "Leadership", "Grade 9 PIO of STE 2"),
                    ("JUNIOR HIGH", "Leadership", "Digimath Member (S.Y. 2021–2022)"),
                    ("JUNIOR HIGH", "Leadership", "Digimath Member (S.Y. 2022–2023)"),
                    ("JUNIOR HIGH", "Leadership", "Red Cross Youth Member"),
                    ("JUNIOR HIGH", "Leadership", "BERT Grade 10 Representative"),
                    ("JUNIOR HIGH", "Leadership", "BERT First Aid Committee Head"),
                    ("JUNIOR HIGH", "Leadership", "RHS GSP Vice President (S.Y. 2022–2023)"),
                    ("JUNIOR HIGH", "Leadership", "Zonta Club Secretary (S.Y. 2022–2023)"),
                    ("SENIOR HIGH", "Academic Achievements", "With High Honors"),
                    ("SENIOR HIGH", "Academic Achievements", "Pasig City Scholar"),
                    ("SENIOR HIGH", "Leadership", "BERT Auditor"),
                    ("SENIOR HIGH", "Leadership", "RHS GSP Secretary"),
                    ("SENIOR HIGH", "Leadership", "SSLG Internal Affairs Committee Member"),
                    ("COLLEGE", "Academic Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 1st Semester (2025–2026)"),
                    ("COLLEGE", "Academic Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 2nd Semester (2025–2026)"),
                    ("COLLEGE", "Academic Achievements", "DOST Scholar"),
                ],
                "platforms": [
                    (
                        "EVERY PESO ACCOUNTED FOR",
                        "Promote transparent and responsible fund handling where every contribution, expense, and balance is recorded, documented, and reported.",
                    ),
                    (
                        "MAKING EVERY PESO COUNT",
                        "Use organizational funds wisely and purposefully while exploring fundraising, donations, and membership fees to support organizational goals.",
                    ),
                    (
                        "PUTTING EVERY PESO TOWARD LEARNING",
                        "Prioritize spending that directly supports the academic growth and development of Statistics students.",
                    ),
                ],
            },
            {
                "name": "BORTIKEY, KARYLLE T.",
                "position": "AUDITOR",
                "photo": "theme/images/candidates/karylle.jpg",
                "hierarchy_order": 7,
                "credentials": [
                    ("GENERAL", "Education", "Rizal Technological University — Bachelor of Science in Statistics (2025–Present)"),
                    ("GENERAL", "Education", "Lagro High School — Accountancy, Business, and Management Strand (2023–2025)"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 7 (2020–2021)"),
                    ("JUNIOR HIGH", "Leadership", "Class Secretary — Grade 7 (2020–2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 8 (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 9 (2022–2023)"),
                    ("JUNIOR HIGH", "Extracurricular", "ExplainED PH Online National Press Conference — Participant (2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "With Honors — Grade 10 (2022–2023)"),
                    ("SENIOR HIGH", "Academic Achievements", "With High Honors — Grade 11 (2023–2024)"),
                    ("SENIOR HIGH", "Organization", "ABM Students in Service through Excellence and Transformation — Member (2023–2024)"),
                    ("SENIOR HIGH", "Leadership", "Certificate of Recognition — Master of Ceremony, ABM Beyond: Unleashing Creativity and Innovation (2024)"),
                    ("SENIOR HIGH", "Leadership", "Business Venture Chief Executive Officer — Grade 11 (2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "Outstanding Performance in Fundamentals of Accountancy in Business Management — Grade 11 (2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "Outstanding Performance in Organization and Management (2023–2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "With High Honors — Grade 12 (2024–2025)"),
                    ("SENIOR HIGH", "Leadership", "Class P.R.O — Grade 12 (2024–2025)"),
                    ("SENIOR HIGH", "Organization", "ASSET Documentation Committee (2024–2025)"),
                    ("SENIOR HIGH", "Organization", "Young Entrepreneurs and Accountants Association — Documentation Committee (2024–2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "Outstanding Performance in Work Immersion Program (2025)"),
                    ("SENIOR HIGH", "Organization", "ASSET Member (2025)"),
                    ("SENIOR HIGH", "Leadership", "Feasibility Study Assistant Leader (2025)"),
                    ("SENIOR HIGH", "Leadership", "ABM Week Event Facilitator (2025)"),
                    ("SENIOR HIGH", "Extracurricular", "LHS Research Congress (2025)"),
                    ("SENIOR HIGH", "Training", "Real-World Ready: A Student's Guide to Work Immersion Success (2024)"),
                    ("COLLEGE", "Organization", "Kultura Rizalia Dance Troupe — Member (2025–Present)"),
                    ("COLLEGE", "Organization", "Organization of Statistics Students — Finance Committee (2026)"),
                    ("COLLEGE", "Training", "LIMITLESS 2026: Illuminating Change with Statistics"),
                    ("COLLEGE", "Training", "ANOVA — Analytics and Numerical Operations Via Applications: Jamovi and Python Workshop (2026)"),
                    ("COLLEGE", "Training", "Data Science Training for Students, Project D3 — Phase 1 (2025)"),
                ],
                "platforms": [
                    (
                        "Regular Auditing",
                        "Review financial records, transactions, and supporting documents for accuracy and completeness.",
                    ),
                    (
                        "Monthly and Annual Financial Reporting",
                        "Provide clear financial reports accessible to students showing how organizational funds are allocated and used.",
                    ),
                    (
                        "Organizational Feedback and Evaluation",
                        "Gather confidential feedback regarding organizational performance to support accountability and improvement.",
                    ),
                ],
            },
            {
                "name": "CAUDILLA, VANESSA NICOLE B.",
                "position": "ASST. AUDITOR",
                "photo": "theme/images/candidates/vanessa.jpg",
                "hierarchy_order": 8,
                "credentials": [
                    ("GENERAL", "Year Level", "2nd Year"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — Rank 5, Best in Mathematics"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — Academic Achiever"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — Conduct Award"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — Second Grading Filipino Excellence Award"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — With Honors"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Mathematics Recognition Award"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — With Honors"),
                    ("JUNIOR HIGH", "Extracurricular", "Grade 7 — 2nd Runner-Up in Slogan Poster Making, Values Education"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — First and Second Semester Academic Achiever"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — First and Second Semester Academic Achiever"),
                    ("SENIOR HIGH", "Academic Achievements", "Recognition Award in Disaster Risk Management"),
                    ("SENIOR HIGH", "Academic Achievements", "Recognition Award in Pagbasa sa Pananaliksik — Filipino"),
                    ("SENIOR HIGH", "Leadership & Extracurricular", "Head Writer and Editorial Cartoonist — Journalism Club"),
                    ("SENIOR HIGH", "Leadership & Extracurricular", "Techno Kids Member — Self-learned HTML & CSS"),
                    ("SENIOR HIGH", "Leadership & Extracurricular", "Research Leader — Filipino"),
                    ("SENIOR HIGH", "Leadership & Extracurricular", "Yes-O Club — Committee"),
                    ("COLLEGE", "Academic Achievements", "1st Year, 2nd Semester — Certificate of Excellence, OSS: Parangal Veritas et Numeri"),
                    ("COLLEGE", "Leadership", "1st Year, 1st Semester — Class Representative, Pathfit 1"),
                    ("COLLEGE", "Leadership", "1st Year, 2nd Semester — Class Representative, Art Appreciation"),
                    ("COLLEGE", "Extracurricular", "OSS Extension Relation Committee — First Year, Second Semester"),
                    ("COLLEGE", "Training & Certifications", "DataCamp — SQL and Data Visualization"),
                    ("COLLEGE", "Training & Certifications", "Microsoft Excel — Data Entry and Finance Basics"),
                    ("COLLEGE", "Training & Certifications", "Webinar on Jamovi and Python — Participant"),
                    ("COLLEGE", "Training & Certifications", "Search Engine Optimization — YouTube"),
                    ("COLLEGE", "Scholarships", "CHED Tulong Dunong Program — Applicant"),
                    ("COLLEGE", "Scholarships", "TEFAP: Parañaque City — Applicant"),
                ],
                "platforms": [
                    (
                        "STUDENT BUDGET WISHLIST",
                        "Allow students to suggest fund allocations and review the top suggestions before events.",
                    ),
                    (
                        "DATA AUDIT LITERACY",
                        "Explain financial and audit terms, reports, expenses, and budget categories in accessible ways.",
                    ),
                    (
                        "POST-EVENT FINANCIAL TRACKER",
                        "Present actual expenses against approved budgets with charts within one week after an event.",
                    ),
                    (
                        "Transparent Data, Accountable Leadership",
                        "Make relevant audit data accessible to students to strengthen accountability.",
                    ),
                ],
            },
            {
                "name": "TOMAWIS, ALLIYAH P.",
                "position": "PROJECT MANAGER",
                "photo": "theme/images/candidates/alliyah.jpg",
                "hierarchy_order": 9,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 7 — With Honors (2019–2020)"),
                    ("JUNIOR HIGH", "Academic Achievements", "SciCoMath Quiz Bee — 3rd Place (2020)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 8 — With Honors (2020–2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — With High Honors (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "With High Honors in English Subject (2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — With High Honors (2022–2023)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Certificate of Completion — Junior High School (2023)"),
                    ("JUNIOR HIGH", "Leadership", "Science Club Grade 7 Representative (2019–2020)"),
                    ("JUNIOR HIGH", "Leadership", "Class President (2020–2021)"),
                    ("JUNIOR HIGH", "Leadership", "Painting Club Secretary (2022–2023)"),
                    ("JUNIOR HIGH", "Leadership", "Techno Club Grade 10 Representative (2022–2023)"),
                    ("JUNIOR HIGH", "Leadership", "Beauty Care Class Auditor (2022–2023)"),
                    ("JUNIOR HIGH", "Extracurricular", "Bridging Cultures: One Speech at a Time — UPLB (2022)"),
                    ("JUNIOR HIGH", "Extracurricular", "LHS Capacity Building Webinar (2022)"),
                    ("JUNIOR HIGH", "Extracurricular", "PROJECT ASTRAL (2023)"),
                    ("JUNIOR HIGH", "Extracurricular", "ASEAN Data Science Explorers Enablement Session — SAP Analytics Cloud Training (2023)"),
                    ("JUNIOR HIGH", "Extracurricular", "Spoken Poetry Contest (2023)"),
                    ("SENIOR HIGH", "Academic Achievements", "STEM Grade 11 — With High Honors (2023–2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "With Honors in Wika Subject — 1st Semester (2023)"),
                    ("SENIOR HIGH", "Academic Achievements", "With Honors in Statistics & Probability (2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "STEM Grade 12 — With High Honors (2024–2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "With High Honors in Akademik Subject (2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "Certificate of Completion — Work Immersion Program (2025)"),
                    ("SENIOR HIGH", "Leadership", "Class PIO (2023–2024)"),
                    ("SENIOR HIGH", "Extracurricular", "International Cultural Immersion Program at RTU (2024)"),
                    ("SENIOR HIGH", "Extracurricular", "Women Empowerment for Gender Equality and Inclusive Society Seminar (2024)"),
                    ("COLLEGE", "Academic Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 1st Semester (2025)"),
                    ("COLLEGE", "Academic Achievements", "OSS: Parangal Veritas et Numeri — 1st Year, 2nd Semester (2026)"),
                    ("COLLEGE", "Leadership", "Block Representative (2025)"),
                    ("COLLEGE", "Leadership", "Understanding The Self — Block Representative (2026)"),
                    ("COLLEGE", "Extracurricular", "LIMITLESS: National Youth Summit on Statistics 2026"),
                ],
                "platforms": [
                    (
                        "PROJECT IMPACT CHECK",
                        "Establish clear objectives, participant feedback, and evaluation mechanisms to improve projects.",
                    ),
                    (
                        "STAT SYNC: PEER ACADEMIC SUPPORT",
                        "Organize peer-led review sessions with facilitators, tutors, practice problems, and reviewers.",
                    ),
                    (
                        "INCOME GENERATING PROJECTS",
                        "Develop affordable products, events, booths, and merchandise to support future organizational activities.",
                    ),
                ],
            },
            {
                "name": "ABAINZA, YSHIE KARYLLE A.",
                "position": "PRO",
                "photo": "theme/images/candidates/yshie.jpg",
                "hierarchy_order": 10,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 8 — With Honors (2020–2021)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Best in Filipino (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Best in STM (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — Best in MAPEH (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — With Honors (2021–2022)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 10 — With Honors (2022–2023)"),
                    ("JUNIOR HIGH", "Academic Achievements", "Pasig City Science High School Full Scholarship Program"),
                    ("JUNIOR HIGH", "Leadership", "Grade 7 — Class President (2020–2021)"),
                    ("JUNIOR HIGH", "Leadership", "Grade 9 — Class President (2021–2022)"),
                    ("JUNIOR HIGH", "Extracurricular", "Research Congress 2023 — Technical Working Committee"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With Honors (2023–2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — With Honors (2024–2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "Pasig City Science High School Full Scholarship Program"),
                    ("SENIOR HIGH", "Extracurricular", "CONSTELLATE: PCSHS Astrobiology and Biology Club — Volunteer Pubmat Creator (2024)"),
                    ("SENIOR HIGH", "Extracurricular", "GAMMA: PCSHS Physics Club — Content and Planning Committee (2024–2025)"),
                    ("SENIOR HIGH", "Extracurricular", "GAMMA: PCSHS Physics Club — Volunteer Academic Tutor (2024–2025)"),
                    ("COLLEGE", "Academic Achievements", "OSS: Certificate of Excellence — Parangal Veritas et Numeri, 1st Year, 1st Semester (2025–2026)"),
                    ("COLLEGE", "Academic Achievements", "OSS: Certificate of Excellence — Parangal Veritas et Numeri, 1st Year, 2nd Semester (2025–2026)"),
                    ("COLLEGE", "Academic Achievements", "DOST-SEI RA 7687 Scholarship Program"),
                    ("COLLEGE", "Academic Achievements", "Real LIFE Scholarship Program"),
                    ("COLLEGE", "Academic Achievements", "DataCamp Scholarship Program of Google Developer Groups on Campus, Polytechnic University of the Philippines"),
                    ("COLLEGE", "Leadership", "Class Representative — Mathematics in Modern World, 1st Year, 1st Semester (2025)"),
                    ("COLLEGE", "Leadership", "Class Representative — Purposive Communication, 1st Year, 1st Semester (2025)"),
                    ("COLLEGE", "Leadership", "Class Representative — NSTP-CWTS 2, 1st Year, 2nd Semester (2026)"),
                    ("COLLEGE", "Leadership", "Block Representative — CAS-05-301A, 2nd Year, 2nd Semester (2026)"),
                    ("COLLEGE", "Extracurricular", "OSS Committee on Creatives and Multimedia (2025–2026)"),
                    ("COLLEGE", "Extracurricular", "RTU DOST Scholars' Association — Multimedia and Marketing Committee (2025–2026)"),
                    ("COLLEGE", "Extracurricular", "DataCamp: Understanding Data Science (2026)"),
                ],
                "platforms": [
                    (
                        "Statistics News Flash",
                        "Provide timely and accurate updates regarding suspensions, occasions, activities, and notices.",
                    ),
                    (
                        "Statisticians First",
                        "Strengthen student voice regarding issues, events, postings, themes, and programs.",
                    ),
                    (
                        "Strong Connections, Greater Opportunities",
                        "Build stronger connections among students to create opportunities for participation and collaboration.",
                    ),
                ],
            },
            {
                "name": "PALOMA, FRANZCHESKA KHRYSBETH",
                "position": "ECO-WARRIOR",
                "photo": "theme/images/candidates/franzcheska.jpg",
                "hierarchy_order": 11,
                "credentials": [
                    ("JUNIOR HIGH", "Academic Achievements", "Grade 9 — 3rd Runner-Up in Poster Making"),
                    ("JUNIOR HIGH", "Leadership", "Grade 10 — Gender and Development Auditor"),
                    ("JUNIOR HIGH", "Leadership", "Grade 10 — Class Secretary"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — With Honors (A.Y. 2023–2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 11 — Best in Humanities and Social Sciences (A.Y. 2023–2024)"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — With Honors (A.Y. 2024–2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "Grade 12 — Best in Understanding Culture, Society, and Politics (A.Y. 2024–2025)"),
                    ("SENIOR HIGH", "Academic Achievements", "Service Awardee (A.Y. 2024–2025)"),
                    ("SENIOR HIGH", "Leadership", "Grade 11 — Class Vice President"),
                    ("SENIOR HIGH", "Leadership", "Grade 12 — Class Auditor"),
                    ("SENIOR HIGH", "Organization", "VOX HARMONIAE: AECHOVIN — Band Main Vocalist (A.Y. 2023–2025)"),
                    ("SENIOR HIGH", "Organization", "Humanities and Social Sciences Executive Committee — Member (A.Y. 2023–2024)"),
                    ("SENIOR HIGH", "Organization", "Student Council Committee: Set Up Committee — Member (A.Y. 2024–2025)"),
                    ("COLLEGE", "Leadership", "PATHFIT — Class Representative, 2nd Semester (A.Y. 2025–2026)"),
                    ("COLLEGE", "Leadership", "Technical Communication — Class Representative, 1st Semester (A.Y. 2026–2027)"),
                ],
                "platforms": [
                    (
                        "Clean up, Stand out!",
                        "Promote cleanliness and hygiene while providing necessary goods such as tissues, sanitary pads, and soap and encouraging responsible waste management.",
                    ),
                    (
                        "Earth Keeper",
                        "Ensure that events leave no waste behind, keep areas clean, and avoid harmful or disruptive materials.",
                    ),
                    (
                        "Root Note",
                        "Create environmental posts discussing challenges, cleanliness, pollution, and the 5 R's.",
                    ),
                    (
                        "Securing Our Environment: Protect Our Future",
                        "Build an inspiring environment where students can become their best selves while caring for their surroundings.",
                    ),
                ],
            },
            {
                "name": "TAMIDLES, JHON PHILIP",
                "position": "2ND YEAR REPRESENTATIVE",
                "photo": "theme/images/candidates/jhon.jpg",
                "hierarchy_order": 12,
                "credentials": [
                    ("JUNIOR HIGH", "Achievements", "Grade 10 — With Honors, First Quarter to Fourth Quarter"),
                    ("JUNIOR HIGH", "Leadership", "Grade 9 — Class President"),
                    ("JUNIOR HIGH", "Leadership", "Grade 10 — Class Vice President"),
                    ("JUNIOR HIGH", "Leadership", "Grade 10 — Research Group Leader"),
                    ("SENIOR HIGH", "Achievements", "Grade 11 STEM — With Honors, First Semester"),
                    ("SENIOR HIGH", "Achievements", "Science Wizard — First Semester"),
                    ("SENIOR HIGH", "Achievements", "Grade 11 STEM — With Honors, Second Semester"),
                    ("SENIOR HIGH", "Achievements", "Science Wizard — Second Semester"),
                    ("SENIOR HIGH", "Achievements", "Grade 12 STEM — With High Honors"),
                    ("SENIOR HIGH", "Leadership", "Grade 11 STEM — Research Group Leader"),
                    ("SENIOR HIGH", "Leadership", "Grade 12 STEM — Research Group Leader"),
                    ("COLLEGE", "Achievements", "OSS Parangal Veritas et Numeri — 1st Year, First Semester, A.Y. 2025–2026"),
                    ("COLLEGE", "Achievements", "OSS Parangal Veritas et Numeri — 1st Year, Second Semester, A.Y. 2025–2026"),
                    ("COLLEGE", "Leadership", "Class Representative — PATHFIT 1"),
                ],
                "platforms": [
                    (
                        "STAT-SUPPORT",
                        "Make Statistics students' lives more connected, supported, and heard.",
                    ),
                    (
                        "Academic Support",
                        "Create a shared reviewer and resource bank with upper-year tips, notes, and study strategies.",
                    ),
                    (
                        "Student Concerns & Representation",
                        "Provide anonymous channels for concerns and suggestions, bring 2nd-year concerns to officers and faculty, and provide updates on actions taken.",
                    ),
                ],
            },
        ]

        overall_platforms = [
            (
                "OSS Essentials",
                "OSS Merchandise",
                "Statistics-related merchandise such as ID laces, shirts, tote bags, stickers, and educational materials to raise funds and promote Statistics.",
            ),
            (
                "OSSHub",
                "OSS Digital Hub",
                "An online hub showcasing achievements, research, activities, archived academic works, announcements, and learning materials.",
            ),
            (
                "OSSDevelop",
                "Local Statistics Competitions",
                "Healthy competitions in Mathematics, Statistics, and Coding.",
            ),
            (
                "OSSDevelop",
                "Research Congress",
                "A platform to showcase and archive student research and promote a stronger research culture.",
            ),
            (
                "OSSCore",
                "Coding and Statistics Seminars",
                "Seminars covering tools, coding languages, and current trends relevant to Statistics students.",
            ),
            (
                "OSSCore",
                "Statistics Check-In",
                "Interviews with professionals and students during events to share experiences and perspectives.",
            ),
            (
                "OSSCore",
                "Statistics Peer Tutoring",
                "Faculty-approved peer tutoring materials focused on fundamental Statistics concepts.",
            ),
            (
                "OSSConnect",
                "Calculator Rentals",
                "A reliable calculator rental service supported by alumni donations and available organizational resources.",
            ),
            (
                "OSSConnect",
                "Research Statistics Services",
                "An alumni directory that can connect students with statistical assistance for academic papers.",
            ),
            (
                "OSSFeed",
                "Improved Online Engagement",
                "An active social media space featuring Statistics concepts and interactive educational activities.",
            ),
            (
                "OSSFeed",
                "Voice for Student Affairs",
                "Feedback and sensing forms after events to help address student concerns, questions, and frequently raised issues.",
            ),
        ]

        self.stdout.write("Seeding candidates...")

        for candidate_data in candidates:
            credentials = candidate_data.pop("credentials")
            platforms = candidate_data.pop("platforms")

            slug = slugify(candidate_data["name"])

            candidate, created = Candidate.objects.update_or_create(
                slug=slug,
                defaults=candidate_data,
            )

            CandidateCredential.objects.filter(
                candidate=candidate,
            ).delete()

            for order, credential in enumerate(credentials, start=1):
                education_level, category, title = credential

                CandidateCredential.objects.create(
                    candidate=candidate,
                    education_level=education_level,
                    category=category,
                    title=title,
                    order=order,
                )

            CandidatePlatform.objects.filter(
                candidate=candidate,
            ).delete()

            for order, platform in enumerate(platforms, start=1):
                title, description = platform

                CandidatePlatform.objects.create(
                    candidate=candidate,
                    title=title,
                    description=description,
                    order=order,
                )

            action = "Created" if created else "Updated"

            self.stdout.write(
                self.style.SUCCESS(
                    f"{action}: {candidate.name}"
                )
            )

        OverallPlatform.objects.all().delete()

        for order, platform in enumerate(
            overall_platforms,
            start=1,
        ):
            category, title, description = platform

            OverallPlatform.objects.create(
                category=category,
                title=title,
                description=description,
                order=order,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "VARIANZA seed completed successfully."
            )
        )