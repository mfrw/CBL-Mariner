Name:          xf86-input-keyboard
Version:       1.9.0
Release:       1%{?dist}
Summary:       X.Org input drivers for keyboards
Group:         System/X11
Vendor:        Microsoft Corporation
Distribution:  Mariner
URL:           http://x.org
Source0:        ftp://ftp.freedesktop.org/pub/individual/driver/xf86-input-keyboard-%{version}.tar.bz2
%define sha1 xf86-input-keyboard=24b5d84d221a75650f390ff63315912bf9a94992
License:       MIT
BuildRequires:	pixman-devel libpciaccess-devel pkg-config systemd-devel
BuildRequires:       xorg-x11-server-devel
BuildRequires:       xorg-x11-server-Xorg
BuildRequires:       xorg-x11-server-Xwayland
BuildRequires:       xorg-x11-server-Xvfb

Requires:       xorg-x11-server-Xorg
Requires:       xorg-x11-server-Xwayland
Requires:       xorg-x11-server-Xvfb

Requires:	pixman libpciaccess pkg-config systemd

%description
X.Org input drivers for mouse.

%package devel
Summary:       Devel files for %{name}
Group:         Development/Libraries

%description devel
Devel files for %{name}.

%prep
%setup -q -n xf86-input-keyboard-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install


%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/kbd_drv.la
%{_libdir}/xorg/modules/input/kbd_drv.so
%{_mandir}/man4/kbd.4.gz

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.9.0-1
-	Mariner initial version

