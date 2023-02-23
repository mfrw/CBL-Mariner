Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           byte-buddy
Version:        1.12.0
Release:        3%{?dist}
Summary:        Runtime code generation for the Java virtual machine
License:        ASL 2.0
URL:            http://bytebuddy.net/
# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz

# Patch the build to avoid bundling inside shaded jars
Patch1:         0001-Avoid-bundling-asm.patch
Patch2:         0002-Remove-dependencies.patch
Patch3:         0003-Remove-Java-14-tests.patch
Patch4:         0004-Remove-JDK-15-sealed-classes.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-dep)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
%endif

BuildArch:      noarch

%description
Byte Buddy is a code generation library for creating Java classes during the
runtime of a Java application and without the help of a compiler. Other than
the code generation utilities that ship with the Java Class Library, Byte Buddy
allows the creation of arbitrary classes and is not limited to implementing
interfaces for the creation of runtime proxies. 

%package agent
Summary: Byte Buddy Java agent

%description agent
The Byte Buddy Java agent allows to access the JVM's HotSwap feature.

%package maven-plugin
Summary: Byte Buddy Maven plugin

%description maven-plugin
A plugin for post-processing class files via Byte Buddy in a Maven build.

%package parent
Summary: Byte Buddy parent POM

%description parent
The parent artifact contains configuration information that
concern all modules.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

rm byte-buddy-agent/src/test/java/net/bytebuddy/agent/VirtualMachineAttachmentTest.java
rm byte-buddy-agent/src/test/java/net/bytebuddy/agent/VirtualMachineForOpenJ9Test.java

# Cause pre-compiled stuff to be re-compiled
mv byte-buddy-dep/src/precompiled/java/net/bytebuddy/build/*.java \
  byte-buddy-dep/src/main/java/net/bytebuddy/build
mkdir -p byte-buddy-dep/src/test/java/net/bytebuddy/test/precompiled/
mv byte-buddy-dep/src/precompiled/java/net/bytebuddy/test/precompiled/*.java \
  byte-buddy-dep/src/test/java/net/bytebuddy/test/precompiled/

# Don't ship android or benchmark modules
%pom_disable_module byte-buddy-android
%pom_disable_module byte-buddy-android-test
%pom_disable_module byte-buddy-benchmark

# Don't ship gradle plugin
%pom_disable_module byte-buddy-gradle-plugin

# Remove check plugins unneeded by RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :pitest-maven
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :jitwatch-jarscan-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :nexus-staging-maven-plugin

# Avoid circural dependency
%pom_remove_plugin :byte-buddy-maven-plugin byte-buddy-dep

# Not interested in shading sources (causes NPE on old versions of shade plugin)
%pom_xpath_set "pom:createSourcesJar" "false" byte-buddy

# Drop build dep on findbugs annotations, used only by the above check plugins
%pom_remove_dep :findbugs-annotations
sed -i -e '/SuppressFBWarnings/d' $(grep -lr SuppressFBWarnings)

# Plugin for generating Java 9 module-info file is not in Fedora
%pom_remove_plugin -r :modulemaker-maven-plugin

%pom_remove_dep org.ow2.asm:asm-deprecated

%pom_remove_plugin :maven-shade-plugin byte-buddy
%pom_remove_plugin :maven-shade-plugin byte-buddy-benchmark

%pom_remove_dep net.java.dev.jna:jna byte-buddy
%pom_remove_dep net.java.dev.jna:jna byte-buddy-dep
%pom_remove_dep net.java.dev.jna:jna byte-buddy-agent

%pom_remove_dep net.java.dev.jna:jna-platform byte-buddy
%pom_remove_dep net.java.dev.jna:jna-platform byte-buddy-dep
%pom_remove_dep net.java.dev.jna:jna-platform byte-buddy-agent

%build
# Ignore test failures, there seems to be something different about the
# bytecode of our recompiled test resources, expect 6 test failures in
# the byte-buddy-dep module
%mvn_build -s -- -P'java8,!checks' -Dsourcecode.test.version=1.8 -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name} -f .mfiles-%{name}-dep
%doc README.md release-notes.md
%license LICENSE NOTICE

%files agent -f .mfiles-%{name}-agent
%license LICENSE NOTICE

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.12.0-3
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Marian Koncek <mkoncek@redhat.com> - 1.12.0-1
- Update to upstream version 1.12.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10.20-2
- Bootstrap build
- Non-bootstrap build

* Thu Feb 04 2021 Marian Koncek <mkoncek@redhat.com> - 1.10.20-1
- Update to upstream version 1.10.20

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Marian Koncek <mkoncek@redhat.com> - 1.10.16-1
- Update to upstram version 1.10.16

* Fri Aug 14 2020 Jerry James <loganjerry@gmail.com> - 1.10.14-1
- Version 1.10.14
- Remove no longer needed no-unixsocket.patch
- Add workaround for compiling tests with JDK 11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.9.5-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Marian Koncek <mkoncek@redhat.com> - 1.10.7-1
- Update to upstream version 1.10.7

* Thu Nov 21 2019 Marian Koncek <mkoncek@redhat.com> - 1.10.3-1
- Update to upstream version 1.10.3

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.10.1-2
- Mass rebuild for javapackages-tools 201902

* Thu Sep 12 2019 Marian Koncek <mkoncek@redhat.com> - 1.10.1-1
- Update to upstream version 1.10.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Marian Koncek <mkoncek@redhat.com> - 1.9.13-2
- Remove the dependency on maven-shade-plugin

* Thu Jun 06 2019 Marian Koncek <mkoncek@redhat.com> - 1.9.13-1
- Update to upstream version 1.9.13

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.5-5
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Mat Booth <mat.booth@redhat.com> - 1.9.5-4
- Prevent NPE in maven-shade-plugin

* Wed Dec 05 2018 Mat Booth <mat.booth@redhat.com> - 1.9.5-3
- Enable test suites

* Tue Dec 04 2018 Mat Booth <mat.booth@redhat.com> - 1.9.5-2
- Full, non-bootstrap build

* Fri Nov 30 2018 Mat Booth <mat.booth@redhat.com> - 1.9.5-1
- Update to latest upstream release
- Add a bootstrap mode to break circular self-dependency
- Patch out use of optional external unixsocket library that is not present
  in Fedora
- Patch to avoid bundling ASM inside the shaded jar

* Wed May 25 2016 gil cattaneo <puntogil@libero.it> 1.3.19-1
- update to 1.3.19

* Tue Dec 22 2015 gil cattaneo <puntogil@libero.it> 0.7.7-1
- initial rpm
