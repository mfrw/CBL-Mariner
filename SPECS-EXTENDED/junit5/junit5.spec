Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

# Component versions, taken from gradle.properties
%global platform_version 1.%(v=%{version}; echo ${v:2})
%global jupiter_version %{version}
%global vintage_version %{version}

Name:           junit5
Version:        5.7.1
Release:        5%{?dist}
Summary:        Java regression testing framework
License:        EPL-2.0
URL:            https://junit.org/junit5/
BuildArch:      noarch

Source0:        https://github.com/junit-team/junit5/archive/r%{version}/junit5-%{version}.tar.gz

# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/%{platform_version}/junit-platform-commons-%{platform_version}.pom
Source201:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console/%{platform_version}/junit-platform-console-%{platform_version}.pom
Source202:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/%{platform_version}/junit-platform-console-standalone-%{platform_version}.pom
Source203:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/%{platform_version}/junit-platform-engine-%{platform_version}.pom
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source206:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-runner/%{platform_version}/junit-platform-runner-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source208:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-reporting/%{platform_version}/junit-platform-reporting-%{platform_version}.pom
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
# Jupiter POMs
Source300:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
Source305:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
# BOM POM
Source500:      https://repo1.maven.org/maven2/org/junit/junit-bom/%{version}/junit-bom-%{version}.pom

BuildRequires:  asciidoc
BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif

%description
JUnit is a popular regression testing framework for Java platform.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Junit5 API documentation.

%package guide
Summary:        Documentation for %{name}
Requires:       %{name}-javadoc = %{version}-%{release}

%description guide
JUnit 5 User Guide.

%prep
%setup -q -n %{name}-r%{version}
find -name \*.jar -delete

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE205} junit-platform-launcher/pom.xml
cp -p %{SOURCE206} junit-platform-runner/pom.xml
cp -p %{SOURCE207} junit-platform-suite-api/pom.xml
cp -p %{SOURCE208} junit-platform-reporting/pom.xml
cp -p %{SOURCE209} junit-platform-testkit/pom.xml
cp -p %{SOURCE300} junit-jupiter/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE305} junit-jupiter/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml
cp -p %{SOURCE500} junit-bom/pom.xml

for pom in $(find -mindepth 2 -name pom.xml); do
    # Set parent to aggregator
    %pom_xpath_inject pom:project "<parent><groupId>org.fedoraproject.xmvn.junit5</groupId><artifactId>aggregator</artifactId><version>1.0.0</version></parent>" $pom
    # OSGi BSN
    bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep net.sf.jopt-simple:jopt-simple:5.0.4 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

# Disable the console modules
%pom_disable_module junit-platform-console
%pom_disable_module junit-platform-console-standalone

%mvn_package :aggregator __noinstall

%build
%mvn_build -f

# Build docs.  Ignore exit asciidoc -- it fails for some reason, but
# still produces readable docs.
asciidoc documentation/src/docs/asciidoc/index.adoc || :
ln -s ../../javadoc/junit5 documentation/src/docs/api

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md LICENSE-notice.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md LICENSE-notice.md

%files guide
%doc documentation/src/docs/*

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.7.1-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.7.1-2
- Bootstrap build
- Non-bootstrap build

* Fri May 14 2021 Marian Koncek <mkoncek@redhat.com> - 5.7.1-1
- Update to upstream version 5.7.1

* Fri Feb 19 2021 Mat Booth <mat.booth@redhat.com> - 5.7.1-1
- Update to latest upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 24 2020 Fabio Valentini <decathorpe@gmail.com> - 5.7.0-1
- Update to version 5.7.0.

* Mon Sep 21 2020 Marian Koncek <mkoncek@redhat.com> - 5.7.0-1
- Update to upstream version 5.7.0

* Tue Aug 11 2020 Jerry James <loganjerry@gmail.com> - 5.6.2-4
- Add org.junit.jupiter:junit-jupiter, org.junit.platform:junit-platform-testkit

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Marian Koncek <mkoncek@redhat.com> - 5.6.2-1
- Update to upstream version 5.6.2

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 5.6.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 5.6.2-1
- Update to version 5.6.2.

* Wed Mar 04 2020 Marian Koncek <mkoncek@redhat.com> - 5.6.0-1
- Update to upstream version 5.6.0

* Mon Feb 17 2020 Alexander Scheel <ascheel@redhat.com> - 5.6.0-1
- Update to version 5.6.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.5.2-3
- Mass rebuild for javapackages-tools 201902

* Mon Oct 28 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.5.2-2
- Build and install junit-jupiter aggregator

* Sun Oct 13 2019 Fabio Valentini <decathorpe@gmail.com> - 5.5.2-1
- Update to version 5.5.2.

* Wed Sep 11 2019 Marian Koncek <mkoncek@redhat.com> - 5.5.2-1
- Update to upstream version 5.5.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Marian Koncek <mkoncek@redhat.com> - 5.5.1-1
- Update to upstream version 5.5.1

* Sat Jun 08 2019 Fabio Valentini <decathorpe@gmail.com> - 5.4.2-1
- Update to version 5.4.2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.4.0-2
- Mass rebuild for javapackages-tools 201901

* Wed Mar 06 2019 Mat Booth <mat.booth@redhat.com> - 5.4.0-1
- Update to latest upstream release
- License switched to EPL only now the surefire provider was moved to the
  Apache Surefire project

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 11 2018 Mat Booth <mat.booth@redhat.com> - 5.3.1-1
- Update to latest upstream release
- Conditionally build the console modules
- Remove stuff for discontinued gradle plugin

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 5.2.0-3
- Add explicit requirement on javapackages-tools since junit5 script
  uses java-functions. See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Mat Booth <mat.booth@redhat.com> - 5.2.0-1
- Update to latest upstream release

* Wed Jun 27 2018 Mat Booth <mat.booth@redhat.com> - 5.0.0-4
- Add java 9 automatic module name headers to jar files
- License correction EPL -> EPL-2.0

* Thu Mar 15 2018 Michael Simacek <msimacek@redhat.com> - 5.0.0-3
- Disable gradle plugin to fix FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 14 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.0.0-1
- Initial packaging
