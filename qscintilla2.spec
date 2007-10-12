#
# TODO:
#	- QScintilla for Qt3
#
%define		main_ver	2.1
%define		scintilla_ver	1.73
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Summary(pl.UTF-8):	QScintilla2 - port komponentu edytora Scintilla dla biblioteki Qt
Name:		qscintilla2
Version:	%{main_ver}_%{scintilla_ver}
Release:	2
License:	GPL v2
Group:		X11/Libraries
Source0:	http://www.riverbankcomputing.com/Downloads/QScintilla2/QScintilla-%{scintilla_ver}-gpl-%{main_ver}.tar.gz
# Source0-md5:	13049717628391ca4db43f7ede0eeeb4
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-internal_build.patch
URL:		http://www.riverbankcomputing.co.uk/qscintilla/index.php
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtScript-devel
BuildRequires:	QtXml-devel
BuildRequires:	python-PyQt4-devel >= 4.1.1
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpm-pythonprov
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
Requires:	python-PyQt4 >= 4.1.1

%description -n python-%{name}
Python bindings for the QScintilla2.

%description -n python-%{name} -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2.

%package -n python-%{name}-devel
Summary:	Python bindings for the QScintilla2 - development files
Summary(pl.UTF-8):	Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne
Group:		Development/Languages/Python
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-PyQt4-devel >= 4.1.1

%description -n python-%{name}-devel
Python bindings for the QScintilla2 - development files.

%description -n python-%{name}-devel -l pl.UTF-8
Wiązania Pythona dla komponentu QScintilla2 - pliki programistyczne.

%prep
%setup -q -n QScintilla-%{scintilla_ver}-gpl-%{main_ver}
%patch0 -p1
%patch1 -p1

%build
cd Qt4
qt4-qmake qscintilla.pro
%{__make}
cd -

cd designer-Qt4
qt4-qmake designer.pro
%{__make}
cd -

cd Python
python configure.py \
	-c -j 3 \
	-n ../Qt4 \
	-o ../Qt4
%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Qt4 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -C designer-Qt4 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT
%{__make} -C Python install \
	DESTDIR=$RPM_BUILD_ROOT

for file in $RPM_BUILD_ROOT%{_datadir}/locale/*.qm
do
	lang=`echo $file | sed -r 's:.*/[a-zA-Z]*_(.*).qm:\1:'`
	[ "$lang" == "pt_br" ] && lang=pt_BR
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES
	mv -f $file $RPM_BUILD_ROOT%{_datadir}/locale/$lang/LC_MESSAGES/qscintilla2.qm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla2.so.*.*.*
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/qscintilla2.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla2.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qscintilla2.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/qscintilla2.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qscintilla2.qm
%{_datadir}/qt4/qsci

%files devel
%defattr(644,root,root,755)
%doc doc/Scintilla/*
%attr(755,root,root) %{_libdir}/libqscintilla2.so
%{_includedir}/qt4/Qsci

%files -n QtDesigner-plugin-%{name}
%attr(755,root,root) %{_libdir}/qt4/plugins/designer/*.so

%files -n python-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/PyQt4/*.so*

%files -n python-%{name}-devel
%defattr(644,root,root,755)
%{_sipfilesdir}/PyQt4/Qsci
