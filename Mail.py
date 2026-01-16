
import pandas as pd
import yagmail

sender_email = "karan0797s@gmail.com"
app_password = "zhjdemuhfadkxgvm"   # regenerate & replace

yag = yagmail.SMTP(sender_email, app_password)

data = pd.read_csv("professors.csv")

for _, row in data.iterrows():

    subject = "Research Internship Inquiry – Computer Engineering Student"

    body = f"""
Dear Dr. {row['Name']},

I hope this email finds you well.

My name is Karanpal Singh, and I am a B.Tech Computer Engineering student.
I am highly interested in your research work in {row['Research Area']}.

I would be grateful for an opportunity to work under your guidance.

Warm regards,
Karanpal Singh
"""

    # 🔑 OPEN FILE AS HANDLE (KEY FIX)
    with open("Karanpal_Singh_Resume.pdf", "rb") as resume_file:
        yag.send(
            to=row["Email"],
            subject=subject,
            contents=[body],
            attachments=[resume_file]   # 👈 FILE HANDLE, NOT STRING
        )

    print(f"Email sent to {row['Email']}")
