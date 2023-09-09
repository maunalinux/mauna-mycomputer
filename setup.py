#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os, subprocess


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "mauna-mycomputer.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/mauna-mycomputer.mo"]))
    return mo


changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = ""
    f = open("src/__version__", "w")
    f.write(version)
    f.close()


data_files = [
    ("/usr/share/applications/", ["top.mauna.mycomputer.desktop"]),
    ("/usr/share/mauna/mauna-mycomputer/", ["mauna-mycomputer.svg"]),
    ("/usr/share/mauna/mauna-mycomputer/src", [
        "src/Main.py",
        "src/MainWindow.py",
        "src/DiskManager.py",
        "src/Unmount.py",
        "src/UserSettings.py",
        "src/__version__"
    ]),
    ("/usr/share/mauna/mauna-mycomputer/ui", ["ui/MainWindow.glade"]),
    ("/usr/share/mauna/mauna-mycomputer/autostart/", ["autostart/mauna-mycomputer-add-to-desktop"]),
    ("/usr/share/mauna/mauna-mycomputer/css/", ["css/style.css"]),
    ("/etc/xdg/autostart", ["autostart/mauna-mycomputer-add-to-desktop.desktop"]),
    ("/usr/bin/", ["mauna-mycomputer"]),
    ("/usr/share/icons/hicolor/scalable/apps/", ["mauna-mycomputer.svg"])
] + create_mo_files()

setup(
    name="mauna-mycomputer",
    version="0.1.0",
    packages=find_packages(),
    scripts=["mauna-mycomputer"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Mauna Linux",
    author_email="dev@maunalinux.top",
    description="My Computer, UI for information and management of disks on your computer.",
    license="GPLv3",
    keywords="",
    url="https://maunalinux.top",
)
