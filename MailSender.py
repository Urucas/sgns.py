#! /usr/bin/env python

# Author: Urucas <info@urucas.com>
# Version: 1.0.0

class MailSender():

	_from, _to, _subject, _msg, _smtp = '', [], '', None, None

	def clear(self):
		self._from = ''
		self._to = []
		self._subject = ''
		self._msg = None
	
	def validateMail(self, mail):
		import re
		regex_mail = re.compile(r"(?:^|\s)[-a-z0-9_.\+]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)", re.IGNORECASE)
                if re.match(regex_mail, mail):
                    return True
		return None

	def setBody(self, body):
		from email.mime.text import MIMEText
		self._msg = MIMEText(body)

        def setBodyHTML(self, body):
            from email.mime.text import MIMEText
            self._msg = MIMEText(body, 'html')

	def setFrom(self, _from):
		if(self.validateMail(_from) is None): raise Exception('MailSender.setFrom: _from param is not a valid email --> %s' % _from)
		self._from = _from

	def setTo(self, _to):
		if(self.validateMail(_to) is None): raise Exception('MailSender.setTo: _to param is not a valid email --> %s' % _to)
		self._to.append(_to)

	def setSubject(self, _subject):
		self._subject = _subject

	def opensmtp(self, email_account, pwd, log = False):
            import smtplib
            self._smtp = smtplib.SMTP('smtp.gmail.com', 587)
            self._smtp.ehlo()
            self._smtp.starttls()
            self._smtp.ehlo()
            self._smtp.login(email_account, pwd)
            self._smtp.set_debuglevel(log)


	def send(self):
		if self._msg is None: raise Exception('MailSender.send: mail body not set')
		if self._smtp is None: self.opensmtp()
		self._msg['Subject'] = self._subject
		self._msg['From']    = self._from
		self._msg['To']      = ', '.join(self._to)
		self._smtp.sendmail(self._from, self._to, self._msg.as_string())
		
	def __del__(self):
		self._smtp.quit()

