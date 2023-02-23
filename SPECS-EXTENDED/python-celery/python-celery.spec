Vendor:         Microsoft Corporation
Distribution:   Mariner
%bcond_without tests
# Packaging unstable?
# %%global prerel rc2
%global general_version 5.2.6
%global upstream_version %{general_version}%{?prerel}

Name:           python-celery
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
BuildArch:      noarch

License:        BSD
URL:            https://docs.celeryq.dev/
Source0:        https://github.com/celery/celery/archive/v%{upstream_version}/%{name}-%{upstream_version}.tar.gz
# Fix custom pytest markers for pytest
Source1:        pytest.ini
Summary:        Distributed Task Queue

%description
An open source asynchronous task queue/job queue based on
distributed message passing. It is focused on real-time
operation, but supports scheduling as well.

The execution units, called tasks, are executed concurrently
on one or more worker nodes using multiprocessing, Eventlet
or gevent. Tasks can execute asynchronously (in the background)
or synchronously (wait until ready).

Celery is used in production systems to process millions of
tasks a day.

Celery is written in Python, but the protocol can be implemented
in any language. It can also operate with other languages using
web hooks.

The recommended message broker is RabbitMQ, but limited support
for Redis, Beanstalk, MongoDB, CouchDB and databases
(using SQLAlchemy or the Django ORM) is also available.

%package doc
Summary: Documentation for python-celery
License: CC-BY-SA

%description doc
Documentation for python-celery.

%package -n python3-celery
Summary:        Distributed Task Queue

# Requires are auto-generated from setup.py (and then from requirements/default.txt)

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with tests}
BuildRequires:  python3-amqp
BuildRequires:  python3-billiard
BuildRequires:  python3-case
BuildRequires:  python3-cryptography
BuildRequires:  python3-click
BuildRequires:  python3-dns
BuildRequires:  python3-dateutil
BuildRequires:  python3-future
BuildRequires:  python3-kombu
BuildRequires:  python3-msgpack
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-pytest-subtests
BuildRequires:  python3-pytz
BuildRequires:  python3-pyyaml
BuildRequires:  python3-redis
BuildRequires:  python3-simplejson
%endif

%description -n python3-celery
%{desc}

%prep
%autosetup -p1 -n celery-%{upstream_version}

# there is no reason to limit click in a such aggresive way
sed -i 's/click>=8.0.3,<9.0/click/g' requirements/default.txt

%build
%py3_build

#pushd docs
# missing python-sphinx_celery (for the moment)
#make %{?_smp_mflags} html
#popd

# fix custom celery markers in pytest
cp %{SOURCE1} .

%install
%py3_install
pushd %{buildroot}%{_bindir}
mv celery celery-%{python3_version}
ln -s celery-%{python3_version} celery-3
ln -s celery-3 celery
popd

%check
# python-moto is not packaged in Fedora, ignore S3 tests
# mongodb is not packaged in Fedora, ignore mongodb tests
%if %{with tests}
# cache tests
export TEST_BROKER=redis://
export TEST_BACKEND=cache+pylibmc://
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py

# redis tests
export TEST_BROKER=redis://
export TEST_BACKEND=redis://
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py

# rabbitmq tests
export TEST_BROKER=pyamqp://
export TEST_BACKEND=rpc
%pytest --ignore=t/unit/backends/test_s3.py --ignore=t/unit/backends/test_mongodb.py --ignore=t/distro/test_CI_reqs.py
%endif

%files doc
%license LICENSE

%files -n python3-celery
%license LICENSE
%doc README.rst TODO CONTRIBUTORS.txt examples
%{_bindir}/celery
%{_bindir}/celery-3*
%{python3_sitelib}/celery-*.egg-info
%{python3_sitelib}/celery

%changelog
* Sat Apr 09 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.6-1
- Celery 5.2.6

* Sun Apr 03 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.5-1
- Celery 5.2.5

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.3-2
- Lighten up some dependency ranges a bit

* Thu Jan 06 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.3-1
- Celery 5.2.3

* Mon Nov 22 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.1-1
- Celery 5.2.1

* Wed Nov 10 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.0-1
- Celery 5.2.0

* Wed Nov 03 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.0~rc2-1
- Celery 5.2.0rc2

* Thu Oct 14 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.2.0~rc1-1
- Celery 5.2.0rc1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.2-1
- Celery 5.1.2

* Wed Jun 30 2021 Miro Hrončok <mhroncok@redhat.com> - 5.1.1-2
- Work with click 8
- Fixes rhbz#1977508

* Wed Jun 23 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.1-1
- Celery 5.1.1

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.1.0-2
- Rebuilt for Python 3.10

* Tue May 25 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.1.0-1
- Celery 5.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.5-1
- Celery 5.0.5

* Tue Dec 08 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.4-1
- Celery 5.0.4
- Remove requires from spec, let generators do their job :)

* Sun Dec 06 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.3-1
- Celery 5.0.3

* Tue Nov 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.2-1
- Celery 5.0.2

* Mon Oct 19 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.1-1
- Celery 5.0.1

* Wed Sep 30 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.0-2
- Enable more tests

* Tue Sep 29 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 5.0.0-1
- Celery 5.0.0

* Mon Aug 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.4.7-1
- Celery 4.4.7

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.4.6-1
- Celery 4.4.6

* Mon Jun 08 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.4.5-1
- Celery 4.4.5

* Mon Jun 01 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.4.4-1
- Celery 4.4.4

* Mon Jun 01 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 4.4.3-1
- Celery 4.4.3
- Run pytest during rpm build

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nils Philippsen <nils@redhat.com> - 4.3.0-1
- Update to 4.3.0

* Thu Jun 06 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.2.1-5
- Drop python2-celery, as nothing was using it and it fails to install (#1716370).

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Neal Gompa <ngompa13@gmail.com> - 4.2.1-3
- Drop old, unused dependencies from Python 2 subpackage

* Mon Jan 28 2019 Neal Gompa <ngompa13@gmail.com> - 4.2.1-2
- Switch celery binary to Python 3 in F30+
- Switch to bconds for controlling the build
- Drop unused macro

* Wed Sep 19 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1 (#1602746).
- https://github.com/celery/celery/blob/v4.2.1/Changelog
- Correct documentation license to CC-BY-SA.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Matthias Runge <mrunge@redhat.com> - 4.2.0-2
- rebuild for python 3.7

* Mon Jun 25 2018 Carl George <carl@george.computer> - 4.2.0-1
- Latest upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.1-2
- Rebuilt for Python 3.7

* Tue May 22 2018 Matthias Runge <mrunge@redhat.com> - 4.1.1-1
- update to 4.1.1 (rhbz#1474545)

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.0.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
