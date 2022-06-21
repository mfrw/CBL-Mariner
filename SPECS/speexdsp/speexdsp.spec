Name:           speexdsp
Version:        1.2
%global rc_ver  rc3
Release:        0.15.%{rc_ver}%{?dist}
Summary:        An Open Source, Patent Free Speech Codec
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Vendor:		Microsoft Corporation
Distribution:	Mariner
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{name}-%{version}%{rc_ver}.tar.gz
%define sha1 speexdsp=818403a21ec428feb39fe58f6cb6836d595e639b
# taken from upstream boo#929450
Patch0:         speexdsp-fixbuilds-774c87d.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  libogg-devel

Conflicts: speex <= 1.2-0.21.rc1

%description
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
Summary: 	Development package for %{name}
Requires: 	%{name}%{?_isa} = %{version}-%{release}
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts: speex-devel <= 1.2-0.21.rc1


%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

This is the DSP package, see the speex package for the codec part.

%prep
%setup -q -n %{name}-%{version}%{rc_ver}
%patch0 -p1 -b .inc

%build
autoreconf -vif

%configure \
%ifarch aarch64
	--disable-neon \
%endif
	--disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install


# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING TODO ChangeLog README NEWS doc/manual.pdf
%doc %{_docdir}/speexdsp/manual.pdf
%{_libdir}/libspeexdsp.so.*

%files devel
%{_includedir}/speex
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.2-0.15.
-	Mariner initial version
