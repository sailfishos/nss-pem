Name:       nss-pem
Version:    1.1.0
Release:    1
Summary:    PEM file reader for Network Security Services (NSS)

License:    GPLv2 and (MPLv1.1 or GPLv2+ or LGPLv2+)
URL:        https://github.com/sailfishos/nss-pem
Source0:    %{name}-%{version}.tar.bz2
Patch1:     0001-cmake-require-at-least-CMake-3.5.patch
BuildRequires: cmake
BuildRequires: nss-pkcs11-devel
Requires: nss

%description
PEM file reader for Network Security Services (NSS), implemented as a PKCS#11
module.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%cmake src
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libnsspem.so
%license COPYING.{GPL,MPL}
