Vendor:         Microsoft Corporation
Distribution:   Mariner
%global hgrev 9de14a6f77e2586269e91f770ca7f7b95282945d
%global hgshortrev 9de14a6f77e2

Name:    python-nss
Version: 1.0.1^20210803hg%{hgshortrev}
Release: 6%{?dist}
Summary: Python bindings for Network Security Services (NSS)

License: MPL-2.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:     https://firefox-source-docs.mozilla.org/security/nss/legacy/python_binding_for_nss/index.html

# There is a pypi package, but it does not include docs. hg.mozilla.org is the upstream VCS.
# This is a snapshot of the current hg tip, three commits ahead of PYNSS_RELEASE_1_0_1
Source0: https://hg.mozilla.org/projects/python-nss/archive/%{hgrev}.zip

Patch1: 0001-Remove-the-docs-build-from-setup.py.patch
Patch2: 0002-Remove-the-version-number-from-setup.py.patch
Patch3: 0003-Use-pkgconfig-to-find-nss-and-nspr.patch
Patch4: 0004-Switch-to-setuptools.patch
Patch5: 0005-Convert-the-tests-to-pytest.patch
Patch6: 0006-Add-dynamic-fields-to-pyproject.toml.patch
Patch7: 0007-Separate-C-and-python-sources.patch

BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-packaging
BuildRequires: python3-requests
BuildRequires: python3-wheel
BuildRequires: python3-pkgconfig
BuildRequires: nss-devel

# Needed for tests
BuildRequires: nss-tools

%global _description %{expand:
This package provides Python bindings for Network Security Services
(NSS) and the Netscape Portable Runtime (NSPR).

NSS is a set of libraries supporting security-enabled client and
server applications. Applications built with NSS can support SSL v2
and v3, TLS, PKCS #5, PKCS #7, PKCS #11, PKCS #12, S/MIME, X.509 v3
certificates, and other security standards. Specific NSS
implementations have been FIPS-140 certified.}

%description %_description

%package -n python3-nss
Summary: %{summary}

%description -n python3-nss %_description

%prep
%autosetup -n python-nss-%{hgrev} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nss

%check
%tox

%files -n python3-nss -f %{pyproject_files}
%doc README

%changelog
* Wed Jan  4 2023 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2-6
- Correct the license files

* Tue Jan  3 2023 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2-5
- Fix ChangeLog in the MANIFEST file
- Remove the .c and .h files from the python module
- Remove the sphinx docs

* Tue Jan  3 2023 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2-4
- Use the tox docs environment for buildrequires
- Remove an unnecessary mkdir

* Tue Jan  3 2023 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2-3
- Fix the license to indicate the correct tri-license
- Allow sphinx 5 for the docs
- Use the deps from the docs extra for the sphinx requirement

* Tue Jan  3 2023 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2-2
- Update the license to use an SPDX identifier
- Remove the sphinx .buildinfo file

* Fri Sep 30 2022 David Shea <reallylongword@gmail.com> - 1.0.1^20210803hg9de14a6f77e2
- Restore the python-nss package
- Start from the upstream hg tip
- Modernize the build process to use a PEP517/518 style build
- Modernize the spec file
