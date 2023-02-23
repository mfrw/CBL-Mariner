Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-archiver
Version:        3.5.1
Release:        5%{?dist}
Summary:        Maven Archiver
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-archiver/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.5.1-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-2
- Bootstrap build
- Non-bootstrap build

* Sat Jan 30 2021 Fabio Valentini <decathorpe@gmail.com> - 0:3.5.1-1
- Update to version 3.5.1.

* Thu Jan 28 2021 Marian Koncek <mkoncek@redhat.com> - 3.5.1-1
- Update to upstream version 3.5.1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0:3.5.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Marian Koncek <mkoncek@redhat.com> - 3.5.0-1
- Update to upstream version 3.5.0

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.0-3
- Mass rebuild for javapackages-tools 201902

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 0:3.5.0-1
- Update to version 3.5.0.

* Thu Aug 08 2019 Marian Koncek <mkoncek@redhat.com> - 0:3.4.0-1
- Update to upstream version 3.4.0
- Fixes: RHBZ #1680430

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.4.0-2
- Mass rebuild for javapackages-tools 201901

* Wed Feb 27 2019 Marian Koncek <mkoncek@redhat.com> - 0:3.4.0-1
- Update to upstream version 3.4.0
- Fixes: RHBZ #1680430

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.2.0-1
- Update to upstream version 3.2.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.1.1-1
- Update to upstream version 3.1.1

* Thu Apr 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.2-1
- Update to upstream version 3.0.2

* Wed Apr 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:3.0.0-1
- Update to upstream version 3.0.0
- Remove legacy obsoletes/provides

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 27 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.6-1
- Update to upstream version 2.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.5-10
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-9
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-7
- Build with xmvn

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:2.5-6
- Add missing license files

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:2.5-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 16 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:2.5-2
- Add versioned BR/R on plexus-archiver and rebuild

* Wed Feb 15 2012 Alexander Kurtakov <akurtako@redhat.com> 0:2.5-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 6 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.2-1
- Update to 2.4.2 upstream release.

* Mon Sep 19 2011 Tomas Radej <tradej@redhat.com> - 0:2.4.1-7
- Fixed dep on maven-core artifact
- Minor fixes

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-6
- Build with maven 3.x.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-4
- Add missing BR.

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-3
- Remove tests as they don't compile.

* Mon May 31 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-2
- BR java-devel >= 1:1.6.0.

* Sat May 29 2010 Alexander Kurtakov <akurtako@redhat.com> 0:2.4.1-1
- Update to 2.4.1.

* Wed Dec 23 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.4-1
- Update to 2.4.

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-3
- BR maven-surefire-provider-junit.

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.2-2
- Fix line length.
- Own only specific fragment and pom.

* Wed May 20 2009 Fernando Nasser <fnasser@redhat.com> 0:2.2-1
- Fix license
- Update instructions to obtain sources
- Refresh source tar ball

* Thu Jul 26 2007 Deepak Bhole <dbhole@redhat.com> 0:2.2-0jpp.1
- Initial build
