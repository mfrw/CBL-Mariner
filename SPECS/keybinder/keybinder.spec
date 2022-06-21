Name:		keybinder
Version:	0.3.1
Release:	22%{?dist}
Summary:	A library for registering global keyboard shortcuts
License:	MIT
URL:		https://github.com/engla/keybinder
Source0:	%url/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gtk2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	%{_bindir}/gtkdocize
Obsoletes:		python2-%{name} < 0.3.1-16
 
 
%description
keybinder is a library for registering global keyboard shortcuts. 
Keybinder works with GTK-based applications using the X Window System.
 
The library contains:
- A C library, libkeybinder
- An examples directory with programs in C, Lua, and Vala.
 
%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
 
%description	devel
This package contains the development files for %{name}.
 
 
%prep
%setup -q -n %{name}-%{version}
sed -i -e 's@-rpath @@g' libkeybinder/Makefile.in \
 lua-keybinder/Makefile.in python-keybinder/Makefile.in
autoreconf -fiv
 
%build
PY2_STATUS=disable
%configure --disable-static --${PY2_STATUS}-python --disable-lua \
	--disable-silent-rules
%make_build
%install
%make_install
#Remove libtool archives.
find %{buildroot} -name '*.la'| xargs rm -f
 
 
%ldconfig_scriptlets
%files
%doc NEWS AUTHORS README
%{_libdir}/libkeybinder.so.* 
%{_libdir}/girepository-1.0/Keybinder-*.typelib
%{_datadir}/gir-1.0/Keybinder-*.gir

 
%files devel
%{_includedir}/keybinder.h
%{_libdir}/pkgconfig/keybinder.pc
%{_libdir}/libkeybinder.so
%{_datadir}/gtk-doc/html/%{name}

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 0.3.0-2
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 0.3.0-1
-	initial version
