#! /usr/bin/env python

# Author: Urucas <info@urucas.com>
# Version: 1.0.0


class NewsletterSender():

    def login(self, email_account, password):
        from MailSender import MailSender
        self._email = email_account
        self._mailSender = MailSender()
        self._mailSender.opensmtp(email_account, password)

    def prepare(self, json_path, html_path, email_subject):
        
        self._subject = str(email_subject)

        with open(json_path, "r") as filereader:
            data = filereader.read().replace('\n','')
            
        import json
        self._users = json.loads(data)

        with open(html_path, "r") as filereader:
            self._htmlcontent = filereader.read()
                
    def send(self, delay = 2):
        for user in self._users:
            self._mailSender.clear()
            self._mailSender.setBodyHTML(self._htmlcontent)
            self._mailSender.setFrom(self._email)
            self._mailSender.setTo(user.get("mail"))
            self._mailSender.setSubject(self._subject)
            self._mailSender.send()
            import time
            time.sleep(delay)




