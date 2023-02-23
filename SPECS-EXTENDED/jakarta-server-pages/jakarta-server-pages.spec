Vendor:         Microsoft Corporation
Distribution:   Mariner
%global srcname jsp-api

Name:           jakarta-server-pages
Version:        2.3.6
Release:        7%{?dist}
Summary:        Jakarta Server Pages (JSP)
# some files have Apache-2.0 license headers
# https://github.com/eclipse-ee4j/jsp-api/issues/180
License:        (EPL-2.0 or GPLv2 with exceptions) and ASL 2.0

# there's no code changes in jsp-api between 2.3.6 and IMPL-2.3.6 releases,
# so we're using the more recent one
%global upstream_version IMPL-%{version}-RELEASE

URL:            https://github.com/eclipse-ee4j/jsp-api
Source0:        %{url}/archive/%{upstream_version}/%{srcname}-%{upstream_version}.tar.gz

# build with support for JDTJavaCompiler (for eclipse) and AntJavaCompiler
Patch1:         0001-enable-support-for-JDTJavaCompiler-and-AntJavaCompil.patch
# fix compilation errors due to unimplemented interfaces in newer servlet APIs
Patch2:         0002-Port-to-latest-version-of-Servlet-API.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(jakarta.el:jakarta.el-api)
BuildRequires:  mvn(jakarta.servlet:jakarta.servlet-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jdt:core)
BuildRequires:  mvn(org.glassfish:javax.el)

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp = %{version}-%{release}
Obsoletes:      glassfish-jsp < 2.3.4-9

%description
Jakarta Server Pages provides a container-independent implementation of
the JSP API.


%package api
Summary:        Jakarta Server Pages (JSP) API

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp-api = %{version}-%{release}
Obsoletes:      glassfish-jsp-api < 2.3.3-6

%description api
Jakarta Server Pages provides a container-independent implementation of
the JSP API. This package contains the API only.


%package javadoc
Summary:        Javadoc for %{name}

# package renamed in fedora 33, remove in fedora 35
Provides:       glassfish-jsp-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-javadoc < 2.3.4-9
Provides:       glassfish-jsp-api-javadoc = %{version}-%{release}
Obsoletes:      glassfish-jsp-api-javadoc < 2.3.3-6

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -n %{srcname}-%{upstream_version} -p1

# remove unnecessary dependency on parent POM
%pom_remove_parent . api impl

# do not build specification documentation
%pom_disable_module spec

# do not install useless parent POM
%mvn_package org.eclipse.ee4j.jsp:jsp-parent __noinstall

# reset jsp-api version from 2.3.7-SNAPSHOT to 2.3.6 (no code changes)
sed -i "s/2\.3\.7-SNAPSHOT/2.3.6/" api/pom.xml

# ant and ecj should be optional OSGi requirements
%pom_xpath_inject "pom:dependency[pom:groupId='org.apache.ant']" "<optional>true</optional>" impl
%pom_xpath_inject "pom:dependency[pom:groupId='org.eclipse.jdt']" "<optional>true</optional>" impl

# this source file is excluded by maven-compiler-plugin configuration;
# remove it entirely to fix building javadocs
rm impl/src/main/java/org/apache/jasper/runtime/PerThreadTagHandlerPool.java

# add aliases for old maven artifact coordinates
%mvn_alias org.glassfish.web:jakarta.servlet.jsp \
    org.eclipse.jetty.orbit:org.apache.jasper.glassfish \
    org.glassfish.web:javax.servlet.jsp

%mvn_alias jakarta.servlet.jsp:jakarta.servlet.jsp-api \
    javax.servlet.jsp:javax.servlet.jsp-api \
    javax.servlet.jsp:jsp-api \
    javax.servlet:jsp-api

# add compat symlinks for the old classpaths
%mvn_file :jakarta.servlet.jsp     %{name}/jakarta.servlet.jsp     glassfish-jsp     javax.servlet.jsp
%mvn_file :jakarta.servlet.jsp-api %{name}/jakarta.servlet.jsp-api glassfish-jsp-api


%build
%mvn_build -s


%install
%mvn_install


%files -f .mfiles-jakarta.servlet.jsp
%license LICENSE.md NOTICE.md
%doc README.md

%files api -f .mfiles-jakarta.servlet.jsp-api
%license LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md


%changelog
* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.6-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Markku Korkeala <markku.korkeala@iki.fi> - 2.3.6-5
- Add alias for javax.servlet.jsp:jsp-api.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Mat Booth <mat.booth@redhat.com> - 2.3.6-2
- Make the OSGi dep on ant and ecj optional, jsp can be used without these

* Tue Aug 25 2020 Fabio Valentini <decathorpe@gmail.com> - 2.3.6-1
- Initial package produced by merging glassfish-jsp and glassfish-jsp-api.

