Name:           fooyin
Version:        0.9.2
Release:        1
Summary:        A customisable music player built with Qt
License:        GPL-3.0-only
Group:		      Sound
URL:            https://github.com/ludouzi/%{name}
Source0:         https://github.com/ludouzi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/ValleyBell/libvgm/archive/libvgm-305b1bad78f7486c9e4058191abdd9195775efa0.zip

# from opensuse
Patch0:  Fix-compatibility-with-Qt-6.10.1.patch
Patch1:  Add-missing-header-include-for-QElapsedTimer-class.patch

BuildRequires:  make
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Linguist)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
#BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)

%description
fooyin is a Qt6 music player built around customisation. It offers a
growing list of widgets to manage and play a local music collection.
It is extendable through the use of plugins, and many widgets make
use of FooScript to offer an even deeper level of control.

%prep
%autosetup -p1 -a1

cp -r libvgm-*/* 3rdparty/libvgm/

%build
%cmake
%make_build

%install
%make_install -C build


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/doc/%{name}
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.*
%{_datadir}/%{name}
%{_libdir}/%{name}/
