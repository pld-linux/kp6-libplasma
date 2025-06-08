# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	6.3.5
%define		qtver		5.15.2
%define		kf6ver		5.102.0
%define		kpname		libplasma

Summary:	Foundational libraries, components, and tools of the Plasma workspaces
Summary(pl.UTF-8):	Podstawowe biblioteki, komponenty i narzędzia środowiska Plasma
Name:		kp6-%{kpname}
Version:	6.3.5
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	2cd56cb43fa2b117426a21910823ee82
URL:		http://www.kde.org/
BuildRequires:	AppStream-qt6-devel >= 1.0
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6PrintSupport-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Svg-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6WaylandClient-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.22
BuildRequires:	fontconfig-devel
BuildRequires:	gpsd-devel
BuildRequires:	iso-codes
BuildRequires:	ka6-kio-extras-devel
BuildRequires:	ka6-libkexiv2-devel
BuildRequires:	kf6-baloo-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kf6ver}
BuildRequires:	kf6-karchive-devel >= %{kf6ver}
BuildRequires:	kf6-kauth-devel >= %{kf6ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf6ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kcrash-devel >= %{kf6ver}
BuildRequires:	kf6-kdbusaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kdeclarative-devel >= %{kf6ver}
BuildRequires:	kf6-kded-devel
BuildRequires:	kf6-kdoctools-devel >= %{kf6ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf6ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf6ver}
BuildRequires:	kf6-kholidays-devel
BuildRequires:	kf6-ki18n-devel >= %{kf6ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf6ver}
BuildRequires:	kf6-kidletime-devel >= %{kf6ver}
BuildRequires:	kf6-kio-devel >= %{kf6ver}
BuildRequires:	kf6-kirigami-devel >= %{kf6ver}
BuildRequires:	kf6-kitemmodels-devel >= %{kf6ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf6ver}
BuildRequires:	kf6-knotifications-devel >= %{kf6ver}
BuildRequires:	kf6-knotifyconfig-devel >= %{kf6ver}
BuildRequires:	kf6-kpackage-devel >= %{kf6ver}
BuildRequires:	kf6-kpeople-devel >= %{kf6ver}
BuildRequires:	kf6-kquickcharts-devel >= %{kf6ver}
BuildRequires:	kf6-krunner-devel >= %{kf6ver}
BuildRequires:	kf6-ksvg-devel >= %{kf6ver}
BuildRequires:	kf6-ktexteditor-devel >= %{kf6ver}
BuildRequires:	kf6-ktextwidgets-devel >= %{kf6ver}
BuildRequires:	kf6-kunitconversion-devel >= %{kf6ver}
BuildRequires:	kf6-kwallet-devel >= %{kf6ver}
BuildRequires:	kf6-networkmanager-qt-devel >= %{kf6ver}
BuildRequires:	kf6-prison-devel >= %{kf6ver}
BuildRequires:	kp6-plasma-activities-devel >= %{version}
BuildRequires:	kuserfeedback-devel
BuildRequires:	libdrm-devel
BuildRequires:	libicu-devel
BuildRequires:	libqalculate-devel > 2.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	phonon-qt6-devel >= 4.6.60
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig
BuildRequires:	plasma-wayland-protocols-devel >= 1.6
BuildRequires:	polkit-qt6-1-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.31
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildConflicts:	phonon-qt5
Requires:	kp6-libplasma-data = %{version}-%{release}
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libplasma provides the following:
- QML components that can be used by any Plasma shell
- A C++ library: libplasma itself
- Script engines

%description -l pl.UTF-8
libplasma obejmuje:
- komponenty QML, które mogą być używane z powłoką Plasma
- samą bibliotekę C++ libplasma
- silniki skryptowe

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
Obsoletes:	kp5-%{kpname}-data < 6
BuildArch:	noarch

%description data
Data for %{kpname}.

%description data -l pl.UTF-8
Dane dla %{kpname}.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Gui-devel >= %{qtver}
Requires:	Qt6Qml-devel >= %{qtver}
Requires:	kf6-kpackage-devel >= %{kf6ver}
Requires:	kf6-kwindowsystem-devel >= %{kf6ver}
Obsoletes:	kp5-%{kpname}-devel < 6

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname}6 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPlasma.so.*.*
%ghost %{_libdir}/libPlasma.so.6
%attr(755,root,root) %{_libdir}/libPlasmaQuick.so.*.*
%ghost %{_libdir}/libPlasmaQuick.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kirigami/platform/KirigamiPlasmaStyle.so
%dir %{_libdir}/qt6/plugins/kf6/packagestructure
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_applet.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_containmentactions.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_generic.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_shell.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_theme.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/packagestructure/plasma_wallpaper.so
%dir %{_libdir}/qt6/qml/org/kde/kirigami/styles/Plasma
%{_libdir}/qt6/qml/org/kde/kirigami/styles/Plasma/AbstractApplicationHeader.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/components
%{_libdir}/qt6/qml/org/kde/plasma/components/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/components/liborg_kde_plasmacomponents3.so
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection
%{_libdir}/qt6/qml/org/kde/plasma/components/org_kde_plasmacomponents3.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/components/private
%{_libdir}/qt6/qml/org/kde/plasma/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/core
%{_libdir}/qt6/qml/org/kde/plasma/core/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/core/corebindingsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/core/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/core/libcorebindingsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/core/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/extras
%{_libdir}/qt6/qml/org/kde/plasma/extras/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations
%{_libdir}/qt6/qml/org/kde/plasma/extras/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/extras/plasmaextracomponentsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/extras/private
%{_libdir}/qt6/qml/org/kde/plasma/extras/qmldir

%files data -f %{kpname}6.lang
%defattr(644,root,root,755)
%dir %{_datadir}/plasma/desktoptheme
%{_datadir}/plasma/desktoptheme/breeze-dark
%{_datadir}/plasma/desktoptheme/breeze-light
%{_datadir}/plasma/desktoptheme/default
%{_datadir}/qlogging-categories6/plasma-framework.categories
%{_datadir}/qlogging-categories6/plasma-framework.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libPlasma.so
%{_libdir}/libPlasmaQuick.so
%{_includedir}/Plasma
%{_includedir}/PlasmaQuick
%{_libdir}/cmake/Plasma
%{_libdir}/cmake/PlasmaQuick
%{_datadir}/kdevappwizard/templates/cpp-plasmoid6.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma6-wallpaper.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma6-wallpaper-with-qml-extension.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid6.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid6-with-qml-extension.tar.bz2
