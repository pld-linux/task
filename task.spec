Summary:	The metapackages for PLD
Summary(pl):	Metapakiety dla PLD.
Name:		task
Version:	20040214
Release:	1
License:	GPL
Group:		Base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metapackages for PLD.

%description -l pl
Metapakiety dla PLD.

%package gui-kde
Summary:	KDE metapackage for PLD.
Summary(pl):	Metapakiet z KDE dla PLD.
Group:		X11/Window Managers
Version:	3.2.0
Release:	1

%description gui-kde
This metapackage will install all KDE packages in PLD (even those that 
require additional not really useful for most users packages like 
wireless-tools or run as deamons). You are welcome to remove non needed 
packages after the installation.

%description gui-kde -l pl
Ten metapakiet zainstaluje wszystkie pakiety KDE, nawet te, kt�re 
wymagaj� dodatkowych, nieprzydatnych dla wi�kszo�ci u�ytkownik�w, 
pakiet�w jak wireless-tools lub dzia�aj� jako demony). Niepotrzebne 
pakiety mo�na usun�� po instalacji.

%files gui-kde

%clean
rm -rf $RPM_BUILD_ROOTclean
rm -rf $RPM_BUILD_ROOT
