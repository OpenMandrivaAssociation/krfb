Summary:	KDE Remote Desktop Server
Name:		krfb
Version:	15.08.0
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
Source0:	http://download.kde.org/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		krfb-4.11.0-desktop.patch
Patch1:		krfb-4.11.0-soversion.patch
BuildRequires:	jpeg-devel
BuildRequires:	kdelibs-devel
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
%{_bindir}/krfb                                                                                        
%{_datadir}/apps/krfb                                                                                  
%{_datadir}/applications/kde4/krfb.desktop                                                             
%{_libdir}/kde4/krfb_*.so                                                                              
%{_datadir}/kde4/services/krfb*.desktop                                                                
%{_datadir}/kde4/servicetypes/krfb*.desktop                                                            
%doc %{_docdir}/HTML/*/krfb                                                                            
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
%{_libdir}/libkrfbprivate.so.%{krfbprivate_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
