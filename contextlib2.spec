#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : contextlib2
Version  : 0.5.5
Release  : 20
URL      : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Source0  : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Summary  : Backports and enhancements for the contextlib module
Group    : Development/Tools
License  : Python-2.0
Requires: contextlib2-legacypython
Requires: contextlib2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
.. image:: https://jazzband.co/static/img/badge.svg
:target: https://jazzband.co/
:alt: Jazzband

%package legacypython
Summary: legacypython components for the contextlib2 package.
Group: Default

%description legacypython
legacypython components for the contextlib2 package.


%package python
Summary: python components for the contextlib2 package.
Group: Default
Requires: contextlib2-legacypython

%description python
python components for the contextlib2 package.


%prep
%setup -q -n contextlib2-0.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505000419
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 test_contextlib2.py
%install
export SOURCE_DATE_EPOCH=1505000419
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
