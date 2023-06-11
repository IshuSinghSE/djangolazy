import os
import json
import urllib3
import time
import argparse
import sys
from pathlib import Path



def file_opener(name, mode, content=[]):
    if mode == 'r':
        with open(name, mode) as f:
            return f.readlines()
    elif mode == 'w':
        with open(name, mode) as f:
            f.writelines(content)
    elif mode == 'json':
        with open(name, 'w') as f:
            json.dump(content, f, indent=4, sort_keys=True)


def array2str(arr):
    str = ''
    for item in arr:
        str += item + '\n'
    return str


def array2file(content: list()):
    arr = []
    for item in content:
        arr.append(item+'\n')
    return arr


def system(path, venv, project, app, file, args):
    if not os.path.exists(f'{path}/{venv}') and not os.path.exists(f'{path}/{project}'):
        print('-> Generating virtual environment ...')
        os.system(f"python -m venv {venv}")

        os.system(
            f"{path}/{venv}/Scripts/python.exe -m pip install -q --upgrade pip")
        print('-> Installing modules ...')
        os.system(
            f"{path}/{venv}/Scripts/pip3.exe install  django python-dotenv ")

    if not os.path.exists(f'{path}/{project}') and os.path.exists(f'{path}/{venv}/Scripts/django-admin.exe'):
        os.system(f"{path}/{venv}/Scripts/django-admin.exe  startproject {project}")
        os.system(f"{path}/{venv}/Scripts/pip3.exe freeze -q > {project}/requirements.txt")
        print('-> Creating Django project... ')

    if not os.path.exists(f'{path}/{project}/{app}') and os.path.exists(f'{path}/{project}'):
        os.system(
            f'"cd {project} && {path}/{venv}/Scripts/django-admin.exe  startapp {app} && echo #> {app}/urls.py"')
        print('-> Creating Django app... ')
        appsetup(path, venv, project, app, file, args)


def projectsetup(path, venv, project, app, file, args):
    def create_env(name, value='', file=''):
        # creating .ENV file value
        with open(f'{project}/.env', 'a+') as f:
            f.writelines(f"{name} = {value}\n")
            if name == "SECRET_KEY":
                new_file.append(f'{name} = os.getenv("{name}")\n')
            else:
                new_file.append(
                    f'{name}{" "*((18 - len(name)))} = os.getenv("{name}")\n')

    new_file = []
    string = file_opener(f'{project}/{project}/settings.py', 'r')[12:]

    # project/settings.py
    for index in range(len(string)):
        # Without comments, exclude in the settings.py
        if  args.comment:
          if string[index][0] != "#" :
            if string[index] != "\n" and string[index].split()[0] == file['project']['settings']['secret']:
                name = file['project']['settings']['secret']
                value = string[index].split()[-1]
                # .ENV file
                create_env(name, value)

            elif string[index] != "\n" and string[index].split()[0] == 'INSTALLED_APPS':
                new_file.append(string[index])
                new_file.insert(
                    index+1, array2str(file['project']['settings']['install_app']))

            elif string[index] != "\n" and args.template and string[index].split()[0].strip(":") == "'DIRS'":
                template = "os.path.join(BASE_DIR, 'Templates')"
                new_file.append(f"\t\t'DIRS' : [{template}],\n")

            elif string[index] != "\n" and string[index].split()[0] == "STATIC_URL":
                new_file.append(string[index])
                new_file.append(array2str(file["project"]["settings"]["path"]))

            elif string[index] != "\n" and  args.email  and string[index].split()[0] == "DEFAULT_AUTO_FIELD":
                new_file.append(string[index])
                new_file.append(
                    array2str(file["project"]["settings"]["email_backend"]))

                for name in file["project"]["settings"]["email_secret"]:
                    create_env(name)
                new_file.append(
                    array2str(file["project"]["settings"]["email_protocol"]))

            else:
                new_file.append(string[index])

        #With comments, include in the settings.py
        else:        
            if string[index] != "\n" and string[index].split()[0] == file['project']['settings']['secret']:
                name = file['project']['settings']['secret']
                value = string[index].split()[-1]
                # .ENV file
                create_env(name, value)

            elif string[index] != "\n" and string[index].split()[0] == 'INSTALLED_APPS':
                new_file.append(string[index])
                new_file.insert(
                    index+1, array2str(file['project']['settings']['install_app']))

            elif string[index] != "\n" and args.template and string[index].split()[0].strip(":") == "'DIRS'":
                template = "os.path.join(BASE_DIR, 'Templates')"
                new_file.append(f"\t\t'DIRS' : [{template}],\n")

            elif string[index] != "\n" and string[index].split()[0] == "STATIC_URL":
                new_file.append(string[index])
                new_file.append(array2str(file["project"]["settings"]["path"]))

            elif string[index] != "\n" and  args.email  and string[index].split()[0] == "DEFAULT_AUTO_FIELD":
                new_file.append(string[index])
                new_file.append(
                    array2str(file["project"]["settings"]["email_backend"]))

                for name in file["project"]["settings"]["email_secret"]:
                    create_env(name)
                new_file.append(
                    array2str(file["project"]["settings"]["email_protocol"]))

            else:
                new_file.append(string[index])

    # import module in settings.py
    new_file.insert(1, array2str(file['project']['settings']['import']))

    # project/settings.py
    file_opener(f'{project}/{project}/settings.py', 'w', new_file)

    # project/urls.py
    file_opener(f'{project}/{project}/urls.py', 'w', array2file(file['project']['urls']))


def appsetup(path, venv, project, app, file, args):
    file_opener(f'{project}/{app}/urls.py', 'w', array2file(file["app"]['urls']))
    if args.template:
        file_opener(f'{project}/{app}/views.py', 'w', array2file(file["app"]['views']))
    else:
        file_opener(f'{project}/{app}/views.py', 'w', array2file(file["app"]['index']))


def staticsetup(path, venv, project, app, file, args):
    # creating static, media, template folders
    dirs = []
    if args.template:
        dirs.append('Templates')
    if args.static != None:
        dirs.append(args.static[0])
        dirs.append(args.static[1])

    if  args.static != None or args.template:
        for dir in dirs:
            Path(f'{project}/{dir}').mkdir(parents=True, exist_ok=True)

    # File names to get from Github Repo
    files =  ['README.md']

    if args.template:
        files.append(f'{dirs[0]}/index.html')
    if args.gitignore:
        files.append('.gitignore')

    for file in files:
        if not os.path.exists(f'{path}/{project}/{file}'):
            url = f'https://raw.githubusercontent.com/IshuSinghSE/scripts/master/{file}'
            filename = f'{project}/{file}'
            c = urllib3.PoolManager()
            with c.request('GET', url, preload_content=False) as resp, open(filename, 'wb') as out_file:
                for chunk in resp:
                    out_file.write(chunk)
            resp.release_conn()

            print(f'--> {file} created ')


def createsuperuser(path, venv, project,app, file, args):
    ### This is the best way I found out to create a SuperUser programmatically ###
    # file_opener(f'{project}/{project}/wsgi.py', 'w', file_opener(f'{project}/{project}/wsgi.py', 'r')[9:] + array2file(file['project']['wsgi']))
    # file_opener(f'{project}/{project}/wsgi.py', 'w', file_opener(f'{project}/{project}/wsgi.py', 'r')[:7])
    # file_opener(f'{project}/{project}/wsgi.py', 'w', file_opener(f'{project}/{project}/wsgi.py', 'r')[9:])
    # os.system(f'"{path}/{venv}/Scripts/python.exe {project}/manage.py createsuperuser --no-input --username admin --email admin@email.com"')
    # os.system('set DJANGO_SUPERUSER_USERNAME="admin" &&    set DJANGO_SUPERUSER_PASSWORD="admin" && set DJANGO_SUPERUSER_EMAIL="abc"')
    if not os.path.exists(f'{path}/{project}/db.sqlite3') and args.username and args.password:
        os.system(
            f'"{path}/{venv}/Scripts/python.exe {project}/manage.py makemigrations"')
        os.system(
            f'"{path}/{venv}/Scripts/python.exe {project}/manage.py migrate "')
        os.system(
            f'echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser("{args.username}", "admin@email.com", "{args.password}") | "{path}/{venv}/Scripts/python.exe" {project}/manage.py shell')
        print('-> User created !\n-> username & password ->', 'admin')
    else:
        print('-> User already created !\n-> username & password ->', 'admin')


def startserver(path, venv, project, app,  file, args):

    print('Everything has been setup .💗.\nstarting server...')
    time.sleep(0.5)
    # os.system(
    #     f'start "C:\Program Files/Google\Chrome\Application\chrome.exe"  http://127.0.0.1:8000/admin/')
    os.system(
        f'start "C:\Program Files/Google\Chrome\Application\chrome.exe"  http://127.0.0.1:8000/')
    # os.system(f'"{path}/{venv}/Scripts/activate.bat"')
    os.system(f"{path}/{venv}/Scripts/python.exe {project}/manage.py runserver")



