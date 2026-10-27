%global _find_debuginfo_dwz_opts %{nil}
%undefine _debugsource_packages
# set rpath
%global ldflags %{ldflags} -Wl,-rpath -Wl,%{_libdir}/foo
Name:           fooyin
Version:        0.14.1
Release:        1
Summary:        A customisable music player built with Qt
License:        GPL-3.0-only
Group:		      Sound
URL:            https://fooyin.org/
Source0:         https://github.com/ludouzi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:	patchelf
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
BuildRequires:	pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake(QCoro6)

#FIXME add projectM 4 as br

%description
fooyin is a Qt6 music player built around customisation. It offers a
growing list of widgets to manage and play a local music collection.
It is extendable through the use of plugins, and many widgets make
use of FooScript to offer an even deeper level of control.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake
%make_build

%install
%make_install -C build

# tip from ROSA Linux
# set rpath
patchelf --set-rpath '$ORIGIN/../%{_lib}/%{name}' %{buildroot}%{_bindir}/%{name}

# libs
for lib in %{buildroot}%{_libdir}/fooyin/libfooyin_*.so*; do
    patchelf --set-rpath '$ORIGIN' "$lib"
done

%files
%license COPYING
%doc README.md  
%doc %{_datadir}/doc/fooyin/LICENSE 
%doc %{_datadir}/doc/fooyin/README
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{name}.*
%{_datadir}/%{name}
%{_libdir}/%{name}/
