Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           maven-reporting-impl
Version:        3.1.0
Release:        1%{?dist}
Summary:        Abstract classes to manage report generation
License:        ASL 2.0
URL:            https://maven.apache.org/shared/maven-reporting-impl/
BuildArch:      noarch

Source0:        https://www.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip
Source1:        https://www.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip.asc
# Apache Maven public key
Source2:        https://www.apache.org/dist/maven/KEYS
# Fedora does not have junit-addons
Patch0:         0001-Remove-dependency-on-junit-addons.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-decoration-model)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-site-renderer)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%{?javadoc_package}

%description
Abstract classes to manage report generation, which can be run both:

* as part of a site generation (as a maven-reporting-api's MavenReport),
* or as a direct standalone invocation (as a maven-plugin-api's Mojo).

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1

# integration tests try to download stuff from the internet
# and therefore they don't work in Koji
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
* Wed Feb  9 2022 Jerry James <loganjerry@gmail.com> - 3.1.0-1
- Version 3.1.0
- Verify the sources

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.0-14
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov  6 2021 Jerry James <loganjerry@gmail.com> - 3.0.0-12
- Require JDK 1.8 instead of 1.6 to fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.0.0-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-4
- Remove legacy obsoletes/provides
- Remove dependency on junit-addons
- Remove build-dependency on maven-invoker-plugin

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 12 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Michal Srb <msrb@redhat.com> - 2.4-1
- Update to upstream version 2.4
- Fix BR

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-1
- Update to upstream version 2.3

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-11
- Fix build-requires on parent POM
- Port to Doxia 1.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-9
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-8
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-6
- Add missing BuildRequires

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-5
- Skip running tests outsides Fedora

* Tue Feb 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-4
- Build with xmvn

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Feb 05 2013 Michal Srb <msrb@redhat.com> - 2.2-2
- Migrate from maven-doxia to doxia subpackages

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 2.2-1
- Initial version

