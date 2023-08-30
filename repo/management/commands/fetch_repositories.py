import requests
from django.core.management.base import BaseCommand
from repo.models import Repository

class Command(BaseCommand):
    help = 'Fetch repositories from GitHub API'

    def add_arguments(self, parser):
        parser.add_argument('github_username', type=str, help='GitHub username')

    def handle(self, *args, **options):
        github_username = options['github_username']
        url = f'https://api.github.com/users/{github_username}/repos'

        response = requests.get(url)
        if response.status_code == 200:
            repositories = response.json()
            for repo_data in repositories:
                repository, created = Repository.objects.update_or_create(
                    github_external_id=repo_data['id'],
                    defaults={
                        'name': repo_data['name'],
                        'github_username': github_username,
                        'url': repo_data['html_url'],
                        'stars': repo_data['stargazers_count'],
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added repository: {repo_data['name']}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"Updated repository: {repo_data['name']}"))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch repositories for user: {github_username}"))
