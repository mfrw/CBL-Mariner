Summary:	library for writing single instance applications.
Name:		libunique
Version:	1.1.6
Release:	3%{?dist}
License:	LGPLv2+
URL:		http://www.gnome.org
Group:		User Interface/Desktops
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
%define sha1 libunique=d44ad06503efaaa0c660c5f8a817e90fbe254d1f
Patch0:         libunique1-gcc46.patch
Patch1:         libunique1-no_g_const_return.patch
BuildRequires:	autoconf automake gtk2-devel pkg-config
Requires:	gtk2

%description
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%package -n libunique-1_0-0
Summary:        A library for writing single instance applications
Group:          System/Libraries

%description -n libunique-1_0-0
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%package -n typelib-1_0-Unique-1_0
Summary:        Introspection bindings for libunique
Group:          System/Libraries

%description -n typelib-1_0-Unique-1_0
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

This package provides the GObject Introspection bindings for libunique.

%package devel
Summary:        Development files for libunique
Group:          Development/Libraries/GNOME
Requires:       libunique-1_0-0 = %{version}
Requires:       typelib-1_0-Unique-1_0 = %{version}

%description devel
Unique is a library for writing single instance applications. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
CFLAGS="`echo " %{build_cflags} " | sed 's/-Werror=format-security/-Wno-error=format-security/'`"
CXXFLAGS="`echo " %{build_cxxflags} " | sed 's/-Werror=format-security/-Wno-error=format-security/'`"
export CFLAGS
export CXXFLAGS
# We use --disable-maintainer-flags to allow building with deprecated API
%configure \
    --enable-debug=no \
    --enable-static=no \
    --enable-dbus=yes \
    --disable-maintainer-flags
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libunique-1_0-0 -p /sbin/ldconfig
%postun -n libunique-1_0-0 -p /sbin/ldconfig

%files -n libunique-1_0-0
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.0*

%files -n typelib-1_0-Unique-1_0
# %{_libdir}/girepository-1.0/Unique-1.0.typelib

%files devel
%{_includedir}/unique-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
# %{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/unique

%changelog
*	Mon Jun 29 2020 Andrew Phelps <anphel@microsoft.com> 1.1.6-3
-	Modify cflags to fix compilation errors.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.1.6-2
-	Mariner initial version
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.1.6-1
-	initial version
