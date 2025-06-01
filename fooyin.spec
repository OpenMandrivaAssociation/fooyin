Name:           fooyin
Version:        0.8.1
Release:        1
Summary:        A customisable music player built with Qt
License:        GPL-3.0-only
Group:		      Sound
URL:            https://github.com/ludouzi/%{name}
Source:         https://github.com/ludouzi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xkbcommon)

%description
fooyin is a Qt6 music player built around customisation. It offers a
growing list of widgets to manage and play a local music collection.
It is extendable through the use of plugins, and many widgets make
use of FooScript to offer an even deeper level of control.

%prep
%autosetup -p1

%build
%cmake -DBUILD_LIBVGM=OFF
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
