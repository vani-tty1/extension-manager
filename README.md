# Extension Manager (Unofficial RPM Build)

A native utility for browsing, installing, and managing GNOME Shell Extensions. This tool allows you to search and install extensions from `extensions.gnome.org` without needing a web browser or the GNOME Shell browser connector.

---

### Important Notes
* **Unofficial Build:** This is a community package maintained by `vanit-tty1`. It is not affiliated with the original developer or the Fedora Project.
 
To see readable crash reports (with filenames and line numbers), you must install the debug symbols:
```bash
sudo dnf install extension-manager-debuginfo
```


---

### Installation

Enable the repository and install the package:

```bash
sudo dnf copr enable vaniiiiii/extension-manager
sudo dnf install extension-manager
```

 Issues & Support

Please do not report packaging issues to the original developer.
If you encounter installation errors, missing dependencies, or crashes specific to this RPM build, please open an issue [**here**](https://github.com/vani-tty1/extension-manager/issues)




### Credits
This application was originally developed by **[Matt Jakeman](https://github.com/mjakeman)**.
* **Official Repository:** [mjakeman/extension-manager](https://github.com/mjakeman/extension-manager)
* **Official Website:** [mattjakeman.com/apps/extension-manager](https://mattjakeman.com/apps/extension-manager)
