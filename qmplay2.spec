#define _disable_lto 1
%define _disable_ld_no_undefined 1

#define debug_package	%{nil}
%define major 1
%define libname %mklibname %{name}_ %{major}
%define lib_name_devel  %mklibname %{name} -d

%define oname QMPlay2

Summary:	Video player
Name:		qmplay2
Version:	23.06.17
Release:	2
Source0:	https://github.com/zaps166/QMPlay2/releases/download/%{oname}-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
Patch0:		qmplay2-xcb-egl-integration.patch

URL:		http://zaps166.sourceforge.net/?app=QMPlay2
License:	LGPLv3
Group:		Video/Multimedia

BuildRequires:  ninja
BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
#BuildRequires:	cmake(Qt6X11Extras)
BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpipewire-0.3)
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
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(gl) 
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  sidplay-devel
BuildRequires:  desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:	plasma-workspace
BuildRequires:  glslc

# since now needs youtube-dl.Sflo
Requires:       yt-dlp
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
%autosetup -p1 -n %{oname}-src-%{version}
%cmake  \
        -G Ninja \
        -DCMAKE_BUILD_TYPE=Release \
        -DUSE_PULSEAUDIO=ON \
        -DUSE_LINK_TIME_OPTIMIZATION=ON \
        -DBUILD_WITH_QT6=ON

%build
%ninja_build -C build

%install
%ninja_install -C build
