Summary:	The metapackages for PLD
Summary(pl.UTF-8):	Metapakiety dla PLD
Name:		task
Version:	20040214
Release:	2
License:	GPL
Group:		Base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Metapackages for PLD.

%description -l pl.UTF-8
Metapakiety dla PLD.

%package gui-kde
Summary:	KDE metapackage for PLD
Summary(pl.UTF-8):	Metapakiet z KDE dla PLD
Group:		X11/Window Managers
Version:	3.2.0
Release:	2

%description gui-kde
This metapackage will install all KDE packages in PLD (even those that
require additional not really useful for most users packages like
wireless-tools or run as daemons). You are welcome to remove non needed
packages after the installation.

%description gui-kde -l pl.UTF-8
Ten metapakiet zainstaluje wszystkie pakiety KDE, nawet te, które
wymagają dodatkowych, nieprzydatnych dla większości użytkowników,
pakietów jak wireless-tools lub działają jako demony). Niepotrzebne
pakiety można usunąć po instalacji.

%prep

%clean
rm -rf $RPM_BUILD_ROOT

%files gui-kde
%defattr(644,root,root,755)
