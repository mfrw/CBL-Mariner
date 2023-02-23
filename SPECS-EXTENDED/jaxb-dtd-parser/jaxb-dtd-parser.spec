Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           jaxb-dtd-parser
Version:        1.5.0
Release:        1%{?dist}
Summary:        SAX-like API for parsing XML DTDs
License:        BSD
URL:            https://github.com/eclipse-ee4j/jaxb-dtd-parser
BuildArch:      noarch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
Provides:       glassfish-dtd-parser = %{version}-%{release}

%description
SAX-like API for parsing XML DTDs.

%package javadoc
Summary:        API documentation for %{name}
%description javadoc
API documentation for %{name}.


%prep
# -S: enable usage of git repo
%autosetup -S git
# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

cd dtd-parser
# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent
# remove unnecessary plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
cd -

%build
cd dtd-parser
%mvn_build
cd -

%install
cd dtd-parser
%mvn_install
cd -

%files -f dtd-parser/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md
%files javadoc -f dtd-parser/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Mon Apr 11 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.5.0-1
- New upstream release 1.5.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.4.5-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.4.5-1
- New upstream release 1.4.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Mat Booth <mat.booth@redhat.com> - 1.4.3-3
- Restore JDK 9+ bits for Jaxb

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Fabio Valentini <decathorpe@gmail.com> - 1.4.3-1
- Initial package renamed from glassfish-dtd-parser.

