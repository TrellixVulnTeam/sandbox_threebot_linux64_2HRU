from smtplib import SMTP
from Jumpscale import j


def main(self):

    # Make sure that the server has stopped
    j.servers.smtp.stop()
    j.servers.smtp.start()
    with SMTP("172.17.0.2", 7002) as smtp:
        # Create the mail
        body = "Hello!"
        from_mail = "you@gmail.com"
        to_mail = "target@example.com"
        msg = ("From: %s\r\nTo: %s\r\n\r\n" % (from_mail, to_mail)) + body
        # Send the mail
        smtp.sendmail(from_mail, "target@example.com", msg)

    # Get the data from the database
    db = j.data.bcdb.get("mails")
    retrieved_model = db.model_get(url="jumpscale.email.message")
    data = retrieved_model.find()[-1]

    # Doing my assertions on the retrieved data
    assert data.from_email == "you@gmail.com", "There is an error with the data"
    assert data.to_email == "target@example.com", "There is an error with the data"
    # Destroy the database
    db.destroy()
    # Stop the server
    j.servers.smtp.stop()
