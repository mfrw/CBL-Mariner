Vendor:         Microsoft Corporation
Distribution:   Mariner
## START: Set by rpmautospec
## (rpmautospec version 0.2.5)
%define autorelease(e:s:pb:) %{?-p:0.}%{lua:
    release_number = 12;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{?dist}
## END: Set by rpmautospec

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-sure
Version:        2.0.0
Release:        %autorelease
Summary:        Idiomatic assertion toolkit with human-friendly failure messages

License:        GPLv3+
URL:            https://github.com/gabrielfalcao/sure
Source0:        %{url}/archive/%{version}/sure-%{version}.tar.gz

# Trivial downstream man page for (nearly pointless) executable
Source1:        sure.1

# Python 3.10 workaround
# In test_context_is_not_optional(), only check the exception type
# https://github.com/gabrielfalcao/sure/issues/169
Patch0:         python3.10-workaround.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# TODO: remove mock dependency from install_requires
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock
# https://github.com/gabrielfalcao/sure/pull/161

# Test dependencies
# development.txt: pytest==6.2.4
BuildRequires:  python3dist(pytest)

# Documentation dependencies
%if %{with doc_pdf}
BuildRequires:  make
# development.txt: Sphinx==2.3.1
BuildRequires:  python3dist(sphinx)
# development.txt: sphinx-rtd-theme==0.4.3
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%global common_description %{expand:
An idiomatic testing library for python with powerful and flexible assertions
created by Gabriel Falcão. Sure’s developer experience is inspired and modeled
after RSpec Expectations and should.js.}

%description %{common_description}


%package -n python3-sure
Summary:        %{summary}

%description -n python3-sure %{common_description}


%package doc
Summary:        Documentation for Sure

%description doc %{common_description}


%prep
%autosetup -p1 -n sure-%{version}

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

cp -p '%{SOURCE1}' .

# Do not generate a coverage report; this obviates the BR on pytest-cov
sed -r -i 's/[[:blank:]]--cov=[^[:blank:]]+//' setup.cfg


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files sure

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 sure.1


%check
# The old_api tests use python3dist(nose), which is deprecated and which we
# have removed from the BuildRequires:
# https://fedoraproject.org/wiki/Changes/DeprecateNose
%pytest --ignore=tests/test_old_api.py


%files -n python3-sure -f %{pyproject_files}
%{_bindir}/sure
%{_mandir}/man1/sure.1*


%files doc
%license COPYING
%doc CHANGELOG.md
%doc README.rst
%doc TODO.rst
%if %{with doc_pdf}
%doc docs/build/latex/Sure.pdf
%endif


%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-11
- Drop intersphinx mappings

* Fri Dec 17 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-10
- Remove build dependencies on nose and pytest-cov

* Thu Nov 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-9
- Reduce LaTeX PDF build verbosity

* Tue Sep 28 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-8
- Build PDF documentation in lieu of HTML

* Mon Sep 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-7
- Reduce macro indirection in the spec file

* Mon Sep 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-6
- Drop BR on pyproject-rpm-macros, now implied by python3-devel

* Mon Sep 13 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-5
- Let pyproject-rpm-macros handle the license file

* Tue Jul 27 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-4
- Move %generate_buildrequires after %prep to make the spec file easier to
  follow

* Wed Jul 21 2021 Benjamin A. Beasley <code@musicinmybrain.net> 2.0.0-3
- Remove .buildinfo file from HTML docs

* Thu Jun 24 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.0-1
- Update to 2.0.0 (closes RHBZ#1974521)
- Drop 9f0e834b2e5eea5dfe21d5be4ea6a3df47baf0b9.patch, now merged upstream
- Add downstream man page for new “sure” executable

* Thu Jun 24 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.4.11-15
- Add license file to new -doc subpackage

* Wed Jun 23 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 1.4.11-14
- Rename %%pypi_name to %%srcname
- Switch to GitHub tarball, which includes docs/
- Use pytest instead of nose (which is deprecated) as the test runner in
  %%check; we are not quite ready to remove the nose BR, however
- Drop manual Requires on python3-six; it will be generated from metadata
- Drop obsolete %%python_provide macro
- Properly mark the license file
- Package CHANGELOG.md, README.rst, and TODO.rst
- Update summaries and descriptions
- Switch to pyproject-rpm-macros
- Build the HTML documentation and add a -doc subpackage

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.4.11-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-8
- Subpackage python2-sure has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 15 2019 Richard Shaw <hobbes1069@gmail.com> - 1.4.11-7
- Rebuild for Python 3.8.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-4
- Fix ambiguous Python requires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-2
- Rebuilt for Python 3.7

* Thu May 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.11-1
- Updated to 1.4.11 (#1421319)

* Thu May 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.10-1
- Updated to 1.4.10 that supports Python 3.7 (#1578530)
- Stop py3dir pushd/popd, it is not needed
- Removed an unneeded shebeng sed
- Drop %%sum macro, use %%summary
- Drop forbidden SCL macros
- Drop unneeded python3 conditional

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.4.0-4
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 21 2016 Adam Williamson <awilliam@redhat.com> - 1.4.0-1
- New release 1.4.0 (builds against Python 3.6)
- Drop sources merged upstream
- Modernize spec a bit (use modern macros)
- Rename python2 package to python2-sure

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 1.2.7-3
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 14 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.2.7-1
- Updated to 1.2.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 31 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.5-2
- Remove unneeded dependencies from setup.py.
Resolves: rhbz#1082400

* Fri Mar 07 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.5-1
- Updated to 1.2.5
- Fix with_python3 macro definition to work correctly on EPEL, too.

* Fri Nov 29 2013 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-1
- Updated
- Introduced Python 3 subpackage

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.7-2
- Introduce SCL macros in the specfile.

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.7-1
- Update to 1.1.7.
- License change from MIT to GPLv3.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.6-1
- Update to 1.0.6.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.3-2
- python-devel should be python2-devel
- URL now points to the real homepage of the project

* Fri Jun 22 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.10.3-1
- Initial package.

