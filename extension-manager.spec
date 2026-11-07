Name:           extension-manager
Version:        0.7.0
Release:        2%{?dist}
Summary:        A utility for browsing and installing GNOME Shell Extensions
License:        GPL-3.0-or-later
URL:            https://github.com/mjakeman/extension-manager
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson gcc gettext blueprint-compiler desktop-file-utils libappstream-glib
BuildRequires:  pkgconfig(gtk4) pkgconfig(libadwaita-1) pkgconfig(libsoup-3.0) pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0) pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(glycin-2) pkgconfig(glycin-gtk4-2)
Requires:       glycin-loaders gtk4 libadwaita json-glib libsoup3 libxml2

%description
A native tool for browsing, installing, and managing GNOME Shell Extensions.

%prep
%autosetup -n %{name}-%{version}

%build
%meson \
    -Dbacktrace=false \
    -Dpackage="Copr Build" \
    -Ddistributor="Giovanni Rafanan <giovannirafanan609@gmail.com>"
%meson_build

%install
%meson_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license COPYING
%{_bindir}/extension-manager
%{_metainfodir}/*.xml
%{_datadir}/applications/com.mattjakeman.ExtensionManager.desktop
%{_datadir}/glib-2.0/schemas/com.mattjakeman.ExtensionManager.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.mattjakeman.ExtensionManager.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.mattjakeman.ExtensionManager-symbolic.svg
%{_datadir}/gnome-shell/search-providers/com.mattjakeman.ExtensionManager.search-provider.ini
%{_datadir}/dbus-1/services/com.mattjakeman.ExtensionManager.service

%changelog
%autochangelog
