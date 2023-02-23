Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:          javaparser
Version:       3.22.0
Release:       3%{?dist}
Summary:       Java 1 to 13 Parser and Abstract Syntax Tree for Java
License:       LGPLv3+ or ASL 2.0
URL:           http://javaparser.org
Source0:       https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(junit:junit)

BuildArch:     noarch

%description
This package contains a Java 1 to 13 Parser with AST generation and
visitor support. The AST records the source code structure, javadoc
and comments. It is also possible to change the AST nodes or create new
ones to modify the source code.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-parent-%{version}

sed -i 's/\r//' readme.md

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :coveralls-maven-plugin

# Compatibility alias
%mvn_alias :javaparser-core com.google.code.javaparser:javaparser

# Fix javacc plugin name
sed -i \
  -e 's/ph-javacc-maven-plugin/javacc-maven-plugin/' \
  -e 's/com.helger.maven/org.codehaus.mojo/' \
  javaparser-core/pom.xml

# This plugin is not in Fedora, so use maven-resources-plugin to accomplish the same thing
%pom_remove_plugin :templating-maven-plugin javaparser-core
%pom_xpath_inject "pom:build" "
<resources>
  <resource>
    <directory>src/main/java-templates</directory>
    <filtering>true</filtering>
    <targetPath>\${basedir}/src/main/java</targetPath>
  </resource>
</resources>" javaparser-core

# Missing dep on jbehave for testing
%pom_disable_module javaparser-core-testing
%pom_disable_module javaparser-core-testing-bdd

# Don't build the symbol solver
%pom_disable_module javaparser-symbol-solver-core
#%pom_disable_module javaparser-symbol-solver-logic
#%pom_disable_module javaparser-symbol-solver-model
%pom_disable_module javaparser-symbol-solver-testing

# Only need to ship the core module
%pom_disable_module javaparser-core-generators
%pom_disable_module javaparser-core-metamodel-generator
%pom_disable_module javaparser-core-serialization

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%files javadoc -f .mfiles-javadoc
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.22.0-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Markku Korkeala <markku.korkeala@iki.fi> - 3.22.0-1
- Update to 3.22.0, comment out removed modules, add junit dependency.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Mat Booth <mat.booth@redhat.com> - 3.14.16-1
- Update to 3.14.x to get Java up to 13 support

* Tue Jul 28 2020 Mat Booth <mat.booth@redhat.com> - 3.5.20-1
- Update to 3.5.x to get Java 10 support

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Markku Korkeala <markku.korkeala@iki.fi> - 3.3.5-5
- Add dependency for javax.annotation.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.3.5-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Mat Booth <mat.booth@redhat.com> - 3.3.5-1
- Update to javaparser 3.3.5 for Java 9 support
- Correct license field to dual license: LGPLv3+ OR ASL 2.0

* Wed Feb 13 2019 Mat Booth <mat.booth@redhat.com> - 2.5.1-1
- Update to javaparser 2.5.1 for Java 1.8 support

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jul 31 2015 gil cattaneo <puntogil@libero.it> 1.0.11-1
- update to 1.0.11

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 gil cattaneo <puntogil@libero.it> 1.0.8-9
- fix Url tag

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 1.0.8-8
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0.8-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.0.8-4
- switch to XMvn
- minor changes to adapt to current guideline

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.8-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 26 2012 gil cattaneo <puntogil@libero.it> 1.0.8-1
- initial rpm
