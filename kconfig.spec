%define major 5
%define libname %mklibname KF5Config %{major}
%define devname %mklibname KF5Config -d
%define debug_package %{nil}

Name: kconfig
Version: 5.2.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Patch0: kconfig-4.99.0-install-location.patch
Summary: The KDE Frameworks 5 configuration library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake >= 2.8.12.2-3
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: qt5-platformtheme-gtk2
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: ninja
Requires: %{libname} = %{EVRD}

%description
The KDE Frameworks 5 configuration library.

%package -n %{libname}
Summary: The KDE Frameworks 5 configuration library
Group: System/Libraries
Requires: %{name} = %{EVRD}

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
%apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_libdir}/qt5
mv %{buildroot}%{_prefix}/mkspecs %{buildroot}%{_libdir}/qt5

L="`pwd`/kconfig%{major}_qt.lang"
cd %{buildroot}
for i in .%{_datadir}/locale/*/LC_MESSAGES/*.qm; do
	LNG=`echo $i |cut -d/ -f5`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f kconfig%{major}_qt.lang
%{_bindir}/kreadconfig5
%{_bindir}/kwriteconfig5
%{_libdir}/libexec/kf5/kconf_update

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{version}

%files -n %{devname}
%{_bindir}/kconfig_compiler_kf5
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/KF5Config
%{_libdir}/qt5/mkspecs/modules/*.pri
