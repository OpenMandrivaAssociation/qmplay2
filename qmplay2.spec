%define debug_package	%{nil}
%define major 1
%define libname %mklibname %{name}_ %{major}
%define lib_name_devel  %mklibname %{name} -d

%define oname QMPlay2

Summary:	Video player
Name:		qmplay2
Version:	20.05.02
Release:	1
Source0:	https://github.com/zaps166/QMPlay2/archive/%{oname}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
URL:		http://zaps166.sourceforge.net/?app=QMPlay2
License:	LGPLv3
Group:		Video

BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(gl) 
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  sidplay-devel
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:	plasma-workspace
Obsoletes:      qmplay2-12072013
Obsoletes:      qmplay2-common-12072013

# since now needs youtube-dl.Sflo
Requires:       youtube-dl
Requires:       %{libname} = %{EVRD}

%description
QMPlay2 is a video player, it can plays all formats 
and stream supported by ffmpeg and libmodplug 
(including J2B). It has integrated Youtube and Wrzuta browser.

%files  
%doc ChangeLog
%{_bindir}/%{oname}
%{_iconsdir}/hicolor/*/apps/%{oname}.*
%{_mandir}/man1/%{oname}.1*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.xml
%{_datadir}/qmplay2/
%{_datadir}/solid/actions/QMPlay2-opencda.desktop
%{_datadir}/mime/packages/*

#############################

%package -n %{libname}

Summary:	Shared library of %{oname}
Group:		System/Libraries

%description -n %{libname}
qmplay2 dynamic libraries.

%files -n %{libname}
%doc ChangeLog
%{_libdir}/libqmplay2.so
%{_libdir}/%{name}/modules/*.so

#############################

%package -n %{lib_name_devel}
Group:      Development/Other
Summary:    Development libs for %{oname}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{EVRD}

%description -n %{lib_name_devel}
Development libs for %{oname}.

%files -n    	%{lib_name_devel}
%doc ChangeLog
%{_includedir}/%{oname}
############################


%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build
