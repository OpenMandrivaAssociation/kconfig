%define major 4
%define libname %mklibname KF5Config %{major}
%define devname %mklibname KF5Config -d
%define debug_package %{nil}

Name: kconfig
Version: 4.96.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: The KDE Frameworks 5 configuration library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 configuration library.

%package -n %{libname}
Summary: The KDE Frameworks 5 configuration library
Group: System/Libraries

%description -n %{libname}
The KDE Frameworks 5 configuration library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
# We allow cmake to return an error code because this should really be a
# warning instead of an error:
# install(EXPORT "KF5ConfigTargets") given absolute DESTINATION "/usr/lib64/cmake/KF5Config" but the export references an installation of target "kconfig_compiler_kf5" which has relative DESTINATION "bin"
%cmake || :

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

%files
%{_libdir}/kde5/libexec/kconf_update

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_bindir}/kconfig_compiler_kf5
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Config
%{_libdir}/qt5/mkspecs/modules/*.pri
