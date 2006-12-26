#
# TODO:
#	- QScintilla for Qt3
#
%define		scintilla_ver	1.71
%define		_snap		20061220
Summary:	QScintilla2 - a port to Qt of the Scintilla editing component
Name:		qscintilla2
Version:	2
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://www.riverbankcomputing.com/Downloads/Snapshots/QScintilla2/QScintilla-%{scintilla_ver}-gpl-%{version}-snapshot-%{_snap}.tar.gz
# Source0-md5:	04ae80adf1f60b56c3bcc5800ec68656
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-internal_build.patch
URL:		http://www.riverbankcomputing.co.uk/qscintilla/index.php
BuildRequires:	QtDesigner-devel
BuildRequires:	QtGui-devel
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

%package devel
Summary:	Development files for the QScintilla2
Summary(pl):	Pliki nag³ówkowe dla QScintilla2
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui-devel

%description devel
This package contains the header files necessary to develop
applications using QScintilla2 - header files.

%package -n QtDesigner-plugin-%{name}
Summary:	QScintilla2 plugin for Qt Designer
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner

%description -n QtDesigner-plugin-%{name}
QScintilla2 plugin for Qt Designer that allows QScintilla instances
to be included in GUI designs just like any other Qt widget.

%package -n python-%{name}
Summary:	Python bindings for the QScintilla2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-PyQt4 >= 4.1.1

%description -n python-%{name}
Python bindings for the QScintilla2.

%package -n python-%{name}-devel
Summary:	Python bindings for the QScintilla2 - development files
Group:		Development/Languages/Python
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-PyQt4-devel >= 4.1.1

%description -n python-%{name}-devel
Python bindings for the QScintilla2 - development files.

%prep
%setup -q -n QScintilla-%{scintilla_ver}-gpl-%{version}-snapshot-%{_snap}
%patch0 -p1
%patch1 -p1

%build
cd Qt4
qt4-qmake qscintilla.pro
%{__make} \
	INSTALL_ROOT=$RPM_BUILD_ROOT
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
	LANG=`echo $file | sed -r 's:.*/[a-zA-Z]*_(.*).qm:\1:'`
	[ "$LANG" == "pt_br" ] && LANG=pt_BR
	mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$LANG/LC_MESSAGES
	mv -f $file $RPM_BUILD_ROOT%{_datadir}/locale/$LANG/LC_MESSAGES/qscintilla2.qm
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libqscintilla2.so.*.*.*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/qscintilla2.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/qscintilla2.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/qscintilla2.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/qscintilla2.qm

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
