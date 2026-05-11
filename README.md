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


---










  
  [![Build Status](https://img.shields.io/github/actions/workflow/status/mjakeman/extension-manager/main.yml?branch=master)](https://github.com/mjakeman/extension-manager/actions/workflows/main.yml)
[![Translation status](https://hosted.weblate.org/widget/extension-manager/svg-badge.svg)](https://hosted.weblate.org/engage/extension-manager/)
[![Release Version](https://img.shields.io/github/v/release/mjakeman/extension-manager)](github.com/mjakeman/extension-manager/releases/latest)
[![Downloads](https://img.shields.io/badge/dynamic/json?color=green&label=downloads&query=installs_total&url=https%3A%2F%2Fflathub.org%2Fapi%2Fv2%2Fstats%2Fcom.mattjakeman.ExtensionManager)](https://flathub.org/apps/details/com.mattjakeman.ExtensionManager)
[![License (GPL-3.0)](https://img.shields.io/github/license/mjakeman/extension-manager)](http://www.gnu.org/licenses/gpl-3.0)

  <sup>Written with GTK 4 and libadwaita</sup>
  
![Screenshot of the main GUI (light mode)](data/screenshot-installed-light.png#gh-light-mode-only)
![Screenshot of the main GUI (dark mode)](data/screenshot-browse-dark.png#gh-dark-mode-only)

</div>

## 🔨 Building
The easiest way to build is by cloning this repo with GNOME Builder. It
will automatically resolve all relevant flatpak SDKs automatically.

Extension Manager needs a recent version of the GNOME SDK in order to build. See the [Development](build-aux/com.mattjakeman.ExtensionManager.Devel.json) or [Stable](/build-aux/com.mattjakeman.ExtensionManager.json) Flatpak manifests for a full dependency list.

### Dependencies
Extension Manager depends on the following libraries:
 - gettext
 - gtk4
 - libadwaita
 - libjson-glib
 - libsoup
 - libxml2
 - [blueprint](https://gitlab.gnome.org/jwestman/blueprint-compiler)

On Debian-based distributions, the required dependencies can be installed with the following command:
```shell
sudo apt install blueprint-compiler gettext libadwaita-1-dev libgtk-4-dev libjson-glib-dev libsoup-3.0-dev libxml2-dev meson
```

### Building From Source
```shell
meson setup _build
meson compile -C _build
meson install -C _build
```

## 👫 Code of Conduct
This project follows the [GNOME Code of Conduct](https://conduct.gnome.org/). Please
adhere to it in all project spaces and interactions.
