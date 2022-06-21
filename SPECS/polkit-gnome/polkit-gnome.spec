Name:          polkit-gnome
Version:       0.105
Release:       2%{?dist}
Summary:       PolicyKit integration for the GNOME desktop
Group:         System/Libraries
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:           http://www.freedesktop.org/wiki/Software/PolicyKit
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/polkit-gnome/%{version}/polkit-gnome-%{version}.tar.xz
%define sha1 polkit-gnome=948bad76395834a1b45b65bd191d46145f5c0b9f
License:       LGPL
BuildRequires: glibc-devel
BuildRequires: gtk-doc
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glib-devel
BuildRequires: gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: pixman-devel
BuildRequires: libpng-devel
# BuildRequires: libpthread-stubs-devel
BuildRequires: libselinux-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXrender-devel
BuildRequires: zlib-devel
BuildRequires: polkit-devel
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Provides:      polkit-gnome-devel
Obsoletes:     polkit-gnome-devel
Obsoletes:     polkit-gnome-apidocs
Requires:      at-spi2-core

%description
%{name} provides an authentication agent for PolicyKit that matches the look and feel of the GNOME desktop

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
PolicyKit integration for the GNOME desktop.

This package contains static libraries and header files need for development.

%package apidocs
Summary:       %{name} API documentation
Group:         Documentation
Requires:      gtk-doc

%description apidocs
%{name} API documentation.

%prep
%setup -q

%build
%configure \
	 --enable-gtk-doc \
	 --disable-introspection
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

#echo 'NotShowIn=KDE;' >> %{buildroot}%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
#%{_sysconfdir}/xdg/autostart/polkit-gnome-*.desktop
#%{_libdir}/libpolkit-gtk-*.so.*
%{_libexecdir}/polkit-gnome-*
# %{_libdir}/girepository-1.0/*.typelib
%doc AUTHORS COPYING
# NEWS README TODO
%{_datadir}/locale/*

#%files devel
#%defattr(-,root,root)
#%{_includedir}/polkit-gtk-1/polkitgtk/*.h
#%{_libdir}/libpolkit-gtk-*.*a
#%{_libdir}/libpolkit-gtk-*.so
#%{_exec_prefix}/lib/pkgconfig/*.pc
# %{_datadir}/gir-1.0/*.gir

#%files apidocs
#%defattr(-,root,root)
#%dir %{_datadir}/gtk-doc/html/polkit-gtk-1
#%{_datadir}/gtk-doc/html/polkit-gtk-1/*

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.105-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.105-1
-	Mariner initial version
