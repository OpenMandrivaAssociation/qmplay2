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
%define version  14.12.01

Summary:	Video player
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://kent.dl.sourceforge.net/project/zaps166/%{oname}/%{oname}-src-%{version}.tar.bz2
Source100:	%{name}.rpmlintrc
Patch0:		QMplay2-desktop.patch

URL:		http://zaps166.sourceforge.net/?app=QMPlay2
License:	LGPLv3
Group:		Video

BuildRequires:  qt4-devel
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
BuildRequires:  kdebase4-workspace
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
%doc COPYING TODO ChangeLog
%{_bindir}/%{oname}
%{_iconsdir}/%{oname}.png
%{_iconsdir}/hicolor/128x128/apps/QMPlay2.png
%{_miconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
# keep this for kde integration
%{_datadir}/apps/solid/actions/*
%{_datadir}/applications/*.desktop
%{_datadir}/qmplay2/
#############################

%package -n %{libname}

Summary:	Shared library of %{oname}
Group:		System/Libraries

%description -n %{libname}
qmplay2 dynamic libraries.

%files -n %{libname}
%doc TODO ChangeLog
%{_libdir}/libqmplay2.so.%{major}*
%{_libdir}/modules/*.so

%exclude %{_libdir}/libqmplay2.so

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
%{_libdir}/libqmplay2.so
############################


%prep
%setup -qn %{oname}-src
perl -pi -e 's|"/"|"/" |' src/modules/Inputs/Inputs.cpp
%patch0 -p0


%build
NOTERM=1 SYSTEM_BUILD=1 ./compile_unix 1

%install
# gen rpmtree
mkdir -p %{buildroot}{%{_bindir},%{_libdir}}
# install
mv app/lib/libqmplay2.* %{buildroot}%{_libdir}
install -m755 app/bin/%{oname} %{buildroot}%{_bindir}/%{oname}
mv app/share %{buildroot}/usr
#
# modules scam
mv %{buildroot}%{_datadir}/qmplay2/modules %{buildroot}%{_libdir}

pushd %{buildroot}%{_datadir}/qmplay2
ln -s  %{_libdir}/modules modules
popd

# icons
# we convert and install the icons properly 
rm -fr %{buildroot}%{_iconsdir}/*.png
#
install -d -m755 %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert src/gui/Icons/QMPlay2.png -resize 32x32 %{buildroot}%{_iconsdir}/%{oname}.png
convert src/gui/Icons/QMPlay2.png -resize 16x16 %{buildroot}%{_miconsdir}/%{oname}.png
convert src/gui/Icons/QMPlay2.png -resize 48x48 %{buildroot}%{_liconsdir}/%{oname}.png

desktop-file-validate %{buildroot}%{_datadir}/applications/%{oname}.desktop
rm -fr %{buildroot}%{_datadir}/qmplay2/noautoupdates
rm -fr %{buildroot}%{_datadir}/qmplay2/ChangeLog

%changelog
* Sat Mar 08 2014 SymbianFlo <symbianflo@mandrivausers.ro> 14.03.05-1
+ Revision: 26051a5
- Log: Update to  14.03.05 , - Improved operation YouTube - operated by the "youtube-dl" (required to provide the path in the options),
- AudioCD disc title displayed as the album,
- Fixed bug with refreshing OSD
- Fixed bugs in editing tags


