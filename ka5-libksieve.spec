%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		libksieve
Summary:	Libksieve
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	14d4b35e3c24f3afccaa035b8126a372
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kimap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-karchive-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-knewstuff-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	kf5-syntax-highlighting-devel >= 5.51.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This lib manages sieve support.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/ksieve_script.knsrc
/etc/xdg/libksieve.categories
/etc/xdg/libksieve.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5KManageSieve.so.5
%attr(755,root,root) %{_libdir}/libKF5KManageSieve.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KSieve.so.5
%attr(755,root,root) %{_libdir}/libKF5KSieve.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KSieveUi.so.5
%attr(755,root,root) %{_libdir}/libKF5KSieveUi.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/sieve.so
%{_datadir}/kservices5/sieve.protocol
%{_datadir}/sieve

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KManageSieve
%{_includedir}/KF5/KSieveUi
%{_includedir}/KF5/kmanagesieve
%{_includedir}/KF5/ksieveui
%{_includedir}/KF5/libksieve_version.h
%{_libdir}/cmake/KF5LibKSieve
%attr(755,root,root) %{_libdir}/libKF5KManageSieve.so
%attr(755,root,root) %{_libdir}/libKF5KSieve.so
%attr(755,root,root) %{_libdir}/libKF5KSieveUi.so
%{_libdir}/qt5/mkspecs/modules/qt_KManageSieve.pri
%{_libdir}/qt5/mkspecs/modules/qt_KSieve.pri
%{_libdir}/qt5/mkspecs/modules/qt_KSieveUi.pri
