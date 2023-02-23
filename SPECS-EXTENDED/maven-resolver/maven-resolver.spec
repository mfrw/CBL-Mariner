Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

%if %{without bootstrap} && !0%{?rhel}
%bcond_without maven_resolver_extra_modules
%else
%bcond_with maven_resolver_extra_modules
%endif

Name:           maven-resolver
Epoch:          1
Version:        1.7.3
Release:        3%{?dist}
License:        ASL 2.0
Summary:        Apache Maven Artifact Resolver library
URL:            https://maven.apache.org/resolver/
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/maven/resolver/%{name}-%{version}-source-release.zip

Patch0:         0001-Remove-use-of-deprecated-SHA-1-and-MD5-algorithms.patch

BuildRequires:  maven-local-openjdk8
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)
%endif
%if %{with maven_resolver_extra_modules}
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-http)
BuildRequires:  mvn(org.eclipse.jetty:jetty-server)
BuildRequires:  mvn(org.eclipse.jetty:jetty-util)
%endif

Provides:       maven-resolver-api = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-spi = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-impl = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-util = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-connector-basic = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-wagon = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-http = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-file = %{epoch}:%{version}-%{release}
Provides:       maven-resolver-transport-classpath = %{epoch}:%{version}-%{release}

Obsoletes:      maven-resolver-api < 1:1.4.2-6
Obsoletes:      maven-resolver-spi < 1:1.4.2-6
Obsoletes:      maven-resolver-impl < 1:1.4.2-6
Obsoletes:      maven-resolver-util < 1:1.4.2-6
Obsoletes:      maven-resolver-connector-basic < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-wagon < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-http < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-file < 1:1.4.2-6
Obsoletes:      maven-resolver-transport-classpath < 1:1.4.2-6
Obsoletes:      maven-resolver-test-util < 1:1.4.2-6

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%{?javadoc_package}

%prep
%setup -q
%patch0 -p1

# requires internet connection
rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/HttpTransporterTest.java

%pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
%pom_remove_plugin -r org.apache.maven.plugins:maven-enforcer-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
%pom_disable_module maven-resolver-transport-classpath
%if %{without maven_resolver_extra_modules}
%pom_disable_module maven-resolver-transport-file
%pom_disable_module maven-resolver-transport-http
%endif
%mvn_package :maven-resolver-test-util __noinstall

# generate OSGi manifests
for pom in $(find -mindepth 2 -name pom.xml) ; do
  %pom_add_plugin "org.apache.felix:maven-bundle-plugin" $pom \
  "<configuration>
    <instructions>
      <Bundle-SymbolicName>\${project.groupId}$(sed 's:./maven-resolver::;s:/pom.xml::;s:-:.:g' <<< $pom)</Bundle-SymbolicName>
      <Export-Package>!org.eclipse.aether.internal*,org.eclipse.aether*</Export-Package>
      <_nouses>true</_nouses>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>create-manifest</id>
      <phase>process-classes</phase>
      <goals><goal>manifest</goal></goals>
    </execution>
  </executions>"
done
%pom_add_plugin "org.apache.maven.plugins:maven-jar-plugin" pom.xml \
"<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
  </archive>
</configuration>"

%mvn_alias 'org.apache.maven.resolver:maven-resolver{*}' 'org.eclipse.aether:aether@1'
%mvn_file ':maven-resolver{*}' %{name}/maven-resolver@1 aether/aether@1

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.7.3-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Marian Koncek <mkoncek@redhat.com> - 1:1.7.3-1
- Update to upstream version 1.7.3

* Thu Oct 28 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.6.1-7
- Remove use of deprecated SHA-1 and MD5 algorithms

* Sun Oct 03 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1:1.6.1-6
- Enable transport-file and transport-http module

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.6.1-4
- Add epoch to obsoleted packages

* Tue Jun 01 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.6.1-3
- Obsolete removed subpackages

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.6.1-2
- Bootstrap build
- Non-bootstrap build

* Wed Feb 17 2021 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.2-5
- Build with -release 8 for better OpenJDK 8 compatibility.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Marian Koncek <mkoncek@redhat.com> - 1.6.1-1
- Update to upstream version 1.6.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.4.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Marian Koncek <mkoncek@redhat.com> - 1.4.2-1
- Update to upstream version 1.4.2

* Sat May 09 2020 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.2-1
- Update to version 1.4.2.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 25 2020 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-3
- Build with OpenJDK 8

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-2
- Mass rebuild for javapackages-tools 201902

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 1:1.4.1-1
- Update to version 1.4.1.

* Wed Sep 11 2019 Marian Koncek <mkoncek@redhat.com> - 1.4.1-1
- Update to upstream version 1.4.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.3.3-3
- Disable unneeded transporters

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.3.3-2
- Mass rebuild for javapackages-tools 201901

* Tue May 14 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.3.3-1
- Update to upstream version 1.3.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Marian Koncek <mkoncek@redhat.com> - 1:1.3.1-1
- Update to upstream version 1.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1.1-2
- Remove aether provides

* Mon Feb 26 2018 Michael Simacek <msimacek@redhat.com> - 1:1.1.1-1
- Update to upstream version 1.1.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1.0-2
- Obsolete aether-ant-tasks
- Resolves: rhbz#1516043

* Wed Oct 25 2017 Michael Simacek <msimacek@redhat.com> - 1:1.1.0-1
- Update to upstream version 1.1.0

* Thu Aug 24 2017 Mat Booth <mat.booth@redhat.com> - 1:1.0.3-7
- Fix OSGi metadata to also export "impl" packages; "internal" packages remain
  unexported

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0.3-5
- Add aether alias for main POM file

* Tue May 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.0.3-4
- Fix duplicate Bundle-SymbolicName in OSGi manifests

* Mon May 15 2017 Mat Booth <mat.booth@redhat.com> - 1:1.0.3-3
- Restore OSGi metadata that was lost in the switch from "aether" to
  "maven-resolver"

* Wed Apr 12 2017 Michael Simacek <msimacek@redhat.com> - 1:1.0.3-2
- Split into subpackages
- Obsolete and provide aether

* Tue Apr 11 2017 Michael Simacek <msimacek@redhat.com> - 1.0.3-1
- Initial packaging
