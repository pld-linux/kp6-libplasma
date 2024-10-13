#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
#  * dbusmenu-qt5 , Support for notification area menus via the DBusMenu protocol , <https://launchpad.net/libdbusmenu-qt>
#
%define		kdeplasmaver	6.2.0
%define		qtver		5.15.2
%define		kf6ver		5.102.0
%define		kpname		libplasma

Summary:	KDE libplasma
Name:		kp6-%{kpname}
Version:	6.2.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	790b44cedb04295e78605886cb692f17
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
BuildRequires:	plasma-wayland-protocols-devel >= 1.6
BuildRequires:	pkgconfig
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
Requires:	kp6-libplasma-data = %{version}-%{release}
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
KDE libplasma.

%package data
Summary:	Data files for %{kpname}
Summary(pl.UTF-8):	Dane dla %{kpname}
Group:		X11/Applications
Obsoletes:	kp5-%{kpname}-data < %{version}
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
Obsoletes:	kp5-%{kpname}-devel < %{version}

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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
%{_libdir}/qt6/qml/org/kde/plasma/components/AbstractButton.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/BusyIndicator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Button.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/CheckBox.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/CheckDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/CheckIndicator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ComboBox.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Container.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Control.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Dial.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Dialog.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/DialogButtonBox.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Drawer.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Frame.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/GroupBox.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Label.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Menu.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/MenuItem.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/MenuSeparator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Page.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/PageIndicator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Pane.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Popup.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ProgressBar.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/RadioButton.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/RadioDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/RadioIndicator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/RangeSlider.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/RoundButton.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ScrollBar.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ScrollView.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Slider.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/SpinBox.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/SwipeView.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/Switch.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/SwitchDelegate.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/SwitchIndicator.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/TabBar.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/TabButton.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/TextArea.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/TextField.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ToolBar.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ToolButton.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/ToolTip.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/components/liborg_kde_plasmacomponents3.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileCursor.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileTextActionsToolBar.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection/MobileTextActionsToolBarImpl.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/mobiletextselection/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/components/org_kde_plasmacomponents3.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/components/private
%{_libdir}/qt6/qml/org/kde/plasma/components/private/ButtonBackground.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/ButtonContent.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/ButtonFocus.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/ButtonHover.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/ButtonShadow.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/DefaultListItemBackground.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/FlatButtonBackground.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/IconLabel.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/RaisedButtonBackground.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/RoundShadow.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/private/TextFieldFocus.qml
%{_libdir}/qt6/qml/org/kde/plasma/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/core
%{_libdir}/qt6/qml/org/kde/plasma/core/corebindingsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/core/kde-qmlmodule.version
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/core/libcorebindingsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/core/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/core/DefaultToolTip.qml
%{_libdir}/qt6/qml/org/kde/plasma/core/DialogBackground.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/extras
%{_libdir}/qt6/qml/org/kde/plasma/extras/ActionTextField.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/BasicPlasmoidHeading.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/DescriptiveLabel.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/ExpandableListItem.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/Heading.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/Highlight.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/ListItem.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/ModelContextMenu.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/PasswordField.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/PlaceholderMessage.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/PlasmoidHeading.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/Representation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/SearchField.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/ShadowedLabel.qml
%dir %{_libdir}/qt6/qml/org/kde/plasma/extras/animations
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations/ActivateAnimation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations/AppearAnimation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations/DisappearAnimation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations/PressedAnimation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/animations/ReleasedAnimation.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/extras/plasmaextracomponentsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/extras/private
%{_libdir}/qt6/qml/org/kde/plasma/extras/private/BackgroundMetrics.qml
%{_libdir}/qt6/qml/org/kde/plasma/extras/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/extras/ListSectionHeader.qml

%files data -f %{kpname}6.lang
%defattr(644,root,root,755)
%dir %{_datadir}/plasma/desktoptheme
%dir %{_datadir}/plasma/desktoptheme/breeze-dark
%{_datadir}/plasma/desktoptheme/breeze-dark/colors
%{_datadir}/plasma/desktoptheme/breeze-dark/metadata.json
%{_datadir}/plasma/desktoptheme/breeze-dark/plasmarc
%dir %{_datadir}/plasma/desktoptheme/breeze-light
%{_datadir}/plasma/desktoptheme/breeze-light/colors
%{_datadir}/plasma/desktoptheme/breeze-light/metadata.json
%{_datadir}/plasma/desktoptheme/breeze-light/plasmarc
%dir %{_datadir}/plasma/desktoptheme/default
%dir %{_datadir}/plasma/desktoptheme/default/dialogs
%{_datadir}/plasma/desktoptheme/default/dialogs/background.svgz
%dir %{_datadir}/plasma/desktoptheme/default/icons
%{_datadir}/plasma/desktoptheme/default/icons/akonadi.svgz
%{_datadir}/plasma/desktoptheme/default/icons/akregator.svgz
%{_datadir}/plasma/desktoptheme/default/icons/amarok.svgz
%{_datadir}/plasma/desktoptheme/default/icons/applications.svgz
%{_datadir}/plasma/desktoptheme/default/icons/apport.svgz
%{_datadir}/plasma/desktoptheme/default/icons/audio.svgz
%{_datadir}/plasma/desktoptheme/default/icons/battery.svgz
%{_datadir}/plasma/desktoptheme/default/icons/bookmarks.svgz
%{_datadir}/plasma/desktoptheme/default/icons/cantata.svgz
%{_datadir}/plasma/desktoptheme/default/icons/computer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/configure.svgz
%{_datadir}/plasma/desktoptheme/default/icons/device.svgz
%{_datadir}/plasma/desktoptheme/default/icons/disk.svgz
%{_datadir}/plasma/desktoptheme/default/icons/distribute.svgz
%{_datadir}/plasma/desktoptheme/default/icons/document.svgz
%{_datadir}/plasma/desktoptheme/default/icons/drive.svgz
%{_datadir}/plasma/desktoptheme/default/icons/edit.svgz
%{_datadir}/plasma/desktoptheme/default/icons/fcitx.svgz
%{_datadir}/plasma/desktoptheme/default/icons/go.svgz
%{_datadir}/plasma/desktoptheme/default/icons/ime.svgz
%{_datadir}/plasma/desktoptheme/default/icons/input.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kalarm.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kdeconnect.svgz
%{_datadir}/plasma/desktoptheme/default/icons/keyboard.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kget.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kgpg.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kleopatra.svgz
%{_datadir}/plasma/desktoptheme/default/icons/klipper.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kmail.svgz
%{_datadir}/plasma/desktoptheme/default/icons/konv_message.svgz
%{_datadir}/plasma/desktoptheme/default/icons/konversation.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kopete.svgz
%{_datadir}/plasma/desktoptheme/default/icons/korgac.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kpackagekit.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kruler.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kteatime.svgz
%{_datadir}/plasma/desktoptheme/default/icons/ktorrent.svgz
%{_datadir}/plasma/desktoptheme/default/icons/kup.svgz
%{_datadir}/plasma/desktoptheme/default/icons/list.svgz
%{_datadir}/plasma/desktoptheme/default/icons/mail.svgz
%{_datadir}/plasma/desktoptheme/default/icons/media.svgz
%{_datadir}/plasma/desktoptheme/default/icons/mobile.svgz
%{_datadir}/plasma/desktoptheme/default/icons/network.svgz
%{_datadir}/plasma/desktoptheme/default/icons/notification.svgz
%{_datadir}/plasma/desktoptheme/default/icons/osd.svgz
%{_datadir}/plasma/desktoptheme/default/icons/phone.svgz
%{_datadir}/plasma/desktoptheme/default/icons/plasmavault.svgz
%{_datadir}/plasma/desktoptheme/default/icons/plasmavault_error.svgz
%{_datadir}/plasma/desktoptheme/default/icons/preferences.svgz
%{_datadir}/plasma/desktoptheme/default/icons/printer.svgz
%{_datadir}/plasma/desktoptheme/default/icons/quassel.svgz
%{_datadir}/plasma/desktoptheme/default/icons/search.svgz
%{_datadir}/plasma/desktoptheme/default/icons/slc.svgz
%{_datadir}/plasma/desktoptheme/default/icons/software.svgz
%{_datadir}/plasma/desktoptheme/default/icons/start.svgz
%{_datadir}/plasma/desktoptheme/default/icons/system.svgz
%{_datadir}/plasma/desktoptheme/default/icons/touchpad.svgz
%{_datadir}/plasma/desktoptheme/default/icons/user.svgz
%{_datadir}/plasma/desktoptheme/default/icons/video-card.svgz
%{_datadir}/plasma/desktoptheme/default/icons/video.svgz
%{_datadir}/plasma/desktoptheme/default/icons/view.svgz
%{_datadir}/plasma/desktoptheme/default/icons/vlc.svgz
%{_datadir}/plasma/desktoptheme/default/icons/wallet.svgz
%{_datadir}/plasma/desktoptheme/default/icons/window.svgz
%{_datadir}/plasma/desktoptheme/default/icons/yakuake.svgz
%{_datadir}/plasma/desktoptheme/default/icons/zoom.svgz
%{_datadir}/plasma/desktoptheme/default/metadata.json
%dir %{_datadir}/plasma/desktoptheme/default/opaque
%dir %{_datadir}/plasma/desktoptheme/default/opaque/dialogs
%{_datadir}/plasma/desktoptheme/default/opaque/dialogs/background.svgz
%dir %{_datadir}/plasma/desktoptheme/default/opaque/widgets
%{_datadir}/plasma/desktoptheme/default/opaque/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/opaque/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/default/plasmarc
%dir %{_datadir}/plasma/desktoptheme/default/solid
%dir %{_datadir}/plasma/desktoptheme/default/solid/dialogs
%{_datadir}/plasma/desktoptheme/default/solid/dialogs/background.svgz
%dir %{_datadir}/plasma/desktoptheme/default/solid/widgets
%{_datadir}/plasma/desktoptheme/default/solid/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/default/solid/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/solid/widgets/tooltip.svgz
%dir %{_datadir}/plasma/desktoptheme/default/translucent
%dir %{_datadir}/plasma/desktoptheme/default/translucent/dialogs
%{_datadir}/plasma/desktoptheme/default/translucent/dialogs/background.svgz
%dir %{_datadir}/plasma/desktoptheme/default/translucent/widgets
%{_datadir}/plasma/desktoptheme/default/translucent/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/default/translucent/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/translucent/widgets/tooltip.svgz
%dir %{_datadir}/plasma/desktoptheme/default/widgets
%{_datadir}/plasma/desktoptheme/default/widgets/action-overlays.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/actionbutton.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/analog_meter.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/arrows.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/bar_meter_horizontal.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/bar_meter_vertical.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/branding.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/busywidget.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/button.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/calendar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/checkmarks.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/clock.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/configuration-icons.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/containment-controls.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/dragger.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/frame.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/glowbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/line.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/lineedit.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/listitem.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/margins-highlight.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/media-delegate.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/menubaritem.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/monitor.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/notes.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/pager.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/panel-background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/picker.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/plasmoidheading.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/plot-background.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/radiobutton.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/scrollbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/scrollwidget.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/slider.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/switch.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tabbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tasks.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/toolbar.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/tooltip.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/translucentbackground.svgz
%{_datadir}/plasma/desktoptheme/default/widgets/viewitem.svgz
%{_datadir}/qlogging-categories6/plasma-framework.categories
%{_datadir}/qlogging-categories6/plasma-framework.renamecategories


%files devel
%defattr(644,root,root,755)
%{_includedir}/Plasma
%{_includedir}/PlasmaQuick
%{_libdir}/cmake/Plasma
%{_libdir}/cmake/PlasmaQuick
%{_libdir}/libPlasma.so
%{_libdir}/libPlasmaQuick.so
%{_datadir}/kdevappwizard/templates/cpp-plasmoid6.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma6-wallpaper-with-qml-extension.tar.bz2
%{_datadir}/kdevappwizard/templates/plasma6-wallpaper.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid6-with-qml-extension.tar.bz2
%{_datadir}/kdevappwizard/templates/qml-plasmoid6.tar.bz2
