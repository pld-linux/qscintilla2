# TODO:
# - fix building with qscintilla2(-devel) installed, remove BC
#   - how to successfully prepend -I../Qt4Qt5 before system qt include in qmake?
#
# Conditional build:
%bcond_without	qt5		# Qt5 library and modules
%bcond_without	qt6		# Qt6 library and modules
#
%define		scintilla_ver	3.3.6
%define		sip_ver		6.4
%define		pyqt5_ver	5.15.7
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt
Name:		qscintilla2
Version:	2.13.3
Release:	5
License:	GPL v3
Group:		X11/Libraries
Source0:	https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
# Source0-md5:	af0dab4ff9908e0d41934aff6ce2348d
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/
%if %{with qt5}
BuildRequires:	Qt5Designer-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	Qt5UiTools-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	python3-PyQt5 >= %{pyqt5_ver}
BuildRequires:	python3-PyQt5-devel >= %{pyqt5_ver}
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
%if %{with qt6}
BuildRequires:	Qt6Designer-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6UiTools-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	python3-PyQt6
BuildRequires:	python3-PyQt6-devel
BuildRequires:	qt6-build
BuildRequires:	qt6-qmake
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.558
BuildRequires:	sip6 >= %{sip_ver}
BuildConflicts:	qscintilla2-devel < %{version}
BuildConflicts:	qscintilla2-qt5-devel < %{version}
Obsoletes:	qscintilla2-qt4 < 2.13.3
Obsoletes:	qscintilla2-qt4-devel < 2.13.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QScintilla2 is a port to Qt of the Scintilla editing component. This
version of QScintilla is based on Scintilla v%{scintilla_ver}.

%description -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt. Ta
wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

%package apidocs
Summary:	QScintilla2 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki QScintilla2
Group:		Documentation
BuildArch:	noarch

%description apidocs
QScintilla2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki QScintilla2.

%package qt5
Summary:	QScintilla2 - a port to Qt 5 of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt 5
Group:		X11/Libraries
Obsoletes:	qscintilla2-qt4 < 2.13.3

%description qt5
QScintilla2 is a port to Qt of the Scintilla editing component. This
version of QScintilla is based on Scintilla v%{scintilla_ver}.

This package contains the Qt 5 port.

%description qt5 -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt. Ta
wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

Ten pakiet zawiera port Qt 5.

%package qt5-devel
Summary:	Development files for the QScintilla2 Qt 5 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QScintilla2 dla Qt 5
Group:		X11/Development/Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Gui-devel >= 5
Obsoletes:	qscintilla2-devel < 2.8.4
Obsoletes:	qscintilla2-qt4-devel < 2.13.3

%description qt5-devel
This package contains the header files necessary to develop
applications using QScintilla2 for Qt 5.

%description qt5-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem komponentu QScintilla2 dla Qt 5.

%package -n Qt5Designer-plugin-%{name}
Summary:	QScintilla2 plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka QScintilla2 dla Qt Designera
Group:		X11/Development/Libraries
Requires:	%{name}-qt5 = %{version}-%{release}
Requires:	Qt5Designer >= 5
Obsoletes:	QtDesigner-plugin-qscintilla2 < 2.13.3

%description -n Qt5Designer-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances to
be included in GUI designs just like any other Qt widget.

This package contains the Qt 5 version.

%description -n Qt5Designer-plugin-%{name} -l pl.UTF-8
Wtyczka WScintilla2 dla Qt Designera pozwalająca na włączanie
instancji QScintilli w projekty GUI w ten sam sposób, co inne widgety
Qt.

Ten pakiet zawiera wersję dla Qt 5.

%package -n python3-PyQt5-%{name}
Summary:	Python 3 bindings for the QScintilla2 (PyQt5 version)
Summary(pl.UTF-8):	Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt5)
Group:		Libraries/Python
Requires:	%{name}-qt5 = %{version}-%{release}
%requires_ge python3-PyQt5
Obsoletes:	python-PyQt4-qscintilla2 < 2.13.3
Obsoletes:	python-PyQt5-qscintilla2 < 2.13.3
Obsoletes:	python3-PyQt4-qscintilla2 < 2.13.3

%description -n python3-PyQt5-%{name}
Python 3 bindings for the QScintilla2 (PyQt5 version).

%description -n python3-PyQt5-%{name} -l pl.UTF-8
Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt5).

%package -n python3-PyQt5-%{name}-devel
Summary:	Python bindings for the QScintilla2 - SIP development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne SIP
Group:		Development/Languages/Python
Requires:	python3-PyQt5-devel >= %{pyqt5_ver}
Obsoletes:	sip-PyQt4-qscintilla2 < 2.13.3
Obsoletes:	sip-PyQt5-qscintilla2 < 2.13.3-3

%description -n python3-PyQt5-%{name}-devel
Python bindings for the QScintilla2 - SIP development files.

%description -n python3-PyQt5-%{name}-devel -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
SIP.

%package qt6
Summary:	QScintilla2 - a port to Qt 6 of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt 6
Group:		X11/Libraries
Obsoletes:	qscintilla2-qt4 < 2.13.3

%description qt6
QScintilla2 is a port to Qt of the Scintilla editing component. This
version of QScintilla is based on Scintilla v%{scintilla_ver}.

This package contains the Qt 6 port.

%description qt6 -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt. Ta
wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

Ten pakiet zawiera port Qt 6.

%package qt6-devel
Summary:	Development files for the QScintilla2 Qt 6 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QScintilla2 dla Qt 6
Group:		X11/Development/Libraries
Requires:	%{name}-qt6 = %{version}-%{release}
Requires:	Qt6Gui-devel >= 5
Obsoletes:	qscintilla2-devel < 2.8.4
Obsoletes:	qscintilla2-qt4-devel < 2.13.3

%description qt6-devel
This package contains the header files necessary to develop
applications using QScintilla2 for Qt 6.

%description qt6-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem komponentu QScintilla2 dla Qt 6.

%package -n Qt6Designer-plugin-%{name}
Summary:	QScintilla2 plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka QScintilla2 dla Qt Designera
Group:		X11/Development/Libraries
Requires:	%{name}-qt6 = %{version}-%{release}
Requires:	Qt6Designer >= 5
Obsoletes:	QtDesigner-plugin-qscintilla2 < 2.13.3

%description -n Qt6Designer-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances to
be included in GUI designs just like any other Qt widget.

This package contains the Qt 6 version.

%description -n Qt6Designer-plugin-%{name} -l pl.UTF-8
Wtyczka WScintilla2 dla Qt Designera pozwalająca na włączanie
instancji QScintilli w projekty GUI w ten sam sposób, co inne widgety
Qt.

Ten pakiet zawiera wersję dla Qt 6.

%package -n python3-PyQt6-%{name}
Summary:	Python 3 bindings for the QScintilla2 (PyQt6 version)
Summary(pl.UTF-8):	Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt6)
Group:		Libraries/Python
Requires:	%{name}-qt6 = %{version}-%{release}
%requires_ge python3-PyQt6
Obsoletes:	python-PyQt4-qscintilla2 < 2.13.3

%description -n python3-PyQt6-%{name}
Python 3 bindings for the QScintilla2 (PyQt6 version).

%description -n python3-PyQt6-%{name} -l pl.UTF-8
Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt6).

%package -n python3-PyQt6-%{name}-devel
Summary:	Python bindings for the QScintilla2 - SIP development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne SIP
Group:		Development/Languages/Python
Requires:	python3-PyQt6-devel

%description -n python3-PyQt6-%{name}-devel
Python bindings for the QScintilla2 - SIP development files.

%description -n python3-PyQt6-%{name}-devel -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
SIP.

%prep
%setup -q -n QScintilla_src-%{version}

%if %{with qt5}
install -d build-qt5/{src,designer,Python}
%endif
%if %{with qt6}
install -d build-qt6/{src,designer,Python}
%endif

%build
export QMAKEFEATURES=$PWD/src/features;

for qt in %{?with_qt5:qt5} %{?with_qt6:qt6} ; do
cd build-${qt}/src
qmake-${qt} ../../src/qscintilla.pro QMAKE_MKSPECS=%{_libdir}/${qt}/mkspecs
%{__make}

cd ../designer
qmake-${qt} ../../designer/designer.pro INCLUDEPATH+=../../src LIBS+=-L../src QMAKE_MKSPECS=%{_libdir}/${qt}/mkspecs
%{__make}

cd ../Python
ln -sf ../../Python/* .
ln -sf pyproject-${qt}.toml pyproject.toml

LD_LIBRARY_PATH=$PWD/../../src \
sip-build \
	--no-make \
	--verbose \
	--pep484-pyi \
	--qmake="%{_bindir}/qmake-${qt}" \
	--api-dir=%{_datadir}/${qt}/qsci \
	--qsci-include-dir=../../src \
	--qsci-library-dir=../src \
	--qsci-features-dir=../../src/features
%{__make} -C build
cd ../..
done

%install
rm -rf $RPM_BUILD_ROOT

for qt in %{?with_qt5:qt5} %{?with_qt6:qt6} ; do
cd build-${qt}
%{__make} -j1 -C src install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -j1 -C designer install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -j1 -C Python/build install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
cd ..
done

# unnecessary symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqscintilla2*.so.15.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%post	qt6 -p /sbin/ldconfig
%postun	qt6 -p /sbin/ldconfig

%files apidocs
%defattr(644,root,root,755)
%doc doc/{Scintilla,html}

%files qt5
%defattr(644,root,root,755)
%doc NEWS
%{_libdir}/libqscintilla2_qt5.so.*.*.*
%ghost %{_libdir}/libqscintilla2_qt5.so.15
%lang(cs) %{_datadir}/qt5/translations/qscintilla_cs.qm
%lang(de) %{_datadir}/qt5/translations/qscintilla_de.qm
%lang(es) %{_datadir}/qt5/translations/qscintilla_es.qm
%lang(fr) %{_datadir}/qt5/translations/qscintilla_fr.qm
%lang(pt_BR) %{_datadir}/qt5/translations/qscintilla_pt_br.qm
%dir %{_datadir}/qt5/qsci
%dir %{_datadir}/qt5/qsci/api
%dir %{_datadir}/qt5/qsci/api/python
%{_datadir}/qt5/qsci/api/python/Python-*.api
%{_datadir}/qt5/qsci/QScintilla.api

%files qt5-devel
%defattr(644,root,root,755)
%{_libdir}/libqscintilla2_qt5.so
%{_includedir}/qt5/Qsci
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

%files -n Qt5Designer-plugin-%{name}
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/designer/libqscintillaplugin.so

%files -n python3-PyQt5-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt5/Qsci.abi3.so
%{py3_sitedir}/qscintilla-%{version}.dist-info
%{py3_sitedir}/PyQt5/Qsci.pyi

%files -n python3-PyQt5-%{name}-devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings/Qsci

%files qt6
%defattr(644,root,root,755)
%doc NEWS
%{_libdir}/libqscintilla2_qt6.so.*.*.*
%ghost %{_libdir}/libqscintilla2_qt6.so.15
%lang(cs) %{_datadir}/qt6/translations/qscintilla_cs.qm
%lang(de) %{_datadir}/qt6/translations/qscintilla_de.qm
%lang(es) %{_datadir}/qt6/translations/qscintilla_es.qm
%lang(fr) %{_datadir}/qt6/translations/qscintilla_fr.qm
%lang(pt_BR) %{_datadir}/qt6/translations/qscintilla_pt_br.qm
%dir %{_datadir}/qt6/qsci
%dir %{_datadir}/qt6/qsci/api
%dir %{_datadir}/qt6/qsci/api/python
%{_datadir}/qt6/qsci/api/python/Python-*.api
%{_datadir}/qt6/qsci/PyQt6-QScintilla.api

%files qt6-devel
%defattr(644,root,root,755)
%{_libdir}/libqscintilla2_qt6.so
%{_includedir}/qt6/Qsci
%{_libdir}/qt6/mkspecs/features/qscintilla2.prf

%files -n Qt6Designer-plugin-%{name}
%defattr(644,root,root,755)
%{_libdir}/qt6/plugins/designer/libqscintillaplugin.so

%files -n python3-PyQt6-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt6/Qsci.abi3.so
%{py3_sitedir}/pyqt6_qscintilla-%{version}.dist-info
%{py3_sitedir}/PyQt6/Qsci.pyi

%files -n python3-PyQt6-%{name}-devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt6/bindings/Qsci
