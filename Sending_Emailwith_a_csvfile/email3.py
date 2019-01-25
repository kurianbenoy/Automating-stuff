import smtplib

from email.message import EmailMessage
from email.headerregistry import Address
from email.utils import make_msgid

msg = EmailMessage()
msg['Subject'] = "Ayons asperges pour le déjeuner"
msg['From'] = Address("Pepé Le Pew", "pepe", "soaikochi@gmail.com")
msg['To'] = ['soaikochi@gmail.com']

msg.set_content("""
Hello <First Name>,

Thank you for confirming your participation in our very first meetup. School of AI believes in bonding as a community and so your involvement will greatly impact the collective, in a positive manner.

The meetup will comprise individuals of varying degree of proficiency in AI, yet it is our policy to not create any distinction as everyone is an eager learner!


The details of the meetup are as mentioned in the poster attached.

We are additionally conducting an online quiz to help you get in the mood of the event. Feel free to use the internet to find the answer but do take the effort to comprehend the meaning of various terms you may come across. The winners will be revealed by tomorrow evening.

As a final note, please do bring a notebook to jot down the valuable points we share tomorrow. Laptops would not be necessary as there are no technical workshops for the first meetup. As the objective of the gathering is to bond together and understand how we can grow together, your active presence of mind and wholehearted enthusiasm will fuel the session.

Look forward to seeing you shine tomorrow, Wizard! Let us forge an innovation together.

Regards,
The Team,
School of AI Kochi
""")

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('soaikochi@gmail.com','siraj@Kochi')
    server.sendmail('soaikochi@gmail.com', ['kurian.bkk@gmail.com'], msg)
