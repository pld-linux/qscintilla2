#
# TODO:
# - fix building with qscintilla2(-devel) installed, remove BC
#   - how to successfully prepend -I../Qt4Qt5 before system qt include in qmake?
# - QScintilla2 for Qt3 (does it make any sense nowadays?)
#
# Conditonal build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	qt4	# Qt4 library and modules
%bcond_without	qt5	# Qt5 library and modules

%define		scintilla_ver	3.3.6
%define		sip_ver		4.16
%define		pyqt4_ver	4.8.2
%define		pyqt5_ver	5.0
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt
Name:		qscintilla2
Version:	2.9.1
Release:	3
License:	GPL v3
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/pyqt/QScintilla-gpl-%{version}.tar.gz
# Source0-md5:	38e6248cb970adf6d05aea7d94f1288e
Patch0:		%{name}-internal_build.patch
Patch1:		%{name}-multiqt.patch
Patch2:		%{name}-make.patch
Patch3:		%{name}-outoftree.patch
Patch4:		%{name}-qt5.patch
Patch5:		%{name}-link.patch
Patch6:		python-install.patch
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/
%if %{with python2}
BuildRequires:	python-sip-devel >= 2:%{sip_ver}
%endif
%if %{with python3}
BuildRequires:	python3-sip-devel >= 2:%{sip_ver}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.558
%if %{with qt4}
BuildRequires:	QtDesigner-devel >= 4.8
BuildRequires:	QtGui-devel >= 4.8
BuildRequires:	qt4-build >= 4.8
BuildRequires:	qt4-qmake >= 4.8
BuildRequires:	sip-PyQt4 >= %{pyqt4_ver}
%if %{with python2}
BuildRequires:	python-PyQt4 >= %{pyqt4_ver}
%endif
%if %{with python3}
BuildRequires:	python3-PyQt4 >= %{pyqt4_ver}
%endif
%endif
%if %{with qt5}
BuildRequires:	Qt5Designer-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5PrintSupport-devel >= 5
BuildRequires:	Qt5UiTools-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	sip-PyQt5 >= %{pyqt5_ver}
%if %{with python2}
BuildRequires:	python-PyQt5 >= %{pyqt5_ver}
%endif
%if %{with python3}
BuildRequires:	python3-PyQt5 >= %{pyqt5_ver}
%endif
%endif
BuildConflicts:	qscintilla2-devel < %{version}
%{?with_qt4:BuildConflicts:	qscintilla2-qt4-devel < %{version}}
%{?with_qt5:BuildConflicts:	qscintilla2-qt5-devel < %{version}}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
QScintilla2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki QScintilla2.

%package qt4
Summary:	QScintilla2 - a port to Qt 4 of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt 4
Group:		X11/Libraries
%ifarch %{x8664} ppc64 s390x sparc64
Provides:	libqscintilla2.so.11()(64bit)
%else
Provides:	libqscintilla2.so.11
%endif
Obsoletes:	qscintilla2 < 2.8.4

%description qt4
QScintilla2 is a port to Qt of the Scintilla editing component.
This version of QScintilla is based on Scintilla v%{scintilla_ver}.

This package contains the Qt 4 port.

%description qt4 -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt.
Ta wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

Ten pakiet zawiera port Qt 4.

%package qt4-devel
Summary:	Development files for the QScintilla2 Qt 4 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki QScintilla2 dla Qt 4
Group:		X11/Development/Libraries
Requires:	%{name}-qt4 = %{version}-%{release}
Requires:	QtGui-devel >= 4
Obsoletes:	qscintilla2-devel < 2.8.4

%description qt4-devel
This package contains the header files necessary to develop
applications using QScintilla2 for Qt 4.

%description qt4-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem komponentu QScintilla2 dla Qt 4.

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

%package -n sip-PyQt4-%{name}
Summary:	Python bindings for the QScintilla2 - SIP development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne SIP
Group:		Development/Languages/Python
Requires:	sip-PyQt4 >= %{pyqt4_ver}
Obsoletes:	python-qscintilla2-devel < 2.8.4

%description -n sip-PyQt4-%{name}
Python bindings for the QScintilla2 - SIP development files.

%description -n sip-PyQt4-%{name} -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
SIP.

%package -n python-PyQt4-%{name}
Summary:	Python 2 bindings for the QScintilla2 (PyQt4 version)
Summary(pl.UTF-8):	Wiązania Pythona 2 dla komponentu QScintilla2 (wersja dla PyQt4)
Group:		Libraries/Python
Requires:	%{name}-qt4 = %{version}-%{release}
%requires_ge	python-PyQt4
Obsoletes:	python-qscintilla2 < 2.8.4

%description -n python-PyQt4-%{name}
Python 2 bindings for the QScintilla2 (PyQt4 version).

%description -n python-PyQt4-%{name} -l pl.UTF-8
Wiązania Pythona 2 dla komponentu QScintilla2 (wersja dla PyQt4).

%package -n python3-PyQt4-%{name}
Summary:	Python 3 bindings for the QScintilla2 (PyQt4 version)
Summary(pl.UTF-8):	Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt4)
Group:		Libraries/Python
Requires:	%{name}-qt4 = %{version}-%{release}
%requires_ge	python3-PyQt4

%description -n python3-PyQt4-%{name}
Python 3 bindings for the QScintilla2 (PyQt4 version).

%description -n python3-PyQt4-%{name} -l pl.UTF-8
Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt4).

%package qt5
Summary:	QScintilla2 - a port to Qt 5 of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt 5
Group:		X11/Libraries

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

%description -n Qt5Designer-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances
to be included in GUI designs just like any other Qt widget.

This package contains the Qt 5 version.

%description -n Qt5Designer-plugin-%{name} -l pl.UTF-8
Wtyczka WScintilla2 dla Qt Designera pozwalająca na włączanie
instancji QScintilli w projekty GUI w ten sam sposób, co inne widgety
Qt.

Ten pakiet zawiera wersję dla Qt 5.

%package -n sip-PyQt5-%{name}
Summary:	Python bindings for the QScintilla2 - SIP development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne SIP
Group:		Development/Languages/Python
Requires:	sip-PyQt5 >= %{pyqt5_ver}

%description -n sip-PyQt5-%{name}
Python bindings for the QScintilla2 - SIP development files.

%description -n sip-PyQt5-%{name} -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
SIP.

%package -n python-PyQt5-%{name}
Summary:	Python 2 bindings for the QScintilla2 (PyQt5 version)
Summary(pl.UTF-8):	Wiązania Pythona 2 dla komponentu QScintilla2 (wersja dla PyQt5)
Group:		Libraries/Python
Requires:	%{name}-qt5 = %{version}-%{release}
%requires_ge	python-PyQt5

%description -n python-PyQt5-%{name}
Python 2 bindings for the QScintilla2 (PyQt5 version).

%description -n python-PyQt5-%{name} -l pl.UTF-8
Wiązania Pythona 2 dla komponentu QScintilla2 (wersja dla PyQt5).

%package -n python3-PyQt5-%{name}
Summary:	Python 3 bindings for the QScintilla2 (PyQt5 version)
Summary(pl.UTF-8):	Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt5)
Group:		Libraries/Python
Requires:	%{name}-qt5 = %{version}-%{release}
%requires_ge	python3-PyQt5

%description -n python3-PyQt5-%{name}
Python 3 bindings for the QScintilla2 (PyQt5 version).

%description -n python3-PyQt5-%{name} -l pl.UTF-8
Wiązania Pythona 3 dla komponentu QScintilla2 (wersja dla PyQt5).

%prep
%setup -q -n QScintilla-gpl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
for qt in %{?with_qt4:qt4} %{?with_qt5:qt5} ; do
install -d build-${qt}/{Qt4Qt5,designer-Qt4Qt5,Python2,Python3}
cd build-${qt}/Qt4Qt5
qmake-${qt} ../../Qt4Qt5/qscintilla.pro \
	$(test "$qt" = "qt4" || echo QMAKE_MKSPECS=%{_libdir}/$qt/mkspecs)
%{__make}
cd ../designer-Qt4Qt5
qmake-${qt} ../../designer-Qt4Qt5/designer.pro
%{__make}
cd ..

%if %{with python2}
cd Python2
# setup PATH to get proper qmake
# pass --apidir because configure.py default is inconsistent with sources (no /qsci subdir)
PATH=%{_libdir}/${qt}/bin:$PATH \
%{__python} ../../Python/configure.py \
	--verbose \
	-c -j 3 \
	-n ../../Qt4Qt5 \
	-o ../Qt4Qt5 \
	--apidir=%{_datadir}/${qt}/qsci \
	--pyqt=PyQt${qt#qt}
%{__make}
cd ..
%endif
%if %{with python3}
cd Python3
PATH=%{_libdir}/${qt}/bin:$PATH \
%{__python3} ../../Python/configure.py \
	--verbose \
	-c -j 3 \
	-n ../../Qt4Qt5 \
	-o ../Qt4Qt5 \
	--apidir=%{_datadir}/${qt}/qsci \
	--pyqt=PyQt${qt#qt}
%{__make}
cd ..
%endif
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT

for qt in %{?with_qt4:qt4} %{?with_qt5:qt5} ; do
%{__make} -C build-${qt}/Qt4Qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -C build-${qt}/designer-Qt4Qt5 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%if %{with python3}
%{__make} -C build-${qt}/Python3 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif
%if %{with python2}
%{__make} -C build-${qt}/Python2 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%endif
done

# unnecessary symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqscintilla2*.so.12.0

%if %{with qt4}
# move Qt4 translations to PLD-specific directory scheme
for file in $RPM_BUILD_ROOT%{_datadir}/locale/*.qm
do
	lang=`echo $file | sed -r 's:.*/[a-zA-Z]*_(.*).qm:\1:'`
	[ "$lang" == "pt_br" ] && lang=pt_BR
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	%{__mv} $file $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/qscintilla2.qm
done

# compatibility symlinks
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libqscintilla2-qt4.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libqscintilla2.so.11
ln -sf $(basename $RPM_BUILD_ROOT%{_libdir}/libqscintilla2-qt4.so.*.*.*) $RPM_BUILD_ROOT%{_libdir}/libqscintilla2.so
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	qt4 -p /sbin/ldconfig
%postun	qt4 -p /sbin/ldconfig

%post	qt5 -p /sbin/ldconfig
%postun	qt5 -p /sbin/ldconfig

%files apidocs
%defattr(644,root,root,755)
%doc doc/{Scintilla,html-Qt4Qt5}

%if %{with qt4}
%files qt4
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla2-qt4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqscintilla2-qt4.so.12
# compatibility symlink
%attr(755,root,root) %{_libdir}/libqscintilla2.so.11
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qscintilla2.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla2.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/qscintilla2.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qscintilla2.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/qscintilla2.qm
%dir %{_datadir}/qt4/qsci
%dir %{_datadir}/qt4/qsci/api
%dir %{_datadir}/qt4/qsci/api/python
%{_datadir}/qt4/qsci/api/python/Python-*.api
%{_datadir}/qt4/qsci/api/python/QScintilla2.api

%files qt4-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqscintilla2-qt4.so
# compatibility symlink
%attr(755,root,root) %{_libdir}/libqscintilla2.so
%{_includedir}/qt4/Qsci
%{_datadir}/qt4/mkspecs/features/qscintilla2.prf

%files -n QtDesigner-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libqscintillaplugin.so

%files -n sip-PyQt4-%{name}
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4/Qsci

%if %{with python2}
%files -n python-PyQt4-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/Qsci.so
%endif

%if %{with python3}
%files -n python3-PyQt4-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt4/Qsci.so
%endif
%endif

%if %{with qt5}
%files qt5
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla2-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqscintilla2-qt5.so.12
%lang(cs) %{_datadir}/qt5/translations/qscintilla_cs.qm
%lang(de) %{_datadir}/qt5/translations/qscintilla_de.qm
%lang(es) %{_datadir}/qt5/translations/qscintilla_es.qm
%lang(fr) %{_datadir}/qt5/translations/qscintilla_fr.qm
%lang(pt_BR) %{_datadir}/qt5/translations/qscintilla_pt_br.qm
%dir %{_datadir}/qt5/qsci
%dir %{_datadir}/qt5/qsci/api
%dir %{_datadir}/qt5/qsci/api/python
%{_datadir}/qt5/qsci/api/python/Python-*.api
%{_datadir}/qt5/qsci/api/python/QScintilla2.api

%files qt5-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqscintilla2-qt5.so
%{_includedir}/qt5/Qsci
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

%files -n Qt5Designer-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/libqscintillaplugin.so

%files -n sip-PyQt5-%{name}
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt5/Qsci

%if %{with python2}
%files -n python-PyQt5-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt5/Qsci.so
%endif

%if %{with python3}
%files -n python3-PyQt5-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/PyQt5/Qsci.so
%endif
%endif
