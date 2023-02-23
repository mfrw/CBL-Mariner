Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           spec-version-maven-plugin
Version:        1.5
Release:        6%{?dist}
Summary:        Spec Version Maven Plugin
License:        CDDL or GPLv2 with exceptions

# project moved to eclipse-ee4j for versions > 1.5
# https://github.com/eclipse-ee4j/glassfish-spec-version-maven-plugin
URL:            https://github.com/javaee/spec-version-maven-plugin
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Maven Plugin to configure APIs version and specs in a MANIFEST.MF file.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.


%prep
%autosetup

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

# Build for JDK 1.8 instead of 1.6
sed -i 's/1\.6/1.8/g' pom.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file :%{name} %{name}


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.5-6
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov  6 2021 Jerry James <loganjerry@gmail.com> - 1.5-4
- Build for JDK 1.8 to fix FTBFS

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.5-1
- Update to version 1.5.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.2-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 gil cattaneo <puntogil@libero.it> 1.2-6
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 02 2013 gil cattaneo <puntogil@libero.it> 1.2-2
- build with XMvn
- minor changes to adapt to current guideline

* Wed May 22 2013 gil cattaneo <puntogil@libero.it> 1.2-1
- initial rpm

