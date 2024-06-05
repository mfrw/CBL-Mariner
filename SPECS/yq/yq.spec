Summary:        Process YAML documents from the CLI
Name:           yq
Version:        4.44.1
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Tools/Container
URL:            https://github.com/mikefarah/yq
Source0:        https://github.com/mikefarah/yq/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-%{version}-vendor.tar.gz
BuildRequires:  golang

%description 
yq is a portable command-line YAML, JSON, XML, CSV, TOML and properties processor


%prep
%autosetup -a1

%build
go build

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} yq

%files
%{_bindir}/yq

%changelog
* Wed Jun 05 2024 Muhammad Falak <mwani@microsoft.com> - 4.44.1-1
- Original version for CBL-Mariner
- License Verified
