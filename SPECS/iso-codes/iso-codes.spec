%global debug_package %{nil}
Summary:	ISO code lists and translations
Name:		iso-codes
Version:	4.2
Release:	1%{?dist}
License:	MIT
URL:		http://anduin.linuxfromscratch.org/BLFS/
Group:		System Environment/Base
Vendor:		Microsoft Corporation
Distribution:	Mariner
Source0:	http://anduin.linuxfromscratch.org/BLFS/%{name}/%{name}-%{version}.tar.xz
%define sha1 iso-codes=e32f25d6d79e93845b82329332d776707019850c
BuildRequires:	gettext python3 pkg-config
Requires:	gettext pkg-config python3
%description
This package provides the ISO 639 Language code list, the ISO 4217
Currency code list, the ISO 3166 Territory code list, and ISO 3166-2
sub-territory lists, and all their translations in gettext format.

%package devel
Summary: Files for development using %{name}
Group:  Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the pkg-config files for development
when building programs that use %{name}.


%prep
%setup -q

%build
%configure
make %{_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang iso-codes --all-name

%files -f iso-codes.lang
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml
%{_datadir}/iso-codes/json/*.json

%files devel
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 4.2-1
-	Mariner initial version

