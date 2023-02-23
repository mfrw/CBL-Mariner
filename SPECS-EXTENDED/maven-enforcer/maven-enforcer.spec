Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_with bootstrap

Name:           maven-enforcer
Version:        3.0.0~M3
Release:        8%{?dist}
Summary:        Maven Enforcer
License:        ASL 2.0
URL:            https://maven.apache.org/enforcer
BuildArch:      noarch

%global upstream_version %(echo '%{version}' | tr '~' '-')

Source0:        https://repo1.maven.org/maven2/org/apache/maven/enforcer/enforcer/%{upstream_version}/enforcer-%{upstream_version}-source-release.zip

# TODO forward upstream
# https://issues.apache.org/jira/browse/MENFORCER-267
Patch0:         0001-Port-to-Maven-3-API.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-rules)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
%endif

%description
Enforcer is a build rule execution framework.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%package api
Summary:        Enforcer API

%description api
This component provides the generic interfaces needed to
implement custom rules for the maven-enforcer-plugin.

%package rules
Summary:        Enforcer Rules

%description rules
This component contains the standard Enforcer Rules.

%package plugin
Summary:        Enforcer Rules

%description plugin
This component contains the standard Enforcer Rules.


%prep
%setup -q -n enforcer-%{upstream_version}
find -name '*.java' -exec sed -i 's/\r//' {} +
%patch0 -p1

# Port to maven-artifact-transfer 0.11.0
sed -i 's/shared\.artifact\.resolve/shared.transfer.artifact.resolve/' enforcer-rules/src/main/java/org/apache/maven/plugins/enforcer/utils/EnforcerRuleUtils.java
sed -i 's/shared\.artifact\.resolve/shared.transfer.artifact.resolve/' enforcer-rules/src/main/java/org/apache/maven/plugins/enforcer/RequirePluginVersions.java

%pom_remove_plugin :maven-enforcer-plugin

find -name EvaluateBeanshell.java -delete
%pom_remove_dep :bsh enforcer-rules

# Avoid dependency cycle
%pom_xpath_inject pom:build/pom:pluginManagement/pom:plugins "
    <plugin>
      <artifactId>maven-enforcer-plugin</artifactId>
      <version>SYSTEM</version>
    </plugin>"

# Replace plexus-maven-plugin with plexus-component-metadata
sed -e "s|<artifactId>plexus-maven-plugin</artifactId>|<artifactId>plexus-component-metadata</artifactId>|" \
    -e "s|<goal>descriptor</goal>|<goal>generate-metadata</goal>|" \
    -i enforcer-{api,rules}/pom.xml

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-enforcer
%doc LICENSE NOTICE

%files api -f .mfiles-enforcer-api
%doc LICENSE NOTICE

%files rules -f .mfiles-enforcer-rules

%files plugin -f .mfiles-maven-enforcer-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.0.0~M3-8
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~M3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~M3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0~M3-5
- Bootstrap build
- Non-bootstrap build

* Fri May 14 2021 Marian Koncek <mkoncek@redhat.com> - 3.0.0~M3-1
- Update to upstream version 3.0.0~M3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~M3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~M3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.0.0~M3-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu May 07 2020 Fabio Valentini <decathorpe@gmail.com> - 3.0.0~M3-1
- Update to version 3.0.0-M3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0~M2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.0~M2-2
- Mass rebuild for javapackages-tools 201902

* Sun Nov 03 2019 Fabio Valentini <decathorpe@gmail.com> - 3.0.0~M2-2
- Port to maven-artifact-transfer 0.11.0.

* Thu Aug 08 2019 Marian Koncek <mkoncek@redhat.com> - 3.0.0~M2-1
- Update to upstream verssion 3.0.0~M2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 29 2019 Marian Koncek <mkoncek@redhat.com> - 3.0.0-1
- Update to upstream version 3.0.0~M2

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-9
- Mass rebuild for javapackages-tools 201901

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-7
- Avoid dependency cycle during Maven build

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-3
- Fix Maven 3 patch

* Mon Oct 12 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-2
- Port to Maven 3 API

* Mon Aug 31 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-1
- Update to upstream version 1.4.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-4
- Remove legacy Obsoletes/Provides for maven2 plugin

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-3
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-1
- Update to upstream version 1.3.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-6
- Build with xmvn
- Update to current packaging guidelines

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-5
- Remove BR on maven-doxia
- Resolves: rhbz#915611

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec  6 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-2
- Add mising R: forge-parent

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.1.1-3
- Including LICENSE and NOTICE

* Mon Oct 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-2
- Remove RPM bug workaround

* Fri Oct 12 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-1
- Update to upstream version 1.1.1
- Convert patches to POM macro
- Remove patch for bug 748074, upstreamed

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.1-4
- Migration to plexus-containers-component-metadata
- Maven3 compatibility patches
- Minor spec file changes according to the latest guidelines

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Jaromir Capik <jcapik@redhat.com> - 1.0.1-2
- Removal of plexus-maven-plugin dependency (not needed)

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-1
- Update to latest upstream 1.0.1.
- Adapt to current guidelines.

* Thu Mar 10 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Update to latest upstream (1.0)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.b2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.2.b2
- Fix FTBFS (#631388)
- Use new maven plugin names
- Versionless jars & javadocs

* Wed May 19 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.1.b2
- Initial package
