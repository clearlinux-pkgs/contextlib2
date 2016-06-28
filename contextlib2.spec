#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : contextlib2
Version  : 0.5.1
Release  : 10
URL      : https://pypi.python.org/packages/source/c/contextlib2/contextlib2-0.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/contextlib2/contextlib2-0.5.1.tar.gz
Summary  : Backports and enhancements for the contextlib module
Group    : Development/Tools
License  : Python-2.0
Requires: contextlib2-python
BuildRequires : linecache2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : unittest2
BuildRequires : unittest2-python

%description
.. image:: https://readthedocs.org/projects/contextlib2/badge/?version=latest
:target: https://contextlib2.readthedocs.org/
:alt: Latest Docs

%package python
Summary: python components for the contextlib2 package.
Group: Default

%description python
python components for the contextlib2 package.


%prep
%setup -q -n contextlib2-0.5.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 test_contextlib2.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
