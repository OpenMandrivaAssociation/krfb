Summary:	KDE Remote Desktop Server
Name:		krfb
Version:	22.12.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch0:		krfb-19.04.2-menuentry.patch
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libvncserver) >= 0.9.10
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(Qt5XkbCommonSupport)

%description
KDE Desktop Sharing is a server application that allows you to share your
current session with a user on another machine, who can use a VNC client
to view or even control the desktop.

%files -f %{name}.lang
%{_bindir}/krfb
%{_bindir}/krfb-virtualmonitor
%dir %{_libdir}/qt5/plugins/krfb
%dir %{_libdir}/qt5/plugins/krfb/events
%dir %{_libdir}/qt5/plugins/krfb/framebuffer
%{_libdir}/qt5/plugins/krfb/events/x11.so
%{_libdir}/qt5/plugins/krfb/events/xdp.so
%{_libdir}/qt5/plugins/krfb/framebuffer/pw.so
%{_libdir}/qt5/plugins/krfb/framebuffer/qt.so
%{_libdir}/qt5/plugins/krfb/framebuffer/xcb.so
%{_datadir}/krfb
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.krfb.appdata.xml
%{_datadir}/icons/*/*/*/krfb.*
%{_datadir}/qlogging-categories5/krfb.categories

#----------------------------------------------------------------------------

%define krfbprivate_major 5
%define libkrfbprivate %mklibname krfbprivate %{krfbprivate_major}

%package -n %{libkrfbprivate}
Summary:	KRFB shared library
Group:		System/Libraries
Obsoletes:	%{mklibname krfbprivate 4} < 3:15.12.0

%description -n %{libkrfbprivate}
KRFB shared library.

%files -n %{libkrfbprivate}
%{_libdir}/libkrfbprivate.so.%{krfbprivate_major}*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
