Summary:	Frontend for DOSBox, ScummVM and VDMSound
Name:		gr-lida
Version:	0.11.0
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		http://www.gr-lida.org/
Source0:	https://github.com/Monthy/gr-lida/archive/%{name}-%{version}.tar.gz
Patch0:		gr-lida-0.11.0-zlib.patch
BuildRequires:	librsvg
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(zlib)

%description
GR-lida is an open source frontend for DOSBox, ScummVM and VDMSound.
It can display games using pictureflow, which is a clone of Apples cover flow.

%files
%doc doc/COPYING.txt doc/AUTHORS.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GR-lida
Comment=Frontend for DOSBox, ScummVM and VDMSound
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

# Install icons of various sizes
for s in 256 128 96 48 32 22 16 ; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
rsvg-convert -w ${s} -h ${s} \
    %{name}.svg -o \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
