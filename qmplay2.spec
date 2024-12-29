#define _disable_lto 1
%define _disable_ld_no_undefined 1

#define debug_package	%{nil}
%define major 1
%define libname %mklibname %{name}_ %{major}
%define lib_name_devel  %mklibname %{name} -d

%define oname QMPlay2

Summary:	Video player
Name:		qmplay2
Version:	24.12.28
Release:	1
Source0:	https://github.com/zaps166/QMPlay2/releases/download/%{oname}-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
Patch0:		qmplay2-xcb-egl-integration.patch
#Patch1:		qmplay2-24.04.02-compile.patch
#Patch1:		qmplay-24.03.16-compile.patch
# https://github.com/llvm/llvm-project/issues/85552
Patch2:		qmplay2-workaround-clang-bug-85552.patch
Patch3:		qmplay2-default-vaapi-on.patch

URL:		https://zaps166.sourceforge.net/?app=QMPlay2
License:	LGPLv3
Group:		Video/Multimedia

BuildRequires:  ninja
BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
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
BuildRequires:	plasma6-workspace
BuildRequires:  glslc
BuildRequires:	vulkan-devel

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
        -DUSE_PULSEAUDIO:BOOL=ON \
        -DUSE_LINK_TIME_OPTIMIZATION:BOOL=ON \
	-DUSE_FFMPEG_VAAPI:BOOL=ON \
	-DFIND_HWACCEL_DRIVERS_PATH:BOOL=ON \
	-DUSE_OPENGL:BOOL=ON \
	-DUSE_VULKAN:BOOL=ON\
	-DUSE_GLSLC:BOOL=ON \
	-DUSE_FREEDESKTOP_NOTIFICATIONS:BOOL=ON\
	-DUSE_DBUS_SUSPEND:BOOL=ON \
	-DUSE_PCH:BOOL=ON \
	-DUSE_FFMPEG_VKVIDEO:BOOL=ON \
        -DBUILD_WITH_QT6:BOOL=ON

%build
%ninja_build -C build

%install
%ninja_install -C build
