#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 5424026
#
Name     : iperf
Version  : 3.18
Release  : 32
URL      : https://github.com/esnet/iperf/archive/3.18/iperf-3.18.tar.gz
Source0  : https://github.com/esnet/iperf/archive/3.18/iperf-3.18.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: iperf-bin = %{version}-%{release}
Requires: iperf-lib = %{version}-%{release}
Requires: iperf-license = %{version}-%{release}
Requires: iperf-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : openssl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
iperf3:  A TCP, UDP, and SCTP network bandwidth measurement tool
================================================================

%package bin
Summary: bin components for the iperf package.
Group: Binaries
Requires: iperf-license = %{version}-%{release}

%description bin
bin components for the iperf package.


%package dev
Summary: dev components for the iperf package.
Group: Development
Requires: iperf-lib = %{version}-%{release}
Requires: iperf-bin = %{version}-%{release}
Provides: iperf-devel = %{version}-%{release}
Requires: iperf = %{version}-%{release}

%description dev
dev components for the iperf package.


%package lib
Summary: lib components for the iperf package.
Group: Libraries
Requires: iperf-license = %{version}-%{release}

%description lib
lib components for the iperf package.


%package license
Summary: license components for the iperf package.
Group: Default

%description license
license components for the iperf package.


%package man
Summary: man components for the iperf package.
Group: Default

%description man
man components for the iperf package.


%prep
%setup -q -n iperf-3.18
cd %{_builddir}/iperf-3.18
pushd ..
cp -a iperf-3.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735083331
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735083331
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/iperf
cp %{_builddir}/iperf-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/iperf/facf5d2f0df5e3883df7f14d54bef01ac589cec6 || :
cp %{_builddir}/iperf-%{version}/docs/_esnet/LICENSE %{buildroot}/usr/share/package-licenses/iperf/2710606f6db128e7cf24e84572811bbf177a4ce9 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/iperf3
/usr/bin/iperf3

%files dev
%defattr(-,root,root,-)
/usr/include/iperf_api.h
/usr/lib64/libiperf.so
/usr/share/man/man3/libiperf.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libiperf.so.0.0.0
/usr/lib64/libiperf.so.0
/usr/lib64/libiperf.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/iperf/2710606f6db128e7cf24e84572811bbf177a4ce9
/usr/share/package-licenses/iperf/facf5d2f0df5e3883df7f14d54bef01ac589cec6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/iperf3.1
