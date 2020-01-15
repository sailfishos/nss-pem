Name:       nss-pem
Version:    1.0.5
Release:    1
Summary:    PEM file reader for Network Security Services (NSS)

License:    MPLv1.1
URL:        https://github.com/kdudka/nss-pem
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: nss-pkcs11-devel
Requires: nss

%description
PEM file reader for Network Security Services (NSS), implemented as a PKCS#11
module.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
mkdir build
cd build
%cmake ../src
make %{?_smp_mflags} VERBOSE=yes

%install
cd build
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libnsspem.so
%license COPYING
