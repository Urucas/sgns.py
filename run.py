#! /usr/bin/env python

# Author: Urucas <info@urucas.com>
# Version: 1.0.0


def main():
    
    import argparse
    parser = argparse.ArgumentParser(description="Simple newsletter sender.")
    parser.add_argument('--email', help='Email param', type=str, default=None)
    parser.add_argument('--pwd', help='Password', type=str, default=None)
    parser.add_argument('--subject', help='Subject', type=str, default=None)
    parser.add_argument('--json', help='Path to JSON object with all the emails', type=str, default=None)
    parser.add_argument('--html', help='Path to HTML newsletter content', type=str, default=None)

    args = parser.parse_args()
    import os
    if args.email == None:
        die("Email param not found")

    if args.pwd == None:
        die("Password param not found")

    if args.subject == None:
        die("Subject param not found")

    if args.json == None or not os.path.exists(args.json):
       die("JSON path not found")
        
    if args.html == None or not os.path.exists(args.html):
        die("HTML path not found")

    from NewsletterSender import NewsletterSender
    f = NewsletterSender()
    f.login(email_account=args.email, password=args.pwd)
    f.prepare(json_path=args.json, html_path=args.html, email_subject=args.subject)
    f.send()
    

def die(msg):
    print msg
    import sys
    sys.exit(1)

if __name__ == '__main__':
    main()

