Summary:        libconfini
Name:           libconfini
Version:        1.16.0
Release:        2%{?dist}
License:        GPLv3
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Tools
URL:            https://madmurphy.github.io/libconfini/html/index.html
#Source0:       https://github.com/madmurphy/libconfini/archive/%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz

%description
libconfini is the ultimate and most consistent INI file parser library written in C.
Originally designed for parsing configuration files written by other programs, it
focuses on standardization and parsing exactness and is at ease with almost every
type of file containing key/value pairs.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
Development files for %{name}

%prep
%setup -q

%build
./bootstrap -z
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -delete -print

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%license COPYING
%doc %{_docdir}/%{name}
%{_mandir}/*
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Sep 10 2021 Thomas Crain <thcrain@microsoft.com> - 1.16.0-2
- Remove libtool archive files from final packaging

*  Fri Dec 11 2020 Jonathan Chiu <jochi@microsoft.com> 1.16.0-1
-  Original version for CBL-Mariner.
