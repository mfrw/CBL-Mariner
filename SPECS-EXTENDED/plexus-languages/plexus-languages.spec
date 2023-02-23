Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           plexus-languages
Version:        1.0.6
Release:        6%{?dist}
Summary:        Plexus Languages
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh

# Upstream patch: Jars of which modulename extraction cause an exception should end up on the classpath
# https://github.com/codehaus-plexus/plexus-languages/issues/70
# https://issues.apache.org/jira/browse/SUREFIRE-1897
Patch0:         0001-70-Jars-of-which-modulename-extraction-cause-an-exce.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%{?javadoc_package}

%prep
%setup -q -n plexus-languages-plexus-languages-%{version}
%patch0 -p1

cp %{SOURCE1} .

%pom_remove_plugin :maven-enforcer-plugin

# Remove module build specific to Java 9
%pom_xpath_remove 'pom:profiles' plexus-java

%build
# many tests rely on bundled test jars/classes
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.6-6
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.6-4
- Add patch for SUREFIRE-1897

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.6-2
- Bootstrap build
- Non-bootstrap build

* Sat Jan 30 2021 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 26 2021 Marian Koncek <mkoncek@redhat.com> - 1.0.6-1
- Update to upstream version 1.0.6

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 1.0.5-6
- Rebuild correctly as a proper JPMS module

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 1.0.5-5
- Bootstrap restoration of essential JPMS classes

* Wed Jul 29 2020 Marian Koncek <mkoncek@redhat.com> - 1.0.5-1
- Update to upstream version 1.0.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-3
- Remove Java 9 specific classes for now to fix build.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.5-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Mar 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Update to version 1.0.5.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.10-5
- Mass rebuild for javapackages-tools 201902

* Fri Oct 11 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.10-4
- Mass rebuild for javapackages-tools 201901

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Michael Simacek <msimacek@redhat.com> - 0.9.10-3
- Repack tarball without bundled jars

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 0.9.10-1
- Update to upstream version 0.9.10

* Fri Jun 29 2018 Michael Simacek <msimacek@redhat.com> - 0.9.3-5
- Disable broken test

* Wed Feb 14 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-4
- Generate javadoc package automatically

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-2
- Replace JARs used as test resources with symlinks to system JARs

* Mon Sep 11 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.9.3-1
- Initial packaging
