Summary:	Networked, team-based, 2D shooter
Summary(pl.UTF-8):	Sieciowa strzelanka 2D
Name:		legesmotus
Version:	0.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/legesmotus/%{name}-%{version}.tar.gz
# Source0-md5:	9ce454f8482942fd5dd0d9209add53b9
Patch0:		%{name}-flags.patch
Patch1:		%{name}-desktop.patch
URL:		http://legesmotus.cs.brown.edu/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libstdc++-devel
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Leges Motus is a networked, team-based, 2D shooter set in
zero-gravity. Using only the force from jumping off of walls and the
recoil from their guns, players must travel across the arena to lower
their opponent's gate.

%description -l pl.UTF-8
Leges Motus to sieciowa strzelanka w 2D, której akcja toczy się w
świecie pozbawionym grawitacji. Zadaniem gracza, poruszającego się
wyłącznie za pomocą skoków i siły wystrzałów, jest przemierzanie
planszy aby niszcyć bramy przeciwników.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix="%{_prefix}"

%{__make} \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	OLDFLAGS="%{rpmldflags}" \
	LIBS_GL="-lGL" \
	XDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	MANDIR=%{_mandir} \
	XDIR=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

install data/sprites/blue_head32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/legesmotus
%{_mandir}/man6/*.6*
%{_desktopdir}/legesmotus.desktop
%{_pixmapsdir}/legesmotus.png
%{_iconsdir}/hicolor/256x256/legesmotus.png
