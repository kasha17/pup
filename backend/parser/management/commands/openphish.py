from django.core.management.base import BaseCommand, CommandError
from parser.models.models import MainSites, PhishingSites, MalwareSites
import requests
from django.core.mail import send_mail


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        print('parse-sites')
        new_malware_count = 0
        new_phishing_count = 0
        all_entries = 0

        main_urls = MainSites.objects.filter(type='txt').all()
        for main_url in main_urls:
            response = requests.get(main_url.url)
            # soup = BeautifulSoup(response.content, "html.parser")
            links = response.text.split('\n')
            for link in links:
                if 'phish' in link or 'phish' in main_url:
                    PhishingSites.objects.get_or_create(url=main_url)
                    all_entries += 1
                    new_phishing_count += 1
                else:
                    MalwareSites.objects.get_or_create(url=main_url)
                    all_entries += 1
                    new_malware_count += 1
            send_report(all_entries, new_phishing_count, new_malware_count)


def send_report(self, all_entries, new_phishing_count, new_malware_count):
    subject = 'Daily report: Site parsing results'
    message = (
        f'Daily parsing completed\n'
        f'All received sites: {all_entries}\n'
        f'Phishing sites: {new_phishing_count}\n'
        f'Malware sites: {new_malware_count}\n'
    )
    send_mail(
        'SITE CHECK REPORT',
        message,
        'admin@example.com',
        ['dofifip704@cartep.com'],  # https://temp-mail.org/ru/
        fail_silently=False,
    )
