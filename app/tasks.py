import requests
from bs4 import BeautifulSoup
from flask_mail import Message
from celery import Celery
from . import app, db, mail
from .models import MainSites, PhishingSites, MalwareSites

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def parse_sites():
    main_urls = MainSites.query.all()
    for main_url in main_urls:
        response = requests.get(main_url.url)
        # soup = BeautifulSoup(response.content, "html.parser")
        links = response.text.split('\n')
        for link in links:
            if 'phish' in link or 'phish' in main_url:
                new_phishing_url = PhishingSites(url=link)
                db.session.add(new_phishing_url)
            else:
                new_malware_url = MalwareSites(url=link)
                db.session.add(new_malware_url)
        db.session.commit()
        send_report()


def send_report():
    msg = Message("SITE CHECK REPORT", recipients=["admin@example.com"])
    phishing_count = PhishingSites.query.count()
    malware_count = PhishingSites.query.count()
    msg.body = f'Daily parsing completed\nPhishing sites: {phishing_count}\nMalware sites: {malware_count}\n'
    mail.send(msg)
