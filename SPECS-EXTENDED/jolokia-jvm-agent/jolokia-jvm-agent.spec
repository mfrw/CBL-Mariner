Vendor:         Microsoft Corporation
Distribution:   Mariner
%global base_name jolokia

# Filter requires for the Java Agent as deps are bundled within.
%global tools_or_json_simple com\\.googlecode\\.json-simple:json-simple.*|com\\.sun:tools.*
%global mvn_requires_filter .*mvn\\(%{tools_or_json_simple}\\)
%global __requires_exclude ^%{mvn_requires_filter}$

Name:          jolokia-jvm-agent
Version:       1.6.2
Release:       10%{?dist}
Summary:       Jolokia JVM Agent

License:       ASL 2.0
URL:           https://jolokia.org

Source0:       https://github.com/rhuss/jolokia/releases/download/v%{version}/%{base_name}-%{version}-source.tar.gz
# See https://github.com/rhuss/jolokia/pull/413, namespace json simple
# so as to reduce problems related to classloading for apps using json_simple
# See also: https://github.com/rhuss/jolokia/issues/398
Patch1:        0001-Shade-json-simple-for-JVM-agent-jar.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(com.googlecode.json-simple:json-simple)
# jolokia core depends on the servlet API
BuildRequires: mvn(javax.servlet:servlet-api)

Provides:      bundled(com.googlecode.json-simple:json-simple) = 1.1.1

%description
Jolokia JVM Agent.

%prep
%setup -q -n %{base_name}-%{version}
%patch1 -p1
# Only build the jolokia-jvm artefact.
%pom_disable_module it
%pom_disable_module client
%pom_disable_module tools/test-util
%pom_disable_module war agent
%pom_disable_module war-unsecured agent
%pom_disable_module jsr160 agent
%pom_disable_module osgi agent
%pom_disable_module osgi-bundle agent
%pom_disable_module jmx agent
%pom_disable_module jvm-spring agent
%pom_disable_module mule agent

%pom_xpath_remove pom:project/pom:build/pom:extensions pom.xml
%pom_xpath_remove pom:project/pom:reporting pom.xml

# Change compiler source/target version to JDK 8 level
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" agent/jvm/pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" agent/jvm/pom.xml

# Remove scope=system for com.sun:tools
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" agent/jvm
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" agent/jvm

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc NOTICE

%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.6.2-10
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1.6.2-8
- Source/target Java compiler level bump for agent/jvm/pom.xml as well.

* Tue Dec 14 2021 Severin Gehwolf <sgehwolf@redhat.com> - 1.6.2-7
- Bump source/target Java compiler level to JDK 8 for JDK 17 compatibility.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1.6.2-2
- Properly name-space bundled json_simple.
  See upstream: https://github.com/rhuss/jolokia/issues/398

* Mon Aug 12 2019 Severin Gehwolf <sgehwolf@redhat.com> - 1.6.2-1
- Initial package.

