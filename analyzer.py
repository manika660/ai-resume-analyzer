import spacy
from pdfminer.high_level import extract_text

skills_list = [
    "python", "java", "c++", "sql", "docker", "kubernetes", "aws",
    "excel", "tableau", "power bi", "machine learning", "tensorflow",
    "pytorch", "nlp", "deep learning", "javascript", "react", "git"
]

def extract_skills(text, skills_list):
    text = text.lower()
    found_skills = []
    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_resume_text(pdf_path):
    return extract_text(pdf_path)

def extract_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text} → {ent.label_}")

def main():
    # Read texts
    resume_text = extract_resume_text("resume.pdf")

    # Assuming job description is in a text file, load it:
    with open("job_description.txt", "r", encoding="utf-8") as f:
        job_text = f.read()

    # Extract skills
    resume_skills = extract_skills(resume_text, skills_list)
    job_skills = extract_skills(job_text, skills_list)

    print("Skills in Resume:", resume_skills)
    print("Skills in Job Description:", job_skills)

    # Find missing skills
    missing_skills = [skill for skill in job_skills if skill not in resume_skills]
    print("Missing Skills:", missing_skills)

    # Extract entities from resume
    print("\n🔍 Named Entities Found in Resume:\n")
    extract_entities(resume_text)

if __name__ == "__main__":
    main()


