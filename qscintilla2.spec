# TODO:
# - fix building with qscintilla2(-devel) installed, remove BC
#   - how to successfully prepend -I../Qt4Qt5 before system qt include in qmake?
#
%define		scintilla_ver	3.3.6
%define		sip_ver		6.4
%define		pyqt5_ver	5.15.7
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt
Name:		qscintilla2
Version:	2.13.3
Release:	3
License:	GPL v3
Group:		X11/Libraries
Source0:	https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
# Source0-md5:	af0dab4ff9908e0d41934aff6ce2348d
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/
BuildRequires:	Qt5Designer-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	Qt5UiTools-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	python3-PyQt5 >= %{pyqt5_ver}
BuildRequires:	python3-PyQt5-devel >= %{pyqt5_ver}
BuildRequires:	qt5-build >= 5
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.558
BuildRequires:	rpm-pythonprov
BuildRequires:	sip6 >= %{sip_ver}
BuildConflicts:	qscintilla2-devel < %{version}
Obsoletes:	qscintilla2-qt4 < 2.13.3
Obsoletes:	qscintilla2-qt4-devel < 2.13.3
BuildConflicts:	qscintilla2-qt5-devel < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QScintilla2 is a port to Qt of the Scintilla editing component.
This version of QScintilla is based on Scintilla v%{scintilla_ver}.

%description -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt.
Ta wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

%package apidocs
Summary:	QScintilla2 API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki QScintilla2
Group:		Documentation
BuildArch:	noarch

%description apidocs
QScintilla2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki QScintilla2.

%package -n QtDesigner-plugin-%{name}
Summary:	QScintilla2 plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka QScintilla2 dla Qt Designera
Group:		X11/Development/Libraries
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	QtDesigner >= 4

%description -n QtDesigner-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances
to be included in GUI designs just like any other Qt widget.

This package contains the Qt 4 version.

%description -n QtDesigner-plugin-%{name} -l pl.UTF-8
Wtyczka WScintilla2 dla Qt Designera pozwalająca na włączanie
instancji QScintilli w projekty GUI w ten sam sposób, co inne widgety
Qt.

Ten pakiet zawiera wersję dla Qt 4.

%package qt5
Summary:	QScintilla2 - a port to Qt 5 of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt 5
Group:		X11/Libraries
Obsoletes:	qscintilla2-qt4 < 2.13.3

%description qt5
QScintilla2 is a port to Qt of the Scintilla editing component.
This version of QScintilla is based on Scintilla v%{scintilla_ver}.

This package contains the Qt 5 port.

%description qt5 -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt.
Ta wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

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
QScintilla2 plugin for Qt Designer that allows QScintilla instances
to be included in GUI designs just like any other Qt widget.

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
%requires_ge	python3-PyQt5
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

%prep
%setup -q -n QScintilla_src-%{version}

%build
export QMAKEFEATURES=$PWD/src/features;

install -d build-qt5/{Qt4Qt5,designer-Qt4Qt5,Python3}
cd src
qmake-qt5 qscintilla.pro QMAKE_MKSPECS=%{_libdir}/qt5/mkspecs
%{__make}

cd ../designer
qmake-qt5 designer.pro INCLUDEPATH+=../src LIBS+=-L../src QMAKE_MKSPECS=%{_libdir}/qt5/mkspecs
%{__make}

cd ../Python
#	--api-dir=%{_qt5_datadir}/qsci/api/python \
ln -s pyproject-qt5.toml pyproject.toml
LD_LIBRARY_PATH=$PWD/../src \
sip-build \
	--no-make \
	--verbose \
	--pep484-pyi \
	--qmake="%{_bindir}/qmake-qt5" \
	--api-dir=%{_datadir}/qt5/qsci \
	--qsci-include-dir=../src \
	--qsci-library-dir=../src \
	--qsci-features-dir=../src/features
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C src install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -j1 -C designer install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -j1 -C Python/build install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# unnecessary symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqscintilla2*.so.15.1

%clean
rm -rf $RPM_BUILD_ROOT

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files apidocs
%defattr(644,root,root,755)
%doc doc/{Scintilla,html}

%files qt5
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/libqscintilla2_qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqscintilla2_qt5.so.15
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
%attr(755,root,root) %{_libdir}/libqscintilla2_qt5.so
%{_includedir}/qt5/Qsci
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

%files -n Qt5Designer-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqscintillaplugin.so

%files -n python3-PyQt5-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt5/Qsci.abi3.so
%{py3_sitedir}/QScintilla-%{version}.dist-info
%{py3_sitedir}/PyQt5/Qsci.pyi

%files -n python3-PyQt5-%{name}-devel
%defattr(644,root,root,755)
%{py3_sitedir}/PyQt5/bindings/Qsci
