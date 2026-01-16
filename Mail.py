
import pandas as pd
import yagmail

sender_email = "karan0797s@gmail.com"
app_password = "zhjdemuhfadkxgvm"

yag = yagmail.SMTP(sender_email, app_password)

data = pd.read_csv("professors.csv")

for _, row in data.iterrows():

    subject = "Research Internship Inquiry – Computer Engineering Student"

    body = f"""
Dear Professor {row['Name']},

I hope this email finds you well.

My name is Karanpal Singh, and I am a B.Tech Computer Engineering student at
B K Birla Institute of Engineering and Technology, Pilani.

I have a strong academic interest in Web Development and Machine Learning,
particularly in modern web technologies, scalable web architectures, and backend systems.

I have hands-on experience in full-stack web development using the MERN stack
(MongoDB, Express.js, React.js, Node.js). I have worked on developing scalable web platforms,
implementing backend logic, and building role-based dashboards for real-world use cases.

I am writing to respectfully inquire about the possibility of pursuing a
remote or on-campus, project-based internship under your guidance.

I am highly motivated, comfortable with remote collaboration tools, and willing
to dedicate consistent time and effort to assigned tasks and responsibilities.

Thank you very much for your time and consideration.
I would be grateful for any guidance or opportunity.

Warm regards,
Karanpal Singh  
B.Tech Computer Engineering  
B K Birla Institute of Engineering and Technology, Pilani  

📧 Email: karan0797s@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/karan-rathore-9a448a302/
"""


    
    with open("Karanpal_Singh_Resume.pdf", "rb") as resume_file:
        yag.send(
            to=row["Email"],
            subject=subject,
            contents=[body],
            attachments=[resume_file]  
        )

    print(f"Email sent to {row['Email']}")
