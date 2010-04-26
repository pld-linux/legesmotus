# $Revision: 1.1 $, $
#
# TODO: pl
#
Summary:	Networked, team-based, 2D shooter
#Summary(pl.UTF-8):	-
Name:		legesmotus
Version:	0.2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/legesmotus/%{name}-%{version}.tar.gz
# Source0-md5:	f28d8e51f5e994f73b4122d4334aa04e
Patch0:		%{name}-flags.patch
URL:		http://legesmotus.cs.brown.edu/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leges Motus is a networked, team-based, 2D shooter set in
zero-gravity. Using only the force from jumping off of walls and the
recoil from their guns, players must travel across the arena to lower
their opponent's gate.

#%%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix="%{_prefix}"

%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	OLDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	MANDIR=%{_mandir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/legesmotus
%{_mandir}/man6/*.6*
