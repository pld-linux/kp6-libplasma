#
# Conditional build:
%bcond_with	tests		# test suite

%define		kf_ver		6.10.0
%define		kp_ver		%{version}
%define		qt_ver		6.7.0
%define		kpname		libplasma

Summary:	Foundational libraries, components, and tools of the Plasma workspaces
Summary(pl.UTF-8):	Podstawowe biblioteki, komponenty i narzędzia środowiska Plasma
Name:		kp6-%{kpname}
Version:	6.5.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kp_ver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	96fdd50badad00db75d941951753386a
URL:		https://kde.org/
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Qml-devel >= %{qt_ver}
# QtQuick, QuickControls2, %{?with_tests:QuickTests}
BuildRequires:	Qt6Quick-devel >= %{qt_ver}
BuildRequires:	Qt6Svg-devel >= %{qt_ver}
%{?with_tests:BuildRequires:	Qt6Test-devel >= %{qt_ver}}
BuildRequires:	Qt6WaylandClient-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.22
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-karchive-devel >= %{kf_ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
# examples only
#BuildRequires:	kf6-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kglobalaccel-devel >= %{kf_ver}
BuildRequires:	kf6-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-kirigami-devel >= %{kf_ver}
BuildRequires:	kf6-knotifications-devel >= %{kf_ver}
BuildRequires:	kf6-kpackage-devel >= %{kf_ver}
BuildRequires:	kf6-ksvg-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kp6-plasma-activities-devel >= %{kp_ver}
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libxcb-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	plasma-wayland-protocols-devel >= 1.10.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	wayland-devel >= 1.9
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xz
Requires:	%{name}-data = %{version}-%{release}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Qml >= %{qt_ver}
Requires:	Qt6Quick >= %{qt_ver}
Requires:	Qt6WaylandClient >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-kglobalaccel >= %{kf_ver}
Requires:	kf6-kguiaddons >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kiconthemes >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-kirigami >= %{kf_ver}
Requires:	kf6-knotifications >= %{kf_ver}
Requires:	kf6-kpackage >= %{kf_ver}
Requires:	kf6-ksvg >= %{kf_ver}
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kwindowsystem >= %{kf_ver}
Requires:	kp6-plasma-activities >= %{kp_ver}
Requires:	wayland >= 1.9
%requires_eq_to Qt6Core Qt6Core-devel
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
Provides:	kf5-plasma-desktoptheme-breeze = %{version}-%{release}
Obsoletes:	kf5-plasma-desktoptheme-breeze < 6
Conflicts:	kf5-plasma-framework < 5.116.0-2
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
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Gui-devel >= %{qt_ver}
Requires:	Qt6Qml-devel >= %{qt_ver}
Requires:	Qt6Quick-devel >= %{qt_ver}
Requires:	kf6-kconfig-devel >= %{kf_ver}
Requires:	kf6-kcoreaddons-devel >= %{kf_ver}
Requires:	kf6-kpackage-devel >= %{kf_ver}
Requires:	kf6-kwindowsystem-devel >= %{kf_ver}
Requires:	libstdc++-devel >= 6:8

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
%{_libdir}/libPlasma.so.*.*
%ghost %{_libdir}/libPlasma.so.6
%{_libdir}/libPlasmaQuick.so.*.*
%ghost %{_libdir}/libPlasmaQuick.so.6
%{_libdir}/qt6/plugins/kf6/kirigami/platform/KirigamiPlasmaStyle.so
%dir %{_libdir}/qt6/plugins/kf6/packagestructure
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_applet.so
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_containmentactions.so
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_generic.so
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_shell.so
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_theme.so
%{_libdir}/qt6/plugins/kf6/packagestructure/plasma_wallpaper.so
%dir %{_libdir}/qt6/qml/org/kde/kirigami/styles/Plasma
%{_libdir}/qt6/qml/org/kde/kirigami/styles/Plasma/AbstractApplicationHeader.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/components
%{_libdir}/qt6/qml/org/kde/plasma/components/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/components/liborg_kde_plasmacomponents3.so
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection
%{_libdir}/qt6/qml/org/kde/plasma/components/org_kde_plasmacomponents3.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/components/private
%{_libdir}/qt6/qml/org/kde/plasma/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/core
%{_libdir}/qt6/qml/org/kde/plasma/core/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/core/corebindingsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/core/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/core/libcorebindingsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/core/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/extras
%{_libdir}/qt6/qml/org/kde/plasma/extras/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations
%{_libdir}/qt6/qml/org/kde/plasma/extras/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/extras/plasmaextracomponentsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/extras/private
%{_libdir}/qt6/qml/org/kde/plasma/extras/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/configuration
%{_libdir}/qt6/qml/org/kde/plasma/configuration/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/configuration/libplasmaconfigplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/configuration/plasmaconfigplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/configuration/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/plasmoid
%{_libdir}/qt6/qml/org/kde/plasma/plasmoid/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/plasmoid/libplasmoidplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/plasmoid/plasmoidplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/plasmoid/qmldir

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
##%{_datadir}/kdevappwizard/templates/qml-plasmoid6-with-qml-extension.tar.bz2
