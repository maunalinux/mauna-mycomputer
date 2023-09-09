# Mauna My Computer

Mauna My Computer is an ui for information and management of disks on your computer.

It is currently a work in progress. Maintenance is done by <a href="https://maunalinux.top/">Mauna Linux</a> team.

## Dependencies:

* This application is developed based on Python3 and GTK+ 3. Dependencies:
   - ```gir1.2-glib-2.0 gir1.2-gtk-3.0 gir1.2-notify-0.7 gir1.2-pango-1.0 gvfs-fuse python3-gi python3```

## Run Application from Source

* Install dependencies :
    * ```sudo apt install gir1.2-glib-2.0 gir1.2-gtk-3.0 gir1.2-notify-0.7 gir1.2-pango-1.0 gvfs-fuse python3-gi python3```
* Clone the repository :
    * ```git clone https://github.com/maunalinux/mauna-mycomputer.git ~/mauna-mycomputer```
* Run application :
    * ```python3 ~/mauna-mycomputer/src/mauna-mycomputer```

## Build deb package

* `sudo apt install devscripts git-buildpackage`
* `sudo mk-build-deps -ir`
* `gbp buildpackage --git-export-dir=/tmp/build/mauna-mycomputer -us -uc`

## Screenshots

![Mauna My Computer 1](screenshots/mauna-mycomputer-1.png)

![Mauna My Computer 2](screenshots/mauna-mycomputer-2.png)

![Mauna My Computer 3](screenshots/mauna-mycomputer-3.png)

![Mauna My Computer 4](screenshots/mauna-mycomputer-4.png)

![Mauna My Computer 5](screenshots/mauna-mycomputer-5.png)

![Mauna My Computer 6](screenshots/mauna-mycomputer-6.png)

![Mauna My Computer 7](screenshots/mauna-mycomputer-7.png)

![Mauna My Computer 8](screenshots/mauna-mycomputer-8.png)
