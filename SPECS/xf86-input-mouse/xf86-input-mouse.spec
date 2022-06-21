%define xorg_ver %(pkg-config xorg-server --modversion|cut -d. -f 1-2)
Name:          xf86-input-mouse
Version:       1.9.2
Release:       1%{?dist}
Summary:       X.Org input drivers for mouse
Group:         System/X11
Vendor:        Microsoft Corporation
Distribution:  Mariner
License:       MIT
URL:           http://x.org
Source0:        ftp://ftp.freedesktop.org/pub/individual/driver/xf86-input-mouse-%{version}.tar.bz2
%define sha1 xf86-input-mouse=d3a0839ad5a33665bb261a4fba33e3a6271817dc
Patch0:        x86-input-mouse-patch.patch
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
%setup -q -n xf86-input-mouse-%{version}
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install


%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/input/mouse_drv.la
%{_libdir}/xorg/modules/input/mouse_drv.so
%{_mandir}/man4/mousedrv.4.gz

%files devel
%defattr(-,root,root)
%{_includedir}/xorg/xf86-mouse-properties.h
%{_libdir}/pkgconfig/xorg-mouse.pc

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.9.2-1
-	Mariner initial version

