%define majver %(echo %version | cut -d. -f1-2)
Name:          lxrandr
Version:       0.3.1
Release:       2%{?dist}
Summary:       Simple monitor configuration tool
Group:         Graphical Desktop/Applications/Environment
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.lxde.org/
Source0:        http://downloads.sourceforge.net/project/lxde/LXRandR%20%28monitor%20config%20tool%29/LXRandR%20%{majver}.x/lxrandr-%{version}.tar.xz
%define sha1 lxrandr=f7378e54388b6e0003e6c00dfb9352caa018d554
Patch0:        %{name}-0.1.1-fix-infinite-loop.patch
License:       GPL

BuildRequires: glibc-devel
BuildRequires: atk-devel gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: intltool desktop-file-utils
BuildRequires: libXrandr-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

%description
LXRandR is a simple monitor configuration tool utilizing X RandR extension.
It's a GUI frontend of the command line program xrandr and manages screen resolution and external monitors.
When you run LXRandR with an external monitor or projector connected, its GUI will change and show you some options to quickly configure the external device.

LXRandR is the standard screen manager of LXDE, the Lightweight X11 Desktop Environment, but can be used in other desktop environments as well.

%prep
%setup -q
#%patch0 -p1
# quick fix for the icon
echo "Icon=video-display" >> data/%{name}.desktop.in

%build
#sed -i "s|AM_PROG_CC_STDC|AC_PROG_CC|" configure.in
#autoreconf
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%find_lang %{name}

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/lxrandr
%{_mandir}/man1/lxrandr.*.gz
%{_datadir}/applications/lxrandr.desktop

%doc AUTHORS COPYING

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.3.1-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.3.1-1
-	Mariner initial version
