%global maj_ver 12
%global min_ver 0
%global patch_ver 1

%global clang_binaries \
    %{_bindir}/clang \
    %{_bindir}/clang++ \
    %{_bindir}/clang-%{maj_ver} \
    %{_bindir}/clang++-%{maj_ver} \
    %{_bindir}/clang-cl \
    %{_bindir}/clang-cpp \

%global clang_tools_binaries \
    %{_bindir}/clang-apply-replacements \
    %{_bindir}/clang-change-namespace \
    %{_bindir}/clang-check \
    %{_bindir}/clang-doc \
    %{_bindir}/clang-extdef-mapping \
    %{_bindir}/clang-format \
    %{_bindir}/clang-include-fixer \
    %{_bindir}/clang-move \
    %{_bindir}/clang-offload-bundler \
    %{_bindir}/clang-offload-wrapper \
    %{_bindir}/clang-query \
    %{_bindir}/clang-refactor \
    %{_bindir}/clang-rename \
    %{_bindir}/clang-reorder-fields \
    %{_bindir}/clang-scan-deps \
    %{_bindir}/clang-tidy \
    %{_bindir}/clangd \
    %{_bindir}/diagtool \
    %{_bindir}/hmaptool \
    %{_bindir}/pp-trace

%global clang_srcdir %{name}-%{version}.src
%global clang_tools_srcdir %{name}-tools-extra-%{version}.src

Summary:        C, C++, Objective C and Objective C++ front-end for the LLVM compiler.
Name:           clang
Version:        %{maj_ver}.%{min_ver}.%{patch_ver}
Release:        2%{?dist}
License:        NCSA
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Tools
URL:            https://clang.llvm.org
Source0:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/%{clang_srcdir}.tar.xz
Source1:        https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/%{clang_tools_srcdir}.tar.xz
BuildRequires:  cmake
BuildRequires:  libxml2-devel
BuildRequires:  llvm-devel = %{version}
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       libxml2
Requires:       llvm
Requires:       ncurses
Requires:       python3
Requires:       zlib
Provides:       %{name}-analyzer = %{version}-%{release}

%description
The goal of the Clang project is to create a new C based language front-end: C, C++, Objective C/C++, OpenCL C and others for the LLVM compiler. You can get and build the source today.

%package analyzer
Summary:        A source code analysis framework
License:        NCSA AND MIT
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package devel
Summary:        Development headers for clang
License:        NCSA
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires:       %{name}-tools-extra = %{version}-%{release}

%package libs
Summary:        Runtime library for clang
License:        NCSA
Recommends:     compiler-rt%{?_isa} = %{version}
Recommends:     libomp%{_isa} = %{version}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends:     libomp-devel%{_isa} = %{version}

%description libs
Runtime library for clang.

%description devel
The clang-devel package contains libraries, header files and documentation
for developing applications that use clang.

%package -n git-clang-format
Summary:        Integration of clang-format for git
License:        NCSA
Requires:       git
Requires:       python3

%description -n git-clang-format
clang-format integration for git.

%package tools-extra
Summary:        Extra tools for clang
License:        NCSA
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description tools-extra
A set of extra tools built using Clang's tooling API.

%prep
%setup -q -T -b 1 -n %{clang_tools_srcdir}

%setup -q -n %{clang_srcdir}

mv ../%{clang_tools_srcdir} tools/extra

%build
# Disable symbol generation
export CFLAGS="`echo " %{build_cflags} " | sed 's/ -g//'`"
export CXXFLAGS="`echo " %{build_cxxflags} " | sed 's/ -g//'`"

mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}   \
      -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
      -DCMAKE_BUILD_TYPE=Release    \
      -DLLVM_ENABLE_EH=ON \
      -DLLVM_ENABLE_RTTI=ON \
      -Wno-dev ..

%make_build

%install
cd build
%make_install

# Remove emacs integration files.
rm %{buildroot}%{_datadir}/clang/*.el

# Remove editor integrations (bbedit, sublime, emacs, vim).
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# Remove HTML docs
rm -Rvf %{buildroot}%{_pkgdocdir}
rm -Rvf %{buildroot}%{_datadir}/clang/clang-doc-default-stylesheet.css
rm -Rvf %{buildroot}%{_datadir}/clang/index.js

# Remove bash autocomplete files.
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
cd build
make clang-check

%files
%defattr(-,root,root)
%license LICENSE.TXT
%{clang_binaries}

%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*

%files libs
%{_libdir}/clang/
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%dir %{_datadir}/clang/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/cmake/*
%{_includedir}/clang/
%{_includedir}/clang-c/
%{_includedir}/clang-tidy/

%files -n git-clang-format
%{_bindir}/git-clang-format

%files tools-extra
%{clang_tools_binaries}
%{_bindir}/c-index-test
%{_bindir}/find-all-symbols
%{_bindir}/modularize
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%{_datadir}/clang/clang-include-fixer.py*
%{_datadir}/clang/clang-tidy-diff.py*
%{_datadir}/clang/run-clang-tidy.py*
%{_datadir}/clang/run-find-all-symbols.py*
%{_datadir}/clang/clang-rename.py*

%changelog
* Wed Sep 29 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 12.0.1-2
- Introduced following subpackages using Fedora 32 (license: MIT) spec as guidance:
  - clang-analyzer,
  - clang-libs,
  - clang-tools-extra.

* Fri Sep 17 2021 Chris Co <chrco@microsoft.com> - 12.0.1-1
- Update to 12.0.1

* Sat Sep 04 2021 Muhammad Falak <mwani@microsoft.com> - 8.0.1-5
- Add `git-clang-format` subpackage.

* Tue Apr 27 2021 Henry Li <lihl@microsoft.com> - 8.0.1-4
- Enable eh/rtti, which are required by lldb.

* Fri Jun 12 2020 Henry Beberman <henry.beberman@microsoft.com> 8.0.1-3
- Temporarily disable generation of debug symbols.

* Sat May 09 2020 Nick Samson <nisamson@microsoft.com> - 8.0.1-2
- Added %%license line automatically

* Tue Mar 17 2020 Henry Beberman <henry.beberman@microsoft.com> 8.0.1-1
- Update to 8.0.1. Fix Source0 URL. License verified.

* Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 6.0.1-2
- Initial CBL-Mariner import from Photon (license: Apache2).

* Thu Aug 09 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 6.0.1-1
- Update to version 6.0.1 to get it to build with gcc 7.3

* Wed Jun 28 2017 Chang Lee <changlee@vmware.com> 4.0.0-2
- Updated %check

* Fri Apr 7 2017 Alexey Makhalov <amakhalov@vmware.com> 4.0.0-1
- Version update

* Wed Jan 11 2017 Xiaolin Li <xiaolinl@vmware.com>  3.9.1-1
- Initial build.
