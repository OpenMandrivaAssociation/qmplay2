%define _disable_lto 1

######################################################
# SpecFile: qmplay2.spec 
# Generato: http://www.mandrivausers.ro/
# MRB: Falticska Florin
######################################################
# empty debug
%define debug_package	%{nil}
%define major 1
%define libname %mklibname %{name}_ %{major}
%define lib_name_devel  %mklibname %{name} -d

######
%define name qmplay2
%define oname QMPlay2
%define release  2
%define version  18.07.03

Summary:	Video player
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	https://github.com/zaps166/QMPlay2/archive/%{oname}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

URL:		http://zaps166.sourceforge.net/?app=QMPlay2
License:	LGPLv3
Group:		Video

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(gl) 
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
Obsoletes:      qmplay2-12072013
Obsoletes:      qmplay2-common-12072013

# since now needs youtube-dl.Sflo
Requires:       youtube-dl
Requires:       %{libname} = %{EVRD}

# kde is Rosa's default DE no need to 
# split kde-integration package
# kdebase4 suggested to allow it on gnome and lxde
# without DE integration
Suggests:	kdebase4-workspace


%description
QMPlay2 is a video player, it can plays all formats 
and stream supported by ffmpeg and libmodplug 
(including J2B). It has integrated Youtube and Wrzuta browser.

%files  
%doc TODO ChangeLog
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
%doc TODO ChangeLog
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
%doc TODO ChangeLog
%{_includedir}/%{oname}
############################


%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
export CC=gcc
export CXX=g++
%cmake
%make_build

%install
%make_install -C build
