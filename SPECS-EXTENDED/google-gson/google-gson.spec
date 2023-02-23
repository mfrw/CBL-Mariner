Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           google-gson
Version:        2.9.1
Release:        1%{?dist}
Summary:        Java lib for conversion of Java objects into JSON representation
License:        ASL 2.0
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz

# Internal packages are naughtily used by other packages in Fedora
Patch1: 0002-Also-export-internal-packages-in-OSGi-metadata.patch
# Remove dependency on unavailable templating-maven-plugin
# Reverts upstream commit https://github.com/google/gson/commit/d84e26d
Patch3: 0004-This-commit-added-a-dependency-on-templating-maven-p.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  bnd-maven-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n gson-gson-parent-%{version}
#rm ./gradle/wrapper/gradle-wrapper.jar
%patch1 -p1
%patch3 -p1

# The test EnumWithObfuscatedTest requires the plugins copy-rename-maven-plugin, proguard-maven-plugin and maven-resources-plugin to work correctly because it tests Gson interaction with a class obfuscated by ProGuard.
# https://github.com/google/gson/issues/2045
rm ./gson/src/test/java/com/google/gson/functional/EnumWithObfuscatedTest.java

# to check later
rm ./gson/src/test/java/com/google/gson/internal/bind/DefaultDateTypeAdapterTest.java
# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :copy-rename-maven-plugin gson
%pom_remove_plugin :proguard-maven-plugin gson

%pom_remove_plugin  :moditect-maven-plugin gson

# Remove dependency on unavailable templating-maven-plugin
%pom_remove_plugin  org.codehaus.mojo:templating-maven-plugin gson
rm gson/src/test/java/com/google/gson/internal/GsonBuildConfigTest.java
rm gson/src/test/java/com/google/gson/functional/GsonVersionDiagnosticsTest.java

# to fix error: package javax.annotation is not visible import javax.annotation.PostConstruct;
rm extras/src/main/java/com/google/gson/typeadapters/PostConstructAdapterFactory.java
rm extras/src/test/java/com/google/gson/typeadapters/PostConstructAdapterFactoryTest.java

#depends on com.google.caliper
%pom_disable_module metrics

#depends on com.google.protobuf:protobuf-java:jar:4.0.0-rc-2 and com.google.truth:truth:jar:1.1.3
%pom_disable_module proto

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%files javadoc  -f .mfiles-javadoc
%license LICENSE

%changelog
* Sat Aug 27 2022 Sérgio Basto <sergio@serjux.com> - 2.9.1-1
- Update google-gson to 2.9.1 (#2112775)
- Refactor patch 0004 , to not use patch to delete files and add a new hunk
- Reenable javadoc sub-package

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.9.0-2
- Rebuilt for Drop i686 JDKs

* Wed Mar 02 2022 Sérgio Basto <sergio@serjux.com> - 2.9.0-1
- Update google-gson to 2.9.0
- javadoc is disabled because it fails to build

* Sun Feb 06 2022 Sérgio Basto <sergio@serjux.com> - 2.8.8-5
- re-add 0002-Also-export-internal-packages-in-OSGi-metadata.patch and pom_xpath_inject

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.8.8-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 02 2022 Sérgio Basto <sergio@serjux.com> - 2.8.8-2
- Clean up and try to fix build on eln114

* Fri Dec 31 2021 Sérgio Basto <sergio@serjux.com> - 2.8.8-1
- Update google-gson to 2.8.8 (#1964408)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 27 2020 Mat Booth <mat.booth@redhat.com> - 2.8.6-7
- Add patch to prevent hard OSGi dep on 'sun.misc' package
- Fix bogus date in changelog

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.8.6-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Sat Jun 06 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-4
- fixed javadoc to build on jdk11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.6-2
- Remove unnecessary dependency on parent POM.

* Fri Nov 01 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.6-1
- Update to version 2.8.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 21 2018 Alexander Kurtakov <akurtako@redhat.com> 2.8.2-1
- Update to upstream 2.8.2 release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Mat Booth <mat.booth@redhat.com> - 2.8.1-2
- Also export internal packages in OSGi metadata

* Fri Aug 25 2017 Mat Booth <mat.booth@redhat.com> - 2.8.1-1
- Update to latest upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.1-6
- Remove unneeded maven-javadoc-plugin invocation

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Michael Simacek <msimacek@redhat.com> - 2.3.1-4
- Skip default jar plugin execution to fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Michael Simacek <msimacek@redhat.com> - 2.3.1-1
- Update to upstream version 2.3.1

* Mon Apr 20 2015 Michael Simacek <msimacek@redhat.com> - 2.2.4-8
- Remove test that relies on networking

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 2.2.4-7
- Remove dependency on cobertura

* Tue Jun 10 2014 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.4-6
- Move to xmvn style packaging.
- Fix FTBFS. Resolves RHBZ#1106707.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.4-4
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-3
- Add BR maven-install-plugin, resolves RHBZ#992422.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Alexander Kurtakov <akurtako@redhat.com> 2.2.4-1
- Update to newer upstream release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Dec 19 2012 Severin Gehwolf <sgehwolf@redhat.com> 2.2.2-2
- Add BR for surefire junit provider.

* Wed Dec 19 2012 Severin Gehwolf <sgehwolf@redhat.com> 2.2.2-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-2
- Add missing BR on maven-enforcer-plugin.
- Remove no longer needed parts of the spec.

* Mon Jul 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.2.1-1
- Update to latest upstream 2.2.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-3
- Removal of failing testInetAddressSerializationAndDeserialization

* Wed May 11 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-2
- Conversion of CR+LF to LF in the license file

* Tue May 10 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-1
- Initial version of the package
