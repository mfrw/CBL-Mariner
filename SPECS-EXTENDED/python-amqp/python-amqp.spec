Vendor:         Microsoft Corporation
Distribution:   Mariner
# Tests can optionally be disabled
%bcond_without tests

# These Sphinx docs do not build without sphinx_celery packaged
%bcond_with sphinx_docs

%global srcname amqp

Name:           python-%{srcname}
Version:        5.1.1
Release:        1%{?dist}
Summary:        Low-level AMQP client for Python (fork of amqplib)

License:        BSD
URL:            http://pypi.python.org/pypi/amqp
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if %{with sphinx_docs}
BuildRequires:  python3-sphinx
%endif

%description
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.


%package -n python3-%{srcname}
Summary:        Client library for AMQP
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-vine >= 5.0.0
%endif
%if %{with sphinx_docs}
BuildRequires:  python3-sphinx >= 0.8
%endif
%{?python_provide:%python_provide python3-%{srcname}}
Requires:    python3-vine >= 5.0.0

%description -n python3-%{srcname}
Low-level AMQP client for Python

This is a fork of amqplib, maintained by the Celery project.

This library should be API compatible with librabbitmq.


%package doc
Summary:        Documentation for python-amqp
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for python-amqp


%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with sphinx_docs}
# docs generation requires everything to be installed first
export PYTHONPATH="$( pwd ):$PYTHONPATH"

pushd docs

# Disable extensions to prevent intersphinx from accessing net during build.
# Other extensions listed are not used.
sed -i s/^extensions/disable_extensions/ conf.py

SPHINX_DEBUG=1 sphinx-build -b html . build/html
rm -rf build/html/.doctrees build/html/.buildinfo

popd
%endif

%check
%if %{with tests}
py.test-3 t/unit
%endif

%files -n python3-%{srcname}
%doc Changelog README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%if %{with sphinx_docs}
%doc docs/build/html docs/reference
%endif


%changelog
* Sun May 08 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.1-1
- python-amqp 5.1.1

* Fri Mar 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.0-1
- python-amqp 5.1.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.9-1
- python-amqp 5.0.9

* Mon Dec 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.8-1
- python-amqp 5.0.8

* Wed Dec 15 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.7-1
- python-amqp 5.0.7
- drop Python 2 subpackage/clean spec
- drop dependency on python-case
- drop dependency on python-nose and python-nose (cstratak)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.0.6-2
- Rebuilt for Python 3.10

* Tue Apr 20 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.6-1
- python-amqp 5.0.6

* Thu Jan 28 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.5-1
- python-amqp 5.0.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.3-1
- python-amqp 5.0.3

* Sun Nov 08 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.2-1
- python-amqp 5.0.2

* Tue Sep 29 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.1-1
- python-amqp 5.0.1

* Mon Aug 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.6.1-1
- python-amqp 2.6.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.6.0-1
- python-amqp 2.6.0

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Yatin Karel <ykarel@redhat.com> - 2.5.2-2
- Fix build for rhel < 8

* Tue Nov 12 2019 Eric Harney <eharney@redhat.com> - 2.5.2-1
- Update to 2.5.2

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 25 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.1-1
- Update to 2.5.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Eric Harney <eharney@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Thu Mar 21 2019 Eric Harney <eharney@redhat.com> - 2.4.2-1
- Update to 2.4.2

* Mon Feb 04 2019 Eric Harney <eharney@redhat.com> - 2.4.1-1
- Update to 2.4.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Neal Gompa <ngompa13@gmail.com> - 2.4.0-1
- Update to 2.4.0
- Fix license tag to match actual source license
- Use bconds for controlling build behavior
- Make compatible with EPEL7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-2
- Rebuilt for Python 3.7

* Thu May 31 2018 Eric Harney <eharney@redhat.com> - 2.3.2-1
- Update to 2.3.2

* Tue May 29 2018 Eric Harney <eharney@redhat.com> - 2.3.1-1
- Update to 2.3.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Eric Harney <eharney@redhat.com> - 2.2.2-2
- Enable py3 build for el8

* Tue Oct 24 2017 Eric Harney <eharney@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 14 2017 Eric Harney <eharney@redhat.com> - 2.2.1-2
- Enable unit tests

* Fri Jul 14 2017 Eric Harney <eharney@redhat.com> - 2.2.1-1
- Update to 2.2.1

* Thu Jul 13 2017 Eric Harney <eharney@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Wed Feb 08 2017 Matthias Runge <mrunge@redhat.com> - 2.1.4-1
- upgrade to 2.1.4 (rhbz#1340298)
- modernize spec, add provides (rhbz#1399248)

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Eric Harney <eharney@redhat.com> - 1.4.9-1
- Update to 1.4.9

* Thu Jan 07 2016 Eric Harney <eharney@redhat.com> - 1.4.8-1
- Update to 1.4.8

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov 11 2015 Eric Harney <eharney@redhat.com> - 1.4.7-1
- Update to 1.4.7

* Wed Nov 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 06 2014 Eric Harney <eharney@redhat.com> - 1.4.6-1
- Update to 1.4.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 Eric Harney <eharney@redhat.com> - 1.4.5-1
- Update to 1.4.5

* Fri Feb 07 2014 Eric Harney <eharney@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Fri Jan 17 2014 Eric Harney <eharney@redhat.com> - 1.4.1-1
- Update to 1.4.1

* Fri Nov 15 2013 Eric Harney <eharney@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Fri Oct 25 2013 Eric Harney <eharney@redhat.com> - 1.3.1-1
- Update to 1.3.1

* Tue Oct 08 2013 Eric Harney <eharney@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Fri Sep 20 2013 Eric Harney <eharney@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Eric Harney <eharney@redhat.com> - 1.0.11-1
- Initial package
