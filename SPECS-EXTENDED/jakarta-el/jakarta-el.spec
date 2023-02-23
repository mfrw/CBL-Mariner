Vendor:         Microsoft Corporation
Distribution:   Mariner
%global srcname el-ri

Name:           jakarta-el
Version:        4.0.0
Release:        7%{?dist}
Summary:        Jakarta Expression Language
License:        EPL-2.0 or GPLv2 with exceptions

URL:            https://github.com/eclipse-ee4j/el-ri
Source0:        %{url}/archive/%{version}-RELEASE/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit47)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-el = %{version}-%{release}
Obsoletes:      glassfish-el < 3.0.1-1

%description
Jakarta Expression Language provides a specification document, API,
reference implementation and TCK that describes an expression language
for Java applications.

This package contains the implementation.


%package api
Summary:        Jakarta Expression Language API

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-el-api = %{version}-%{release}
Obsoletes:      glassfish-el-api < 3.0.1-1

%description api
Jakarta Expression Language provides a specification document, API,
reference implementation and TCK that describes an expression language
for Java applications.

This package contains only the API.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-el-javadoc = %{version}-%{release}
Obsoletes:      glassfish-el-javadoc < 3.0.1-1

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{srcname}-%{version}-RELEASE

# remove unnecessary dependency on parent POM
%pom_remove_parent . api impl

# do not build specification documentation
%pom_disable_module spec

# provide javax.el packages in addition to jakarta.el to ease transition
cp -pr api/src/main/java/jakarta api/src/main/java/javax
sed -i -e 's/jakarta\./javax./g' $(find api/src/main/java/javax -name *.java)
%pom_xpath_replace pom:instructions/pom:Export-Package \
  '<Export-Package>jakarta.el,javax.el;version="3.0.0"</Export-Package>' api

# do not install useless parent POM
%mvn_package jakarta.el:el-parent __noinstall

# remove maven plugins unnecessary for RPM builds
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# add maven artifact coordinate aliases for backwards compatibility
%mvn_alias org.glassfish:jakarta.el org.glassfish:javax.el
%mvn_alias jakarta.el:jakarta.el-api javax.el:javax.el-api javax.el:el-api

# add compat symlinks for packages constructing the classpath manually
%mvn_file :jakarta.el     %{name}/jakarta.el     glassfish-el
%mvn_file :jakarta.el-api %{name}/jakarta.el-api glassfish-el-api


%build
%mvn_build -s


%install
%mvn_install


%files -f .mfiles-jakarta.el
%license LICENSE.md NOTICE.md
%doc README.md

%files api -f .mfiles-jakarta.el-api
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.0.0-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Aug 22 2021 Mat Booth <mat.booth.wg@bp.renesas.com> - 4.0.0-5
- Fix BRs for FTBFS bug

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 31 2020 Fabio Valentini <decathorpe@gmail.com> - 4.0.0-2
- Add a missing maven artifact coordinate alias.

* Thu Aug 13 2020 Fabio Valentini <decathorpe@gmail.com> - 4.0.0-1
- Initial package renamed from glassfish-el.

