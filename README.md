sgns
==============================

**S**imple **G**mail **N**ewsletter **S**ender is a Python command-line tool to send newsletter emails using your Gmail account


# Usage
```bash
  $ python run.py
      --email your_gmail_account 
      --pwd your_gmail_password 
      --subject 'newsletter_subject' 
      --json path_to_json_file_with_emails 
      --html path_to_newsletter_html
```
  
# Example  
Using usuarios.json and newsletter.html we provide on the example folder, type:
```bash
  $ python run.py --email your_gmail_account --pwd your_gmail_password 
  --subject 'Simple Newsleter Testing' --json 'example/usuarios.json' --html 'example/newsletter.html'
```

# TODO
* Add arguments & functionalities to receive other data formats (--xml, --csv, --xls)
* Add argument & funcionality to get the html from an url (--html_uri)
