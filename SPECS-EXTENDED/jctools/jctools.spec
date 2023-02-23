Vendor:         Microsoft Corporation
Distribution:   Mariner
%global srcname JCTools

Name:           jctools
Version:        3.3.0
Release:        1%{?dist}
Summary:        Java Concurrency Tools for the JVM
License:        ASL 2.0

URL:            https://github.com/JCTools/JCTools
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core) >= 3.14.16
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)

# unused parent package was removed for fedora 33+
Obsoletes:      %{name}-parent < 3.1.0-1

# unused channels and experimental modules disabled with 3.1.0 for fedora 33+
# Unsafe.defineClass is not available in JDK 11:
# https://github.com/JCTools/JCTools/issues/254
Obsoletes:      %{name}-channels < 3.1.0-1
Obsoletes:      %{name}-experimental < 3.1.0-1

%description
This project aims to offer some concurrent data structures
currently missing from the JDK:

° SPSC/MPSC/SPMC/MPMC Bounded lock free queues
° SPSC/MPSC Unbounded lock free queues
° Alternative interfaces for queues
° Offheap concurrent ring buffer for ITC/IPC purposes
° Single Writer Map/Set implementations
° Low contention stats counters
° Executor


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{srcname}-%{version}

# drop some failure-prone tests (race conditions?)
rm jctools-core/src/test/java/org/jctools/queues/MpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/queues/atomic/AtomicMpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/maps/NonBlockingHashMapTest.java

# set correct version in all pom.xml files
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set pom:parent/pom:version %{version} jctools-{build,core,channels,experimental}

# remove plugins unnecessary for RPM builds
%pom_remove_plugin :coveralls-maven-plugin jctools-core
%pom_remove_plugin :jacoco-maven-plugin jctools-core
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin jctools-core
%pom_remove_plugin :maven-javadoc-plugin jctools-core

# remove tests with additional kotlin dependencies
%pom_remove_dep org.jetbrains.kotlinx:lincheck jctools-core
rm -r jctools-core/src/test/java/org/jctools/maps/linearizability_test/

# disable unused modules with unavailable dependencies
%pom_disable_module jctools-benchmarks
%pom_disable_module jctools-concurrency-test

# incompatible with Java 11 and unused in fedora:
# https://github.com/JCTools/JCTools/issues/254
%pom_disable_module jctools-channels
%pom_disable_module jctools-experimental

# do not install internal build tools
%mvn_package :jctools-build __noinstall

# do not install unused parent POM
%mvn_package :jctools-parent __noinstall


%build
%mvn_build -s


%install
%mvn_install


%files -f .mfiles-jctools-core
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Tue Aug 10 2021 Sérgio Basto <sergio@serjux.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Fabio Valentini <decathorpe@gmail.com> - 3.2.0-1
- Update to version 3.2.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 04 2020 Mat Booth <mat.booth@redhat.com> - 3.1.0-1
- Update to latest upstream version
- Obsolete sub-packages that cannot be built on JDK 11

* Tue Jul 28 2020 Mat Booth <mat.booth@redhat.com> - 2.1.2-10
- Patch for javaparser API changes

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.1.2-8
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jun 26 2020 Roland Grunberg <rgrunber@redhat.com> - 2.1.2-7
- Force Java 8 as we cannot build with Java 11 due to upstream bug.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Mat Booth <mat.booth@redhat.com> - 2.1.2-5
- Skip problematic NonBlockingHashMapTest

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-4
- Disable another failure-prone unreliable test.

* Mon Sep 09 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1.2-3
- Disable failure-prone unreliable test.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Mat Booth <mat.booth@redhat.com> - 2.1.2-1
- Update to latest upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Mat Booth <mat.booth@redhat.com> - 2.0.2-2
- Drop unneeded dep on guava-testlib

* Mon Aug 14 2017 Tomas Repik <trepik@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 gil cattaneo <puntogil@libero.it> 1.2.1-1
- update to 1.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-0.3.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.2.alpha
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 19 2015 gil cattaneo <puntogil@libero.it> 1.1-0.1.alpha
- initial rpm

