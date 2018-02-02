#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : iperf
Version  : 3.3
Release  : 12
URL      : https://github.com/esnet/iperf/archive/3.3.tar.gz
Source0  : https://github.com/esnet/iperf/archive/3.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: iperf-bin
Requires: iperf-lib
Requires: iperf-doc
BuildRequires : openssl-dev

%description
iperf3:  A TCP, UDP, and SCTP network bandwidth measurement tool
================================================================

%package bin
Summary: bin components for the iperf package.
Group: Binaries

%description bin
bin components for the iperf package.


%package dev
Summary: dev components for the iperf package.
Group: Development
Requires: iperf-lib
Requires: iperf-bin
Provides: iperf-devel

%description dev
dev components for the iperf package.


%package doc
Summary: doc components for the iperf package.
Group: Documentation

%description doc
doc components for the iperf package.


%package lib
Summary: lib components for the iperf package.
Group: Libraries

%description lib
lib components for the iperf package.


%prep
%setup -q -n iperf-3.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510349058
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1510349058
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iperf3

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libiperf.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libiperf.so.0
/usr/lib64/libiperf.so.0.0.0
