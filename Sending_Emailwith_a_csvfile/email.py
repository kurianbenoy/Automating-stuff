# Send anj HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

#import smtplib,email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

email_user = 'soaikochi@gmail.com'
email_password = 'siraj@Kochi'
email_send = ['soaikochi@gmail.com','joelvzach@gmail.com']
#email_send = ['farhakareem998@gmail.com', 'muneebth@gmail.com', 'kiranjohns369@gmail.com', 'yogeshraj1719@gmail.com', 'akbgunner4ever@gmail.com', 'varunhawk19@gmail.com', 'krishnapsk77@gmail.com', 'neenuchacko@live.in', 'shariqansariastronomy@gmail.com', 'mafsan78692@gmail.com', 'riduvan96@gmail.com', 'abhijithneilabrahampk@gmail.com', 'beniljosenellad@gmail.com', 'mariakunnel11@gmail.com', 'prateekpraween1999d@gmail.com', 'munasirkm@gmail.com', 'akoopraba4@gmail.com', 'mohammedshan.p.s@gmail.com', 'awesomeshubham.jha@gmail.com', 'afthabsajad3@gmail.com', 'georgeeldho009@gmail.com', 'vineeth887@gmail.com', 'thatonephysicsnerd@gmail.com', 'jishnunair1398@gmail.com', 'ambrish2007@gmail.com', 'jesuinc918@gmail.com', 'jospaulshajan@gmail.com', 'ajayjyothish007@gmail.com', 'naseefoa@gmail.com', 'garvtambi05@gmail.com', 'kkrishnaprasad.mec@gmail.com', 'krkrishnaraj11@gmail.com', 'pranav1147@gmail.com', 'parthsuresh96@gmail.com', 'gauravkumar.bokaro@gmail.com', 'maheshchandran147@gmail.com', 'akarshashok12@gmail.com', 'nair.shreyas28@gmail.com', 'joelfintan@gmail.com', 'apsalshbk550@gmail.com', 'aldrinalfred72@gmail.com', 'athulakumar10@gmail.com', 'akshaykumarbarahaiya@gmail.com', 'appyranjan11@gmail.com', 'kumariaditi81@gmail.com', 'iamable007@gmail.com', 'ranjanritwick@gmail.com', 'johndavistl6@gmail.com', 'sgovindaramans@gmail.com', 'gauthamastro@gmail.com', 'mr.akashraut@gmail.com', 'nkshaheer03@gmail.com', 'vivekcheroor@gmail.com', 'devikarajeev9@gmail.com', 'unaissv@gmail.com', 'sinhatanya08@gmail.com', 'sujithsundar@gmail.com', 'adithyk9107@gmail.com', 'sankar.jaikishan@gmail.com', 'rufzha@gmail.com', 'anoopvarma.2000@gmail.com', 'memelvin99@gmail.com', 'anaswarak0705@gmail.com', 'annmarycyprian99@gmail.com', 'iamvishalarya@gmail.com', 'rk.sreepriya@gmail.com', 'seethaljames12@gmail.com', 'amaljoseph13@gmail.com', 'elizjacobk@gmail.com', 'nandu.workmail@gmail.com', 'aswinavofficial@gmail.com', 'dixonxavier@gmail.com', 'anusreekdasjks@gmail.com', 'gauthamkrishnanp@gmail.com', 'fawasmohammed92@gmail.com', 'jagannathbhat1998@gmail.com', 'aryansujith@gmail.com', 'pranavmodx@gmail.com']



msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Greetings Wizard! | School of AI,Kochi - Meetup #1'
msgRoot['From'] = email_user
msgRoot['To'] = ','.join(email_send)
msgRoot.preamble = 'This is a multi-part message in MIME format.'

msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Thank you for confirming your participation in our very first meetup. School of AI believes in bonding as a community and so your involvement will greatly impact the collective, in a positive manner.<br/>The meetup will comprise individuals of varying degree of proficiency in AI, yet it is our policy to not create any distinction as everyone is an eager learner!', 'html')

msgAlternative.attach(msgText)

#This example assumes the Image Path in folder
#fp = open('Images/Screenshot from 2018-07-20 00-48-57.png',"rb")
fp = open('images/index.jpeg')
msgImage = MIMEImage(fp.read())

msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
fp.close()

msg1 = MIMEText('The details of the meetup are as mentioned in the poster.<br/>We are additionally conducting an online quiz to help you get in the mood of the event. Feel free to use the internet to find the answer but do take the effort to comprehend the meaning of various terms you may come across. The winners will be revealed by tomorrow evening. <br/>As a final note, please do bring a notebook to jot down the valuable points we share tomorrow. Laptops would not be necessary as there are no technical workshops for the first meetup. As the objective of the gathering is to bond together and understand how we can grow together, your active presence of mind and wholehearted enthusiasm will fuel the session.<br/>Look forward to seeing you shine tomorrow, Wizard! Let us forge an innovation together.<br/><br/>Regards,<br/>The Team<br/> School of AI, Kochi')

# Send the email (this example assumes SMTP authentication is required)
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)
server.sendmail(email_user,email_send,msgRoot.as_string())
server.quit()
