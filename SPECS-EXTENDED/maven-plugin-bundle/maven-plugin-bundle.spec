Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-plugin-bundle
Version:        5.1.1
Release:        5%{?dist}
Summary:        Maven Bundle Plugin
License:        ASL 2.0
URL:            https://felix.apache.org
BuildArch:      noarch

Source0:        https://repo1.maven.org/maven2/org/apache/felix/maven-bundle-plugin/%{version}/maven-bundle-plugin-%{version}-source-release.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.utils)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
%endif

%description
Provides a maven plugin that supports creating an OSGi bundle
from the contents of the compilation classpath along with its
resources and dependencies. Plus a zillion other features.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n maven-bundle-plugin-%{version}

find -name '*.jar' -delete

# There is forked version of maven-osgi in
# src/{main,test}/java/org/apache/maven

rm -rf src/main/java/org/apache/felix/obrplugin/
%pom_remove_dep :org.apache.felix.bundlerepository

rm -f src/main/java/org/apache/felix/bundleplugin/baseline/BaselineReport.java
%pom_remove_dep :doxia-sink-api
%pom_remove_dep :doxia-site-renderer
%pom_remove_dep :maven-reporting-api

%pom_remove_dep :org.osgi.core
%pom_remove_dep :jdom

%pom_remove_plugin :maven-invoker-plugin

%build
# Tests depend on bundled JARs
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.1.1-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 5.1.1-2
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Marian Koncek <mkoncek@redhat.com> - 5.1.1-1
- Update to upstream version 5.1.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.2.1-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat May 16 2020 Fabio Valentini <decathorpe@gmail.com> - 4.2.1-1
- Update to version 4.2.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.2.1-2
- Mass rebuild for javapackages-tools 201902

* Mon Aug 19 2019 Marian Koncek <mkoncek@redhat.com> - 4.2.1-1
- Update to upstream version 4.2.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Marian Koncek <mkoncek@redhat.com> - 4.2.0-1
- Update to upstream version 4.2.0

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.0-3
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov  5 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.5.1-1
- Remove unneeded BR on doxia-core

* Thu Nov 01 2018 Marian Koncek <mkoncek@redhat.com> - 3.5.1-1
- Update to upstream version 3.5.1

* Thu Aug 02 2018 Michael Simacek <msimacek@redhat.com> - 3.5.0-4
- Remove spurious %%if fedora
- Use license macro

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Michael Simacek <msimacek@redhat.com> - 3.5.0-1
- Update to upstream version 3.5.0

* Tue Jan 02 2018 Michael Simacek <msimacek@redhat.com> - 3.4.0-1
- Update to upstream version 3.4.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 3.3.0-1
- Update to upstream version 3.3.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2.0-3
- Add conditionals for building without OBR or Maven reports

* Thu Oct 06 2016 Michael Simacek <msimacek@redhat.com> - 3.2.0-2
- Use osgi APIs instead of felix-framework

* Tue Jul 19 2016 Michael Simacek <msimacek@redhat.com> - 3.2.0-1
- Update to upstream version 3.2.0

* Thu May 26 2016 Michael Simacek <msimacek@redhat.com> - 3.0.1-4
- Remove aqute downgrade patch

* Thu May 12 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.1-3
- Port to plexus-utils 3.0.24

* Thu Apr 14 2016 Mat Booth <mat.booth@redhat.com> - 3.0.1-2
- Fix build against new maven-archiver, which removed some deprecated methods
  that this plugin was using

* Fri Feb 12 2016 Michael Simacek <msimacek@redhat.com> - 3.0.1-1
- Update to upstream version 3.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Michael Simacek <msimacek@redhat.com> - 2.5.4-1
- Update to upstream version 2.5.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-14
- Add build-requires on mockito

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-12
- Update to current packaging guidelines

* Thu Feb 20 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-11
- Remove unneeded R and BR: maven-wagon

* Fri Jul 26 2013 Tomas Radej <tradej@redhat.com> - 2.3.7-10
- Fixed release number

* Wed Jul 17 2013 Tomas Radej <tradej@redhat.com> - 2.3.7-9
- Updated source address (error 404)

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-8
- Add missing BR: maven-plugin-testing-harness

* Mon Mar 11 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-7
- Re-enable tests

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3.7-3
- Add kxml2 to pom as a dependency

* Mon Apr 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.7-2
- Add missing BuildRequires

* Wed Feb 29 2012 Jaromir Capik <jcapik@redhat.com> 2.3.7-1
- Update to 2.3.7

* Thu Jan 19 2012 Jaromir Capik <jcapik@redhat.com> 2.3.6-3
- Bundled maven sources readded (they seem to change the behaviour)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Jaromir Capik <jcapik@redhat.com> 2.3.6-1
- Update to 2.3.6

* Mon Dec 19 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-3
- Minimal aqute-bndlib VR set to 1.43.0-2 (older ones are broken)

* Mon Nov 14 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-2
- OBR plugin readded (it's been merged to the bundle plugin)

* Mon Oct 24 2011 Jaromir Capik <jcapik@redhat.com> 2.3.5-1
- Update to 2.3.5

* Tue Oct 17 2011 Jaromir Capik <jcapik@redhat.com> 2.0.0-11
- aqute-bndlib renamed to aqute-bnd

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-10
- Do not depend on maven2.

* Thu Feb 10 2011 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-9
- BR maven-surefire-provider-junit4.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-7
- BR/R felix-parent.

* Thu Sep 9 2010 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-5
- Fix BuildRequires.

* Fri Sep 18 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-4
- Add missing Requires.

* Wed Sep 9 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-3
- BR doxia-sitetools.

* Mon Sep 7 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-2
- Fix BR/Rs.

* Thu Sep 3 2009 Alexander Kurtakov <akurtako@redhat.com> 2.0.0-1
- Initial import.
