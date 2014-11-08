#
# TODO:
# - fix building with qscintilla2(-devel) installed, remove BC
#   - how to successfully prepend -I../Qt4Qt5 before system qt include in qmake?
# - QScintilla2 for Qt3 (does it make any sense nowadays?)
# - QScintilla2 for Qt5
#
# Conditonal build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	qt4	# Qt4 library and modules
%bcond_without	qt5	# Qt5 library and modules

%define		scintilla_ver	3.3.6
%define		sip_ver		4.16
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt
Name:		qscintilla2
Version:	2.8.4
Release:	1
License:	GPL v2 or GPL v3 with Riverbank GPL Exception v1.1
Group:		X11/Libraries
Source0:	http://downloads.sourceforge.net/pyqt/QScintilla-gpl-%{version}.tar.gz
# Source0-md5:	28aec903ff48ae541295a4fb9c96f8ea
Patch0:		%{name}-internal_build.patch
Patch1:		%{name}-multiqt.patch
Patch2:		%{name}-make.patch
Patch3:		%{name}-outoftree.patch
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/
%if %{with python2}
BuildRequires:	python-PyQt4-devel >= 4.8.2
BuildRequires:	python-sip-devel >= 2:%{sip_ver}
%endif
%if %{with python3}
BuildRequires:	python3-PyQt4-devel >= 4.8.2
BuildRequires:	python3-sip-devel >= 2:%{sip_ver}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.558
%if %{with qt4}
BuildRequires:	QtDesigner-devel >= 4.8
BuildRequires:	QtGui-devel >= 4.8
BuildRequires:	qt4-build >= 4.8
BuildRequires:	qt4-qmake >= 4.8
%endif
%if %{with qt5}
BuildRequires:	Qt5Designer-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
%endif
BuildConflicts:	qscintilla2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sipfilesdir	%{_datadir}/sip

%description
QScintilla2 is a port to Qt of the Scintilla editing component.
This version of QScintilla is based on Scintilla v%{scintilla_ver}.

%description -l pl.UTF-8
QScintilla2 to port komponentu edytora Scintilla dla biblioteki Qt.
Ta wersja QScintilli jest oparta na Scintilli %{scintilla_ver}.

%package devel
Summary:	Development files for the QScintilla2
Summary(pl.UTF-8):	Pliki nagłówkowe dla komponentu QScintilla2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui-devel

%description devel
This package contains the header files necessary to develop
applications using QScintilla2.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do tworzenia programów z
użyciem komponentu QScintilla2.

%package -n QtDesigner-plugin-%{name}
Summary:	QScintilla2 plugin for Qt Designer
Summary(pl.UTF-8):	Wtyczka QScintilla2 dla Qt Designera
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner

%description -n QtDesigner-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances
to be included in GUI designs just like any other Qt widget.

%description -n QtDesigner-plugin-%{name} -l pl.UTF-8
Wtyczka WScintilla2 dla Qt Designera pozwalająca na włączanie
instancji QScintilli w projekty GUI w ten sam sposób, co inne widgety
Qt.

%package -n python-%{name}
Summary:	Python bindings for the QScintilla2
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%requires_ge	python-PyQt4

%description -n python-%{name}
Python bindings for the QScintilla2.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2.

%package -n python-%{name}-devel
Summary:	Python bindings for the QScintilla2 - development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
Group:		Development/Languages/Python
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-PyQt4-devel >= 4.8.2

%description -n python-%{name}-devel
Python bindings for the QScintilla2 - development files.

%description -n python-%{name}-devel -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne.

%prep
%setup -q -n QScintilla-gpl-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
for qt in %{?with_qt4:qt4} %{?with_qt5:qt5} ; do
install -d build-${qt}/{Qt4Qt5,designer-Qt4Qt5,Python2,Python3}
cd build-${qt}/Qt4Qt5
qmake-${qt} ../../Qt4Qt5/qscintilla.pro
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
	--apidir=%{_datadir}/${qt}/qsci
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
	--apidir=%{_datadir}/${qt}/qsci
%{__make}
cd ..
%endif
cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_datadir}/qt5/qsci/api

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

for file in $RPM_BUILD_ROOT%{_datadir}/locale/*.qm
do
	lang=`echo $file | sed -r 's:.*/[a-zA-Z]*_(.*).qm:\1:'`
	[ "$lang" == "pt_br" ] && lang=pt_BR
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	mv -f $file $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/qscintilla2.qm
done

# unnecessary symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libqscintilla2.so.11.3

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc GPL_EXCEPTION.TXT NEWS OPENSOURCE-NOTICE.TXT README
%attr(755,root,root) %{_libdir}/libqscintilla2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqscintilla2.so.11
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qscintilla2.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla2.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/qscintilla2.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qscintilla2.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/qscintilla2.qm
%dir %{_datadir}/qt4/qsci
%dir %{_datadir}/qt4/qsci/api
%dir %{_datadir}/qt5/qsci
%dir %{_datadir}/qt5/qsci/api

%files devel
%defattr(644,root,root,755)
%doc doc/Scintilla/*
%attr(755,root,root) %{_libdir}/libqscintilla2.so
%{_includedir}/qt4/Qsci
%{_datadir}/qt4/mkspecs/features/qscintilla2.prf

%files -n QtDesigner-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/libqscintillaplugin.so

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/Qsci.so
%dir %{_datadir}/qt4/qsci/api/python
%{_datadir}/qt4/qsci/api/python/Python-*.api
%{_datadir}/qt4/qsci/api/python/QScintilla2.api

%files -n python-%{name}-devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4/Qsci
