%define pnpver 13
%define ixmlver 10
Name:           libupnp
Version:        1.8.4
Release:        1%{?dist}
Summary:        An implementation of Universal Plug and Play (UPnP)
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:            https://github.com/mrjimenez/pupnp
Source0:        https://downloads.sourceforge.net/pupnp/libupnp-%{version}.tar.bz2
%define sha1 libupnp=93e7b3c94cf53eb59533b4b7b137ef5cc651e28b
Patch0:         libupnp-configure.patch
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%package -n %{name}%{pnpver}
Summary:        An implementation of Universal Plug and Play (UPnP)
Group:          System/Libraries

%description -n %{name}%{pnpver}
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems

%package -n libixml%{ixmlver}
Summary:        The Portable UPnP SDK's XML library
Group:          System/Libraries

%description -n libixml%{ixmlver}
A C XML parsing library originally created for the Intel UPnP SDK for Linux.

%package devel
Summary:        The Portable Universal Plug and Play (UPnP) SDK
Group:          Development/Libraries/C and C++
Provides:       libixml-devel = %{version}-%{release}
Requires:       %{name}%{pnpver} = %{version}
Requires:       libixml%{ixmlver} = %{version}

%description devel
The Portable Universal Plug and Play (UPnP) SDK provides support for building
UPnP-compliant control points, devices, and bridges on several operating
systems.

%prep
%setup -q
%patch0 -p1

%build
# the openssl simply does not compile
autoreconf -fiv
%configure \
    --disable-samples \
    --enable-ipv6 \
    --disable-static \
    --enable-reuseaddr \
    --disable-open_ssl \
    --enable-unspecified_server
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig -n %{name}%{pnpver}
%postun -p /sbin/ldconfig -n %{name}%{pnpver}

%post -p /sbin/ldconfig -n libixml%{ixmlver}
%postun -p /sbin/ldconfig -n libixml%{ixmlver}

%files -n %{name}%{pnpver}
%doc ChangeLog
%license COPYING
%{_libdir}/libupnp.so.%{pnpver}*

%files -n libixml%{ixmlver}
%doc ChangeLog
%license COPYING
%{_libdir}/libixml.so.%{ixmlver}*

%files -n libupnp-devel
%{_libdir}/pkgconfig/libupnp.pc
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_includedir}/upnp/

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.8.4-1
-	Mariner initial version
