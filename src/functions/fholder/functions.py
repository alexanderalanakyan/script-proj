"""Helper functions for other parts of the program"""

"""REFACTOR"""
import configparser
import subprocess
import shutil
import getpass
import traceback
import tomllib

config = configparser.ConfigParser()
config.read('../settings/settings.ini')


def run(cmd):
    """Runs a command and safely tries to exit"""
    try:
        subprocess.run(cmd, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print('An error has occured! Please report this:')
        print('\n-Errors-\n')
        print(traceback.format_exc)
        print('\n-Stdout/err-\n')
        print(f"\n{e.stderr}")
        print(f"\n{e.stdout}")
        print('\n-Settings-\n')
        print_settings()
        raise SystemExit from e
    print(f"Ran command, {' '.join(cmd)} with user {getpass.getuser()}")


def print_settings():
    """Prints all settings present (used for error handling)"""
    for section in config:
        print(f"[{section}]")
        for k, v in config.items(section):
            print(f"{k} = {v}")


def pacman_install(package_names):
    """Installs a list of pacman packages"""
    if getpass.getuser() == 'root':
        command = [
            'pacman',
            '-S',
            '--needed',
            '--noconfirm',
        ] + package_names
    elif shutil.which('sudo'):
        command = [
            'sudo',
            'pacman',
            '-S',
            '--needed',
            '--noconfirm',
        ] + package_names
    else:
        print('You dont have sudo manually install via pacman to continue (somehow)')
        raise SystemExit from RuntimeError
    run(command)


def flatpak_install(package_names):
    """Install a list of flathub packages"""
    command = [
        'flatpak',
        'install',
        '--noninteractive',
        '-y',
    ] + package_names
    run(command)


def yay_install(package_names):
    """
    Install a list of packages from the AUR using yay as a wrapper,
    while checking if yay exists
    """
    if shutil.which('yay'):
        if getpass.getuser() == 'root':
            print('Please run as an actual user...')
            raise SystemExit
        pacman_install(['base-devel', 'git'])
        run(['git', 'clone', 'https://aur.archlinux.org/yay.git'])
        run(['cd yay', '&&', 'makepkg -si'])
    command = [
        'yay',
        '-S',
        '--needed',
        '--noconfirm',
        '--cleanafter',
    ] + package_names
    run(command)


def open_packages(dir_name, other: str | None):
    """used for getting a bunch of packages from settings"""
    packages = f"../settings/packages/{dir_name}"
    if other is None:
        packages += f"/{dir_name}-packages.toml"
    else:
        packages += f"/{other}-packages.toml"
    try:
        with open(packages, 'rb') as file:
            data = tomllib.load(file)
    except PermissionError as e:
        print(f"You seemingly dont have permission to access {e.filename}... \n")
        print(traceback.format_exc)
        raise SystemError from e
    package_list = []

    def walk(d: dict, li: list):
        for k, v in d.items():
            if k == 'notes':
                continue
            if isinstance(v, list) and k == 'packages':
                for i in v:
                    li.append(i)
            elif isinstance(v, dict):
                walk(v, li)
            else:
                continue

    walk(data, package_list)
    return package_list


def exit_from_error(e: Exception):
    """Takes an input of an Exception and then raises system exit from that"""
    print(
        f"An error has occured! Please report this:\n{traceback.format_exc()}\n with settings:"
    )
    print_settings()
    raise SystemExit from e
