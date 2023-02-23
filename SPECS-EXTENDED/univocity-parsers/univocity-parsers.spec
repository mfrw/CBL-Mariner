Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           univocity-parsers
Version:        2.9.1
Release:        6%{?dist}
Summary:        Collection of parsers for Java
License:        ASL 2.0
URL:            https://github.com/uniVocity/univocity-parsers
BuildArch:      noarch

Source0:        https://github.com/uniVocity/univocity-parsers/archive/v%{version}.tar.gz

Patch0:         0001-Resolve-import-clash-with-OpenJDK-17.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
%endif

%description
uniVocity-parsers is a suite of extremely fast and reliable parsers
for Java.  It provides a consistent interface for handling different
file formats, and a solid framework for the development of new
parsers.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-compiler-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
# Tests require univocity-output-tester, which is not packaged yet.
%mvn_build -f -- -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE-2.0.html

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.html

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.9.1-6
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-4
- Fix build with OpenJDK 17

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.9.1-2
- Bootstrap build
- Non-bootstrap build

* Sat Jan 30 2021 Fabio Valentini <decathorpe@gmail.com> - 2.9.1-1
- Update to version 2.9.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 26 2021 Marian Koncek <mkoncek@redhat.com> - 2.9.1-1
- Update to upstream version 2.9.1

* Fri Sep 11 2020 Marian Koncek <mkoncek@redhat.com> - 2.9.0-1
- Update to upstream version 2.9.0

* Fri Aug 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.9.0-1
- Update to version 2.9.0.

* Thu Aug 13 2020 Mat Booth <mat.booth@redhat.com> - 2.8.4-5
- Make OSGi requirement on com.googlecode.openbeans optional

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Marian Koncek <mkoncek@redhat.com> - 2.8.4-1
- Update to upstream version 2.8.4

* Tue Jul 14 2020 Mat Booth <mat.booth@redhat.com> - 2.8.4-3
- Allow building without tests

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.8.4-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Feb 13 2020 Fabio Valentini <decathorpe@gmail.com> - 2.8.4-1
- Update to version 2.8.4.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.8.3-2
- Mass rebuild for javapackages-tools 201902

* Sun Oct 06 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.3-1
- Update to version 2.8.3.

* Tue Aug 13 2019 Marian Koncek <mkoncek@redhat.com> - 2.8.3-1
- Update to upstream version 2.8.3

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Marian Koncek <mkoncek@redhat.com> - 2.8.2-1
- Update to upstream version 2.8.2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.5-6
- Mass rebuild for javapackages-tools 201901

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Mat Booth <mat.booth@redhat.com> - 2.5.5-4
- Remove unnecessary javadoc invocation

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.5-1
- Initial packaging
