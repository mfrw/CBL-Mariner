Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-shared-utils
Version:        3.3.4
Release:        4%{?dist}
Summary:        Maven shared utility classes
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-shared-utils
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
# XXX temporary for maven upgrade
Patch1:         0001-Restore-compatibility-with-current-maven.patch
Patch2:         0002-Avoid-setting-POSIX-attributes-for-symbolic-links.patch

BuildRequires:  maven-local-openjdk8
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  %{?module_prefix}mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
%endif

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

%{?javadoc_package}

%prep
%setup -q

find -name '*.java' -exec sed -i 's/\r//' {} +

%patch1 -p1
%patch2 -p1

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin

%pom_remove_dep org.apache.commons:commons-text
rm src/test/java/org/apache/maven/shared/utils/CaseTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3.4-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Marian Koncek <mkoncek@redhat.com> - 3.3.4-1
- Update to upstream version 3.3.4

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3.3-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Marian Koncek <mkoncek@redhat.com> - 3.3.3-1
- Update to upstream version 3.3.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.2.1-0.6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-0.4
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-0.3
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.1-0.2
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 26 2018 Michael Simacek <msimacek@redhat.com> - 3.2.1-0.1
- Update to upstream version 3.2.1 (patched temporary)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Michael Simacek <msimacek@redhat.com> - 3.1.0-4
- Regenerate BuildRequires

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-2
- Re-enable tests

* Fri Jul 22 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-0.1.RC
- Update to upstream version 3.1.0
- Temporarly disable tests

* Fri Jul 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-2
- Remove unneeded build-requires

* Thu Jun  2 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-2
- Enable all tests

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Mon Sep 21 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9-1
- Update to upstream version 0.9

* Mon Jun 22 2015 Michal Srb <msrb@redhat.com> - 0.8-1
- Update to upstream release 0.8

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.7-1
- Update to upstream version 0.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.6-1
- Update to upstream version 0.6

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.5-3
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-2
- Fix unowned directory

* Mon Dec 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.5-1
- Update to upstream version 0.5
- Remove patch for MSHARED-285 (accepted upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Tomas Radej <tradej@redhat.com> - 0.4-1
- Updated to latest upstream version
- Fixed and reenabled tests

* Mon Apr 08 2013 Michal Srb <msrb@redhat.com> - 0.3-2
- Disable tests (they don't work with junit >= 4.11)

* Fri Mar 15 2013 Michal Srb <msrb@redhat.com> - 0.3-1
- Update to upstream version 0.3

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.2-4
- Build with xmvn

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 0.2-1
- Initial version
