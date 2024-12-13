from fpdf import FPDF


class ResumeBuilder(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Resume', align='C', ln=True)
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 0, 255)  # Blue color for titles
        self.cell(0, 10, title, ln=True)
        self.ln(3)
        self.set_text_color(0, 0, 0)  # Reset color to black

    def section_content(self, content):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.ln(5)

    def personal_info(self, name, email, phone, linkedin, github):
        self.set_font('Arial', 'B', 18)
        self.cell(0, 10, f"{name}", ln=True, align='C')
        self.set_font('Arial', '', 12)
        # Email, Phone, LinkedIn, and GitHub in one line with space between them
        self.cell(0, 10, f"Email: {email}    Phone: {phone}    LinkedIn: {linkedin}    GitHub: {github}", ln=True,
                  align='C')
        self.ln(10)

    def achievements_section(self, achievements):
        if achievements:
            self.section_title('Achievements')
            for achievement in achievements:
                self.section_content(f"- {achievement}")

    def certificates_section(self, certificates):
        if certificates:
            self.section_title('Certificates')
            for certificate in certificates:
                self.section_content(f"- {certificate}")

    def education_section(self, school, degree, start_date, end_date, percentage=None, cgpa=None):
        self.section_title('Education')
        education_info = f"{degree} from {school}\n{start_date} - {end_date}"
        self.section_content(education_info)
        if percentage:
            self.section_content(f"Percentage: {percentage}%")
        if cgpa:
            self.section_content(f"CGPA: {cgpa}")

    def experience_section(self, company, role, start_date, end_date, description, technologies):
        self.section_title('Work Experience')
        experience_info = f"Role: {role} at {company}\n{start_date} - {end_date}\n{description}"
        self.section_content(experience_info)
        if technologies:
            self.section_title('Technologies Used')
            self.section_content(', '.join(technologies))

    def skills_section(self, skills):
        self.section_title('Skills')
        self.section_content(', '.join(skills))

    def generate_resume(self, name, email, phone, linkedin, github, achievements, certificates, education, experience,
                        skills, output_filename):
        self.add_page()
        self.personal_info(name, email, phone, linkedin, github)

        for edu in education:
            self.education_section(edu['school'], edu['degree'], edu['start_date'], edu['end_date'], edu['percentage'],
                                   edu['cgpa'])

        for exp in experience:
            self.experience_section(exp['company'], exp['role'], exp['start_date'], exp['end_date'], exp['description'],
                                    exp['technologies'])

        self.skills_section(skills)
        self.achievements_section(achievements)
        self.certificates_section(certificates)

        self.output(output_filename)


# Input Data (same as previous code)
name = input("Enter your full name: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
linkedin = input("Enter your LinkedIn profile link (leave blank if not applicable): ")
github = input("Enter your GitHub profile link (leave blank if not applicable): ")

# Achievements
achievements = []
has_achievements = input("Do you have any achievements? (yes/no): ").strip().lower()
if has_achievements == 'yes':
    num_achievements = int(input("How many achievements would you like to add? "))
    for _ in range(num_achievements):
        achievement = input("Enter an achievement: ")
        achievements.append(achievement)

# Certificates
certificates = []
has_certificates = input("Do you have any certificates? (yes/no): ").strip().lower()
if has_certificates == 'yes':
    num_certificates = int(input("How many certificates would you like to add? "))
    for _ in range(num_certificates):
        certificate = input("Enter the certificate name: ")
        certificates.append(certificate)

# Education
education = []
num_educations = int(input("How many education entries do you want to add? "))
for _ in range(num_educations):
    school = input("Enter the school/university name: ")
    degree = input("Enter your degree: ")
    start_date = input("Enter the start date of your education (e.g., 2015): ")
    end_date = input("Enter the end date of your education (e.g., 2019): ")

    percentage = None
    cgpa = None

    # For schooling, ask for percentage
    if "school" in school.lower():
        percentage = input("Enter your percentage: ")

    # For university, ask for CGPA
    if "university" in school.lower():
        cgpa = input("Enter your CGPA: ")

    education.append(
        {'school': school, 'degree': degree, 'start_date': start_date, 'end_date': end_date, 'percentage': percentage,
         'cgpa': cgpa})

# Work Experience
experience = []
num_experiences = int(input("How many work experiences do you want to add? "))
for _ in range(num_experiences):
    company = input("Enter the company name: ")
    role = input("Enter your job role: ")
    start_date = input("Enter the start date of your job (e.g., 2020): ")
    end_date = input("Enter the end date of your job (e.g., Present): ")
    description = input("Enter a brief description of your job role: ")
    technologies_input = input("Enter the technologies you used (separate by commas): ")
    technologies = [tech.strip() for tech in technologies_input.split(',')]  # List of technologies used
    experience.append(
        {'company': company, 'role': role, 'start_date': start_date, 'end_date': end_date, 'description': description,
         'technologies': technologies})

# Skills
skills = input("Enter your skills separated by commas: ").split(',')

# Create Resume PDF
output_filename = f"{name}_Resume.pdf"
resume = ResumeBuilder()
resume.generate_resume(name, email, phone, linkedin, github, achievements, certificates, education, experience, skills,
                       output_filename)

print(f"Your resume has been generated as {output_filename}")
