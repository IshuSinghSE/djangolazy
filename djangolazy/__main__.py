######## -----------------------------------------------------------------------#######
########                Script for initial django project setup                #######
######## -----------------------------------------------------------------------#######

import os
import json
import urllib3
import time
import argparse
import sys
from pathlib import Path

from setupscript import system, projectsetup, startserver, staticsetup, createsuperuser


def main():
    system(path, venv, project, app, file, args)
    if not os.path.exists(f'{path}/{project}/.env') and os.path.exists(f'{path}/{project}'):
        projectsetup(path, venv, project, app, file, args)
        staticsetup(path, venv, project, app, file, args)
        createsuperuser(path, venv, project, app, file, args)
    if args.no_runserver:
        startserver(path, venv, project, app, file, args)

def arguments():
    # file_opener('config.json', 'json', file)

    parser = argparse.ArgumentParser(
                        prog='DjangoSetup',
                        description='Script for initial django project setup !',
                        epilog='Thanks for using...',add_help=True,fromfile_prefix_chars='+')
    # Names
    parser.add_argument("project",nargs='?',default='project', help='Django project name')
    parser.add_argument("app",nargs='?',default='app', help='Django app name')
    parser.add_argument("-v","--venv",default='venv', help='Virtual Environment name')
    parser.add_argument("-s","--static",nargs='+',default=['static', 'media'], help='Static, Media folders')

    #Files & Folders
    parser.add_argument("-t","--template",action="store_true", help='Add Template folder')
    # parser.add_argument("-e","--env",action="store_false", help=' Add .ENV file')
    parser.add_argument("-g","--gitignore",action="store_false", help='Add .gitignore file')
    
    #options
    parser.add_argument("--email",action="store_true", help='Add e-mail Configurations to settings.py')
    parser.add_argument("-c","--comment",action="store_true", help='Remove default comments to settings.py')
    parser.add_argument("-r","--no-runserver",action="store_false", help='Do not runserver, just create everything provided!')
    parser.add_argument("-u","--username",nargs="?",default="admin",help="superuser Username")
    parser.add_argument("-p","--password",nargs="?",default="admin",help="superuser Password")

    #version
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    
    try:
        args = parser.parse_args()
        return args
    except SystemExit: 
        return None


if __name__ == "__main__":
    args = arguments()
    path = os.getcwd()
    
    # if user has prompt for help message
    if args is not None:
        project = args.project 
        app =  args.app  
        venv = args.venv
        file = {
            "project": {
                "urls": [
                    "from django.contrib import admin",
                    "from django.urls import path, include",
                    "from django.conf import settings",
                    "from django.conf.urls.static import static\n",
                    "urlpatterns = [",
                    "\tpath('admin/', admin.site.urls),",
                    f"\tpath('',include('{app}.urls')),",
                    "]",
                    "urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)",],
                "settings": {
                    "import": [
                        "from dotenv import load_dotenv",
                        "import os",
                        "load_dotenv()",],
                    "secret":
                    "SECRET_KEY",
                    "install_app":
                    [f"\t'{app}.apps.{app.capitalize()}Config',",],
                    "path": [
                        f"STATICFILES_DIRS = [os.path.join(BASE_DIR,'{args.static[0]}')]",
                        "STATIC_ROOT = os.path.join(BASE_DIR,'assets')\n",
                        "MEDIA_URL  = '/media/'",
                        f"MEDIA_ROOT = os.path.join(BASE_DIR,'{args.static[1]}')",],
                    "email_backend": [
                        "\n\n### Email Configuration ###",
                        "EMAIL_BACKEND   = 'django.core.mail.backends.smtp.EmailBackend'",
                        "EMAIL_HOST      = 'smtp.mail.yahoo.com'",],
                    "email_secret":
                    ["EMAIL_USER", "EMAIL_PASSWORD",
                    "DEFAULT_FROM_EMAIL", "RECIPIENT_ADDRESS",],
                    "email_protocol": [
                        "EMAIL_PORT    = 587",
                        "EMAIL_USE_TLS = True",
                        "EMAIL_USE_SSL = False",
                        "EMAIL_TIMEOUT = 30",],
                },
                "wsgi": [
                    "from django.contrib.auth.models import User",
                    "users = User.objects.all()",
                    "if not users:",
                    "\tUser.objects.create_superuser(username='admin', email='user@example.com', password='admin', is_active=True, is_staff=True)",
                ],
            },

            "app": {
                "urls": ["from django.urls import path, include",
                        "from .views import index\n",
                        "urlpatterns = [",
                        "\tpath('',index, name='index'),",
                        "\n]",
                        ],
                "views": ["from django.conf import settings",
                        "from django.shortcuts import render\n",
                        "def index(request):",
                        "\treturn render(request, 'index.html',{})",
                        ],
                "index":["from django.conf import settings",
                        "from django.http import HttpResponse\n",
                        "def index(request):",
                        "\thtml = f'''",
                        "\t<html>",
                        "\t<body style='background-color:#f4f7ff'>",
                        "\t<a href='http://localhost:8000/admin' target='_blank' style='text-decoration:None;'><h3> Admin page </h3></a>",
                        "\t<h3>username & password : admin</h3>",
                        "\t<p> Please activate the virtual environment Manually , after stopping server! </br><strong> using  <code style='font-size:15px; background-color:#d7dae0; border-radius:5px;'> venv/Scripts/activate </code> , where venv is your virtual environment name</strong></p>",
                        "\t<script src='' async defer></script>",
                        "\t</body>",
                        "\t</html>",
                        "\t'''",
                        "\treturn HttpResponse(html)"
                        ],
            },
        }
        main()
        
