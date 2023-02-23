Vendor:         Microsoft Corporation
Distribution:   Mariner
Name:           xmvn-connector-ivy
Version:        4.0.0~20210707.d300ce6
Release:        3%{?dist}
Summary:        XMvn Connector for Apache Ivy
License:        ASL 2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch

#Source0:        https://github.com/fedora-java/xmvn-connector-ivy/releases/download/%{version}/xmvn-%{version}.tar.xz
Source0:        https://github.com/fedora-java/xmvn-connector-ivy/archive/d300ce6.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

%description
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n xmvn-connector-ivy-d300ce697fda33135c1a60b6606e28e3bca0dec6

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~20210707.d300ce6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0~20210707.d300ce6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 07 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 4.0.0~20210707.d300ce6-1
- Initial packaging

