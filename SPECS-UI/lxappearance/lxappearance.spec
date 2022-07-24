Summary:	desktop-independent theme switcher for GTK+.
Name:		lxappearance
Version:	0.6.3
Release:	2%{?dist}
License:	GPLv2+
URL:		http://downloads.sourceforge.net/lxde
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
%define sha1 lxappearance=1c281756b240694d0262edd9d40041d5b127d552
BuildRequires: glibc-devel gtk3 gtk3-immodules gtk3-immodule-xim
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: glib-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: pango-devel
BuildRequires: libX11-devel
BuildRequires: intltool
BuildRequires: dbus-glib-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

%description
The LXAppearance package contains a desktop-independent theme switcher for GTK+.
%package 	devel
Group:          Development/Libraries
Summary:        Headers and static lib for application development
Requires:	%{name} = %{version}
Requires:	intltool gtk2-devel gtk2-devel dbus-glib-devel
%description 	devel
Install this package if you want do compile applications using the pcre
library.

%prep
%setup -q
%build
%configure \
	--enable-dbus \
	--enable-gtk2 \
        %{nil}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_bindir}/lxappearance
%{_datadir}/applications/lxappearance.desktop
%{_datadir}/lxappearance/ui/about.ui
%{_datadir}/lxappearance/ui/lxappearance.ui
%{_mandir}/man1/lxappearance.1*
%doc AUTHORS COPYING
%{_datadir}/locale/*

%files devel
%defattr(-,root,root)
%{_includedir}/lxappearance/lxappearance.h
%{_libdir}/pkgconfig/lxappearance.pc
%doc NEWS README

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 0.6.3-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.6.3-1
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.6.1-1
-	initial version
