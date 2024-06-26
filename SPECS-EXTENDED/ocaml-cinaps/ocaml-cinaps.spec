Vendor:         Microsoft Corporation
Distribution:   Mariner
# TESTING NOTE: The ppx_jane module is needed to run the tests.  However,
# ppx_jane transitively requires this module.  Therefore, we cannot run the
# tests at all until we are able to add ppx_jane to Fedora, and even then we
# will only be able to run the tests in non-bootstrap mode.

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global srcname cinaps

Name:           ocaml-%{srcname}
Version:        0.15.1
Release:        2%{?dist}
Summary:        Trivial Metaprogramming tool using the OCaml toplevel

License:        MIT
URL:            https://github.com/ocaml-ppx/%{srcname}
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  help2man
BuildRequires:  ocaml >= 4.04.0
BuildRequires:  ocaml-dune >= 2.0.0
BuildRequires:  ocaml-re-devel >= 1.8.0

%description
Cinaps is a trivial Metaprogramming tool for OCaml using the OCaml
toplevel.

It is intended for two purposes:
- when you want to include a bit of generated code in a file, but writing
  a proper generator/ppx rewriter is not worth it;
- when you have many repeated blocks of similar code in your program, to
  help writing and maintaining them.

It is not intended as a general preprocessor, and in particular can only
be used to generate static code that is independent of the system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-re-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%build
dune build

%install
dune install --destdir=%{buildroot}

# We install the documentation with the doc macro
rm -fr %{buildroot}%{_prefix}/doc

%ifarch %{ocaml_native_compiler}
# Add missing executable bits
chmod a+x %{buildroot}%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmxs
%endif

# Generate the man page
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N --version-string=%{version} %{buildroot}%{_bindir}/cinaps > \
  %{buildroot}%{_mandir}/man1/cinaps.1

%files
%doc README.org
%license LICENSE.md
%{_bindir}/cinaps
%{_mandir}/man1/cinaps.1*
%dir %{_libdir}/ocaml/%{srcname}/
%dir %{_libdir}/ocaml/%{srcname}/runtime/
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cma
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmi
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmxs
%endif

%files devel
%{_libdir}/ocaml/%{srcname}/dune-package
%{_libdir}/ocaml/%{srcname}/opam
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.a
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmx
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmxa
%endif
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmt
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.cmti
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.ml
%{_libdir}/ocaml/%{srcname}/runtime/cinaps_runtime.mli

%changelog
* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 0.15.1-2
- Initial CBL-Mariner import from Fedora 34 (license: MIT).

* Sat Feb 13 2021 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- Version 0.15.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0
- New URLs

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-6
- Add missing ocaml-re-devel R to the -devel subpackage

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-5
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.14.0-4
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Mon May 04 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-7
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-6
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-5
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-4
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 0.13.0-2
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan  2 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
