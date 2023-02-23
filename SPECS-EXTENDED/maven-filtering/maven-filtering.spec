Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-filtering
Version:        3.2.0
Release:        5%{?dist}
Summary:        Shared component providing resource filtering
License:        ASL 2.0
URL:            https://maven.apache.org/shared/%{name}/index.html
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:         0001-Skip-failed-tests.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api::tests:)
%endif

%description
These Plexus components have been built from the filtering process/code in 
Maven Resources Plugin. The goal is to provide a shared component for all 
plugins that needs to filter resources.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch1 -p1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.2.0-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Marian Koncek <mkoncek@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.1.1-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-7
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-6
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul  6 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-2
- Regenerate build-requires

* Fri Jun  3 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.1-1
- Update to upstream version 3.1.1

* Wed Apr 13 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1.0-1
- Update to upstream version 3.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0
- Remove legacy obsoletes/provides
- Update to current packaging guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-1
- Update to upstream version 1.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-4
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Nov 27 2012 Tomas Radej <tradej@redhat.com> - 1.0-9
- Added NOTICE to javadoc

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 15 2012 Tomas Radej <tradej@redhat.com> - 1.0-7
- Replaced plexus-maven-plugin with plexus-containers-component-metadata

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-5
- Really fixed Provides/Obsoletes

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-4
- Fixed Provides/Obsoletes

* Wed Aug 31 2011 Tomas Radej <tradej@redhat.com> - 1.0-3
- Added Provides/Obsoletes

* Tue Aug 16 2011 Tomas Radej <tradej@redhat.com> 1.0-2
- Removed rm -rf {buildroot}

* Tue Aug 16 2011 Tomas Radej <tradej@redhat.com> 1.0-1
- Initial release (thanks to the GULaG team)
