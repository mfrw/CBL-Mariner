Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-artifact-transfer
Version:        0.13.1
Release:        6%{?dist}
Epoch:          1
Summary:        Apache Maven Artifact Transfer
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-artifact-transfer
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Compatibility-with-Maven-3.0.3-and-later.patch
Patch1:         0002-Remove-support-for-maven-3.0.X.patch
Patch2:         0003-Port-to-maven-3.8.1.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-impl)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

%description
An API to either install or deploy artifacts with Maven 3.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q
find -name '*.java' -exec sed -i 's/\r//' {} +
%patch0 -p1
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin

# We don't want to support legacy Maven versions (older than 3.1)
%pom_remove_dep org.sonatype.aether:
find -name Maven30\*.java -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:0.13.1-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Marian Koncek <mkoncek@redhat.com> - 1:0.13.1-4
- Port to maven 3.8.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.13.1-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Marian Koncek <mkoncek@redhat.com> - 0.13.1-1
- Update to upstream version 0.13.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:0.11.0-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Marian Koncek <mkoncek@redhat.com> - 0.12.0-1
- Update to upstream version 0.12.0

* Tue Nov 05 2019 Marian Koncek <mkoncek@redhat.com> - 1:0.11.0-1
- Update to upstream version 0.11.0

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.9.0-6
- Mass rebuild for javapackages-tools 201902

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1:0.11.0-1
- Update to version 0.11.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:0.9.0-5
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 07 2016 Michael Simacek <msimacek@redhat.com> - 0.9.0-1
- Update to upstream version 0.9.0

* Tue Aug 23 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-0.4.20160823svn1753832
- Update to latest upstream snapshot

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.3.20160118svn1722498
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-0.2.20160118svn1722498
- Update to latest upstream snapshot

* Tue Jun  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-0.1.20151012svn1708080
- Initial packaging
