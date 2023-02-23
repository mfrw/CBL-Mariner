Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           jaxb-api
Version:        2.3.3
Release:        6%{?dist}
Summary:        Jakarta XML Binding API
License:        BSD

URL:            https://github.com/eclipse-ee4j/jaxb-api
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

# package renamed from glassfish-jaxb-api in fedora 33
Provides:       glassfish-jaxb-api = %{version}-%{release}
Obsoletes:      glassfish-jaxb-api < 2.3.3-2

# javadoc subpackage is currently not built
Obsoletes:      glassfish-jaxb-api-javadoc < 2.3.3-2

%description
The Jakarta XML Binding provides an API and tools that automate the mapping
between XML documents and Java objects.

%prep
%setup -q

# remove unnecessary dependency on parent POM
%pom_remove_parent

# disable unwanted test module
%pom_disable_module jaxb-api-test

# remove unnecessary maven plugins
%pom_remove_plugin -r :glassfish-copyright-maven-plugin
%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# mark dependency on jakarta.activation as optional
%pom_xpath_inject "pom:dependency[pom:groupId='jakarta.activation']" "<optional>true</optional>" jaxb-api

# add compatibility aliases for old artifact coordinates
%mvn_alias jakarta.xml.bind:jakarta.xml.bind-api javax.xml.bind:jaxb-api
%mvn_file :jakarta.xml.bind-api glassfish-jaxb-api/jakarta.xml.bind-api jaxb-api


%build
# skip javadoc build due to https://github.com/fedora-java/xmvn/issues/58
%mvn_build -j -- -DbuildNumber=unknown -DscmBranch=%{version}


%install
%mvn_install


%files -f .mfiles
%license LICENSE.md NOTICE.md


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.3-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.3-2
- Initial package renamed from glassfish-jaxb-api.

