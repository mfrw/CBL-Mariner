Name:           graphite2
Version:        1.3.12
Release:        4%{?dist}
Summary:        Font rendering capabilities for complex non-Roman writing systems
License:        LGPL-2.1-or-later OR MPL-2.0+
Vendor:		Microsoft Corporation
Distribution:	AzureMarine
Group:          Productivity/Publishing/Word
Url:            http://graphite.sil.org/
#Source0:        https://github.com/silnrsi/graphite/archive/%{name}-%{version}.tgz
Source0:		https://github.com/silnrsi/graphite/releases/download/1.3.12/%{name}-%{version}.tgz
%define sha1 graphite2=3f2f9da5875eeb3b43c14ad3b469e2582b33c0b2
Patch0:         graphite2-1.2.0-cmakepath.patch
Patch2:         link-gcc-shared.diff
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  libgcc-devel
BuildRequires:  glib-devel
BuildRequires:  pkg-config
BuildRequires:  python3

%description
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

%package devel
Summary:        Files for Developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
Graphite2 is a project within SIL's Non-Roman Script Initiative and Language
Software Development groups to provide rendering capabilities for complex
non-Roman writing systems. Graphite can be used to create "smart fonts" capable
of displaying writing systems with various complex behaviors. With respect to
the Text Encoding Model, Graphite handles the "Rendering" aspect of writing
system implementation.

This package contains the %{name} development files.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch2 -p1

# Make sure to use python3 everywhere
find tests -type f -exec sed -i "s|python|python3|g" {} +
find . -name *.cmake -exec sed -i "s|python|python3|g" {} +

%build
%cmake \
	-DGRAPHITE2_COMPARE_RENDERER=OFF \
	-DGRAPHITE2_NTRACING=ON \
	-DCMAKE_SKIP_RPATH=OFF
# Do not use O3, from debian
find . -type f \
	-exec sed -i -e 's/\-O3//g' {} \;

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

#%check
# exclude tests based on fonttool
#cd build
#ctest --output-on-failure --force-new-ctest-process %{?_smp_mflags} \
#    -E "padaukcmp1|chariscmp1|chariscmp2|annacmp1|schercmp1|awamicmp1|awamicmp2|awamicmp3"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc LICENSE COPYING
%{_bindir}/gr2fonttest
%{_libdir}/*.so.3*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}*
%{_libdir}/%{name}*

%changelog
*	Fri Jun 05 2020 Andrew Phelps <anphel@microsoft.com> 1.3.12-2
-	Rename package dependencies for MM5 release.
*	Thu Feb 13 2020 Suresh Babu Chalamalasetty <schalam@microsoft.com> 1.3.12-1
-	Mariner initial version
