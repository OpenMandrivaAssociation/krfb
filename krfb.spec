#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Remote Desktop Server
Name:		krfb
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/krfb/-/archive/%{gitbranch}/krfb-%{gitbranchd}.tar.bz2#/krfb-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/krfb-%{version}.tar.xz
%endif
Source1:	%{name}.rpmlintrc
Patch0:		krfb-19.04.2-menuentry.patch
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libvncserver) >= 0.9.10
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(libpipewire-0.3)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DNSSD)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	cmake(KPipeWire) < 6.27.60
BuildRequires:	cmake(KWayland)
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE Desktop Sharing is a server application that allows you to share your
current session with a user on another machine, who can use a VNC client
to view or even control the desktop.

%files -f krfb.lang
%{_bindir}/krfb
%{_bindir}/krfb-virtualmonitor
%dir %{_libdir}/qt6/plugins/krfb
%dir %{_libdir}/qt6/plugins/krfb/events
%dir %{_libdir}/qt6/plugins/krfb/framebuffer
%{_libdir}/qt6/plugins/krfb/events/x11.so
%{_libdir}/qt6/plugins/krfb/events/xdp.so
%{_libdir}/qt6/plugins/krfb/framebuffer/pw.so
#%{_libdir}/qt6/plugins/krfb/framebuffer/qt.so
%{_libdir}/qt6/plugins/krfb/framebuffer/xcb.so
%{_datadir}/krfb
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.krfb.appdata.xml
%{_datadir}/icons/*/*/*/krfb.*
%{_datadir}/qlogging-categories6/krfb.categories
%{_libdir}/libkrfbprivate.so*

#----------------------------------------------------------------------------

%install -a
%find_lang krfb --with-html
