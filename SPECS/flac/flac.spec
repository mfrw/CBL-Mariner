Name:           flac
Version:        1.3.2
Release:       1%{?dist}
Summary:        Free Lossless Audio Codec
License:        BSD-3-Clause AND GPL-2.0-or-later AND GFDL-1.2-only
Group:          Productivity/Multimedia/Sound/Utilities
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:            https://xiph.org/flac/
Source0:         http://downloads.xiph.org/releases/flac/%{name}-%{version}.tar.xz
%define sha1 flac=2bdbb56b128a780a5d998e230f2f4f6eb98f33ee
Patch0:         flac-cflags.patch
Patch1:         flac-CVE-2017-6888.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  libogg-devel
Obsoletes:      %{name}-doc
%ifarch %{ix86}
BuildRequires:  nasm
%endif

%description
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation. Digital audio compressed by FLAC's
algorithm can typically be reduced to between 50 and 70 percent of
its original size, and decompresses to an identical copy of the
original audio data.

%package -n libFLAC8
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries
Obsoletes:      libflac < %{version}
Provides:       libflac = %{version}

%description -n libFLAC8
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C API library for FLAC.

%package -n libFLAC++6
Summary:        Free Lossless Audio Codec Library
Group:          System/Libraries

%description -n libFLAC++6
FLAC is an audio coding format for lossless compression of digital
audio, and is also the name of the reference software package that
includes a codec implementation.

This package contains the C++ API library for FLAC.

%package devel
Summary:        FLAC Library Development Package
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libFLAC++6 = %{version}
Requires:       libFLAC8 = %{version}
Requires:       libstdc++-devel

%description devel
This package contains the files needed to compile programs that use the
FLAC library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fvi
%configure \
	--disable-silent-rules \
	--disable-thorough-tests \
	--disable-xmms-plugin \
	--disable-static \
	--disable-rpath \
	--enable-sse
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# wrongy installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/

%check
make check %{?_smp_mflags}

%post -n libFLAC8 -p /sbin/ldconfig
%postun -n libFLAC8 -p /sbin/ldconfig
%post -n libFLAC++6 -p /sbin/ldconfig
%postun -n libFLAC++6 -p /sbin/ldconfig

%files
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man*/*

%files -n libFLAC8
%license COPYING*
%{_libdir}/libFLAC.so.8*

%files -n libFLAC++6
%license COPYING*
%{_libdir}/libFLAC++.so.6*

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.3.2-1
-	Mariner initial version


