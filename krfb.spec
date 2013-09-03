Summary:	KDE Remote Desktop Server
Name:		krfb
Version:	4.11.1
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
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		krfb-4.11.0-desktop.patch
Patch1:		krfb-4.11.0-soversion.patch
BuildRequires:	jpeg-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(TelepathyQt4)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)

%description
KDE Desktop Sharing is a server application that allows you to share your
current session with a user on another machine, who can use a VNC client
to view or even control the desktop.

%files
%{_kde_bindir}/krfb
%{_kde_appsdir}/krfb
%{_kde_applicationsdir}/krfb.desktop
%{_kde_libdir}/kde4/krfb_*.so
%{_kde_services}/krfb*.desktop
%{_kde_servicetypes}/krfb*.desktop
%{_kde_docdir}/HTML/*/krfb
#### Telepathy-Qt4-based optional feature ####
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.krfb_rfb*.service
%{_datadir}/telepathy/clients/krfb_rfb*.client

#----------------------------------------------------------------------------

%define krfbprivate_major 4
%define libkrfbprivate %mklibname krfbprivate %{krfbprivate_major}

%package -n %{libkrfbprivate}
Summary:	KRFB shared library
Group:		System/Libraries

%description -n %{libkrfbprivate}
KRFB shared library.

%files -n %{libkrfbprivate}
%{_kde_libdir}/libkrfbprivate.so.%{krfbprivate_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did
