Summary:	Tool for creating converters from dbf files to PGSQL commands
Summary(pl.UTF-8):	Narzędzie do tworzenia konwerterów plików dbf na instrukcje PGSQL
Name:		dbf2pos
Version:	0.1.4
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://www.mat.uni.torun.pl/~jerzy/wegorz/%{name}-%{version}.tar.gz
# Source0-md5:	4eb86e767495b96e72200a5181a8e20f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbf2pos is a little tool that will display dBase III and IV files. You
can also use it to convert your old .dbf files for further use with
Unix.

%description -l pl.UTF-8
dbf2pos jest małym programem wyświetlającym zawartość plików dBase III
i IV. Można go wykorzystać do konwersji starych plików .dbf do
wykorzystania pod Uniksem.

%package expdbflib
Summary:	dbf2pos library
Summary(pl.UTF-8):	Biblioteka dbf2pos
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description expdbflib
dbf2pos library.

%description expdbflib -l pl.UTF-8
Biblioteka dbf2pos.

%prep
%setup -q

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name},%{_includedir},%{_libdir}}
install dbf2pos	$RPM_BUILD_ROOT%{_bindir}
install *.d2p	$RPM_BUILD_ROOT%{_examplesdir}/%{name}
install expdbflib/*.h	$RPM_BUILD_ROOT%{_includedir}
install expdbflib/*.a	$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.polish README.english TODO CREDITS CHANGES
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}

%files expdbflib
%defattr(644,root,root,755)
%{_includedir}/data.h
%{_includedir}/dbf.h
%{_includedir}/defs.h
%{_includedir}/global.h
%{_libdir}/*.a
