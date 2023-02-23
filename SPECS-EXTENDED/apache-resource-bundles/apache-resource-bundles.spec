Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

%global jar_version 1.4
%global lh_version 1.1
%global id_version 1.1

Name:           apache-resource-bundles
Version:        30
Release:        5%{?dist}
Summary:        Apache Resource Bundles
License:        ASL 2.0
URL:            https://repo1.maven.org/maven2/org/apache/apache-resource-bundles/
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/apache/resources/%{name}/%{version}/%{name}-%{version}.pom
Source1:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}-sources.jar
Source2:        https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/%{jar_version}/apache-jar-resource-bundle-%{jar_version}.pom
Source3:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}-sources.jar
Source4:        https://repo1.maven.org/maven2/org/apache/apache-license-header-resource-bundle/%{lh_version}/apache-license-header-resource-bundle-%{lh_version}.pom
Source5:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}-sources.jar
Source6:        https://repo1.maven.org/maven2/org/apache/apache-incubator-disclaimer-resource-bundle/%{id_version}/apache-incubator-disclaimer-resource-bundle-%{id_version}.pom

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
%endif

%description
An archive which contains templates for generating the necessary license files
and notices for all Apache releases.

%prep
%setup -cT
cp -p %{SOURCE0} ./pom.xml
%pom_xpath_inject 'pom:project' '
<modules>
  <module>apache-jar-resource-bundle</module>
  <module>apache-license-header-resource-bundle</module>
  <module>apache-incubator-disclaimer-resource-bundle</module>
</modules>'

%pom_xpath_set 'pom:project/pom:parent/pom:relativePath' '../pom/maven/pom.xml'
%pom_xpath_set 'pom:project/pom:groupId' 'org.apache'

# jar
mkdir -p apache-jar-resource-bundle
pushd apache-jar-resource-bundle
jar xvf %{SOURCE1}
cp -p %{SOURCE2} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# license-header
mkdir -p apache-license-header-resource-bundle
pushd apache-license-header-resource-bundle
jar xvf %{SOURCE3}
cp -p %{SOURCE4} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

# incubator-disclaimer
mkdir -p apache-incubator-disclaimer-resource-bundle
pushd apache-incubator-disclaimer-resource-bundle
jar xvf %{SOURCE5}
cp -p %{SOURCE6} ./pom.xml
%pom_xpath_set 'pom:project/pom:parent/pom:version' %{version}
mkdir -p src/main/resources
mv META-INF src/main/resources
popd

%mvn_file :apache-jar-resource-bundle apache-resource-bundles/jar
%mvn_file :apache-license-header-resource-bundle apache-resource-bundles/license-header
%mvn_file :apache-incubator-disclaimer-resource-bundle apache-resource-bundles/incubator-disclaimer

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 30-5
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 30-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2-25
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Mar 04 2020 Marian Koncek <mkoncek@redhat.com> - 30-1
- Update to upstream version 30

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-22
- Mass rebuild for javapackages-tools 201902

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-21
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-15
- Cleanup spec file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2-13
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2-12
- Fix unowned directory

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2-10
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 2-9
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2-5
- Fix pom file names and add_to_maven_depmap calls (Resolves rhbz#655790)

* Wed Sep 8 2010 Alexander Kurtakov <akurtako@redhat.com> 2-4
- Add maven-site-plugin BR.
- Use newer names of maven plugins.

* Mon Feb  1 2010 Mary Ellen Foster <mefoster at gmail.com> 2-3
- Fix license 

* Tue Jan 19 2010 Mary Ellen Foster <mefoster at gmail.com> 2-2
- Add plugin dependencies from POMs
- Fix description
- Remove maven-release plugin (not on Fedora yet)

* Mon Jan 18 2010 Mary Ellen Foster <mefoster at gmail.com> 2-1
- Initial package
