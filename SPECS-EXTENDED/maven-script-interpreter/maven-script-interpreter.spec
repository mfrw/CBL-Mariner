Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with     groovy

Name:           maven-script-interpreter
Version:        1.2
Release:        11%{?dist}
Summary:        Maven Script Interpreter
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-script-interpreter/
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.beanshell:bsh)
%if %{with groovy}
BuildRequires:  mvn(org.codehaus.groovy:groovy)
%endif
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)


%description
This component provides some utilities to interpret/execute some scripts for
various implementations: Groovy or BeanShell.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q

%if %{without groovy}
%pom_remove_dep :groovy
rm src/main/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreter.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/GroovyScriptInterpreterTest.java
rm src/test/java/org/apache/maven/shared/scriptinterpreter/ScriptRunnerTest.java
sed -i /GroovyScriptInterpreter/d src/main/java/org/apache/maven/shared/scriptinterpreter/ScriptRunner.java
%endif

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.2-11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-6
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Fabio Valentini <decathorpe@gmail.com> - 1.2-3
- Disable groovy support by default.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Add missig build-dependency on maven-shared-utils

* Tue Oct 30 2018 Marian Koncek <mkoncek@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.1-9
- Add groovy conditional

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-5
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1-3
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 02 2013 Michal Srb <msrb@redhat.com> - 1.1-2
- Fix BR

* Mon Sep 02 2013 Michal Srb <msrb@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Mon Aug 05 2013 Michal Srb <msrb@redhat.com> - 1.0-5
- Adapt to current guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jul 24 2012 Tomas Radej <tradej@redhat.com> - 1.0-1
- Initial version

