Summary:        Theme engines for GTK+ 2.0
Name:           gtk2-engines
Version:        2.20.2
Release:        1%{?dist}
Vendor:		Microsoft Corporation
Distribution:	Mariner
License:        LGPLv2+
Group:          System Environment/Libraries
URL:            http://download.gnome.org/sources/gtk-engines
Source0:         http://download.gnome.org/sources/gtk-engines/2.20/gtk-engines-%{version}.tar.bz2
%define sha1 gtk-engines=574c7577d70eaacecd2ffa14e288ef88fdcb6c2a

BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  pkg-config
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  perl-File-Find

Patch0: gtk-engines-2.18.2-change-bullet.patch
# turn on new tooltips look
Patch1: tooltips.patch
# enable automatic mnemonics
Patch2: auto-mnemonics.patch
# allow dragging on empty areas in menubars
Patch3: window-dragging.patch


%description
The gtk2-engines package contains shared objects and configuration
files that implement a number of GTK+ theme engines. Theme engines
provide different looks for GTK+, some of which resemble other
toolkits or operating systems.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries

%description devel
The gtk2-engines-devel package contains files needed to develop
software that uses the theme engines in the gtk2-engines package.

%prep
%setup -q -n gtk-engines-%{version}

%patch0 -p1 -b .bullet
%patch1 -p1 -b .tooltips
%patch2 -p1 -b .mnemonics
%patch3 -p1 -b .window-dragging

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root, -)
%doc README AUTHORS NEWS COPYING
%{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_datadir}/themes/*
%{_datadir}/gtk-engines
%{_datadir}/locale/*

%files devel
%defattr(-, root, root, -)
%{_libdir}/pkgconfig/gtk-engines-2.pc
%{_libdir}/gtk-2.0/2.10.0/engines/*.la

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 2.20.2-1
-	Mariner initial version


