Summary:	A Polish-English-Polish dictionary
Summary(pl.UTF-8):   Słownik polsko-angielski i angielsko-polski
Name:		sap
Version:	0.2
Release:	5
License:	GPL
Vendor:		Bohdan R. Rau <ethanak@bigfoot.com>
Group:		Applications/Dictionaries
Source0:	http://www.terravista.pt/Mussulo/1345/sap/%{name}-%{version}.tgz
# Source0-md5:	a185adfa76b0251a5a0ca16000ba5967
Patch0:		%{name}-path.patch
Patch1:		%{name}-64bit.patch
URL:		http://www.terravista.pt/Mussulo/1345/sap/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polish English / English Polish dictionary.

%description -l pl.UTF-8
Słownik polsko-angielski i angielsko-polski.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd src
%{__cc} %{rpmcflags} -o sap alt_unistd.c charfilter.c sap.c \
	-DDICTIONARIES_DIRECTORY=\"%{_datadir}/%{name}/\" \
	-DGLOBAL_SAPRC_FULLPATH=\"%{_sysconfdir}/saprc\" \
%ifarch ppc ppc64 sparc sparc64 sparcv9 s390 s390x
	-DMSB_FIRST_PROCESSOR
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_datadir}/%{name}}

> $RPM_BUILD_ROOT%{_sysconfdir}/saprc
install src/sap $RPM_BUILD_ROOT%{_bindir}
install	lib/dvp_{1,2}.dic $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README saprc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/saprc
%attr(755,root,root) %{_bindir}/sap
%{_datadir}/%{name}
