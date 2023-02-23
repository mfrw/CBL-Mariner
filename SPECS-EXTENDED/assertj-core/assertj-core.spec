Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           assertj-core
Version:        3.19.0
Release:        5%{?dist}
Summary:        Library of assertions similar to fest-assert
License:        ASL 2.0
URL:            https://joel-costigliola.github.io/assertj/
Source0:        https://github.com/joel-costigliola/assertj-core/archive/assertj-core-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif

%description
A rich and intuitive set of strongly-typed assertions to use for unit testing
(either with JUnit or TestNG).

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides API documentation for %{name}.

%prep
%setup -q -n assertj-core-assertj-core-%{version}

%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.assertj</groupId>"
%pom_xpath_remove "pom:release"

%pom_remove_plugin :maven-invoker-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :yuicompressor-maven-plugin
%pom_remove_plugin :bnd-maven-plugin
%pom_remove_plugin :bnd-resolver-maven-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :bnd-testing-maven-plugin

# package org.mockito.internal.util.collections does not exist
rm -rf ./src/test/java/org/assertj/core/error/ShouldContainString_create_Test.java

%pom_remove_dep :memoryfilesystem
rm -r src/test/java/org/assertj/core/internal/{Paths*.java,paths}

%build
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8 -P \!java9+

%install
%mvn_install

%files -f .mfiles
%doc README.md CONTRIBUTING.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc CONTRIBUTING.md
%license LICENSE.txt

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.19.0-5
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.19.0-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 26 2021 Marian Koncek <mkoncek@redhat.com> - 3.19.0-1
- Update to upstream version 3.19.0

* Wed Jan 20 2021 Marian Koncek <mkoncek@redhat.com> - 3.18.1-1
- Update to upstream version 3.18.1

* Fri Oct 16 2020 Fabio Valentini <decathorpe@gmail.com> - 3.17.2-1
- Update to version 3.17.2.

* Mon Sep 21 2020 Marian Koncek <mkoncek@redhat.com> - 3.17.2-1
- Update to upstream version 3.17.2

* Sun Aug 23 2020 Fabio Valentini <decathorpe@gmail.com> - 3.17.0-1
- Update to version 3.17.0.

* Wed Jul 29 2020 Marian Koncek <mkoncek@redhat.com> - 3.16.1-1
- Update to upstream version 3.16.1

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Markku Korkeala <markku.korkeala@iki.fi> - 3.16.1-4
- Remove profiles from pom.xml.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.16.1-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 13 2020 Fabio Valentini <decathorpe@gmail.com> - 3.16.1-2
- Fix artifact generation by removing antrun plugin again.

* Tue May 12 2020 Fabio Valentini <decathorpe@gmail.com> - 3.16.1-1
- Update to version 3.16.1.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Marian Koncek <mkoncek@redhat.com> - 3.14.0-1
- Update to upstream version 3.14.0

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.13.2-2
- Mass rebuild for javapackages-tools 201902

* Fri Sep 13 2019 Fabio Valentini <decathorpe@gmail.com> - 3.8.0-6
- Remove dependency on memoryfilesystem.

* Tue Aug 06 2019 Marian Koncek <mkoncek@redhat.com> - 3.13.2-1
- Update to upstream version 3.13.2

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Marian Koncek <mkoncek@redhat.com> - 3.12.2-1
- Update to upstream version 3.12.2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.8.0-3
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Mat Booth <mat.booth@redhat.com> - 3.8.0-1
- Update to latest version of assertj
- Disable tests due to missing deps in Fedora

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 2.2.0-3
- Add conditional for memoryfilesystem

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 02 2015 Roman Mohr <roman@fenkhuber.at> - 2.2.0-1
- Initial packaging
