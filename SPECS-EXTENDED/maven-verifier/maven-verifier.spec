Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-verifier
Version:        1.7.2
Release:        8%{?dist}
Summary:        Apache Maven Verifier Component
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-verifier
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
%endif

%description
Provides a test harness for Maven integration tests.

%package javadoc
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q

# This test attempts to write outside the build directory
rm src/test/java/org/apache/maven/it/ForkedLauncherTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.7.2-8
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.2-5
- Unretire package in Fedora

* Fri Sep 11 2020 Marian Koncek <mkoncek@redhat.com> - 1.7.2-1
- Update to upstream version 1.7.2

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-8
- Mass rebuild for javapackages-tools 201902

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-7
- Mass rebuild for javapackages-tools 201901

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 12 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-3
- Remove outdated provides/obsoletes
- Update to current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 25 2015 Michal Srb <msrb@redhat.com> - 1.6-1
- Update to upstream release 1.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-2
- Fix unowned directory

* Mon Dec 09 2013 Michal Srb <msrb@redhat.com> - 1.5-1
- Update to upstream version 1.5

* Thu Oct  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6
- Add missing BR: maven-shared

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-4
- Update to maven-shared-utils 0.3

* Fri Feb 08 2013 Tomas Radej <tradej@redhat.com> - 1.4-3
- Building the new way

* Thu Jan 24 2013 Tomas Radej <tradej@redhat.com> - 1.4-2
- Added BuildRequires on maven-shared-utils

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 1.4-1
- Initial version

