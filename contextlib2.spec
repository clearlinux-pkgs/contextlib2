#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : contextlib2
Version  : 0.5.5
Release  : 62
URL      : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Source0  : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Summary  : Backports and enhancements for the contextlib module
Group    : Development/Tools
License  : Python-2.0
Requires: contextlib2-license = %{version}-%{release}
Requires: contextlib2-python = %{version}-%{release}
Requires: contextlib2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3
BuildRequires : six

%description
.. image:: https://jazzband.co/static/img/badge.svg
:target: https://jazzband.co/
:alt: Jazzband

%package license
Summary: license components for the contextlib2 package.
Group: Default

%description license
license components for the contextlib2 package.


%package python
Summary: python components for the contextlib2 package.
Group: Default
Requires: contextlib2-python3 = %{version}-%{release}

%description python
python components for the contextlib2 package.


%package python3
Summary: python3 components for the contextlib2 package.
Group: Default
Requires: python3-core
Provides: pypi(contextlib2)

%description python3
python3 components for the contextlib2 package.


%prep
%setup -q -n contextlib2-0.5.5
cd %{_builddir}/contextlib2-0.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603410640
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/contextlib2
cp %{_builddir}/contextlib2-0.5.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/contextlib2/ec7666523bed16e7f16d28b4d628caf55a31c7b4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/contextlib2/ec7666523bed16e7f16d28b4d628caf55a31c7b4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
