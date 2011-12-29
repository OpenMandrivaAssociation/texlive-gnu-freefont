# revision 19836
# category Package
# catalog-ctan /fonts/gnu-freefont
# catalog-date 2010-09-21 17:25:45 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-gnu-freefont
Version:	20100921
Release:	1
Summary:	A Unicode font, with rather wide coverage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gnu-freefont
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of outline (i.e. OpenType) fonts
covering as much as possible of the Unicode character set. The
set consists of three typefaces: one monospaced and two
proportional (one with uniform and one with modulated stroke).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMono.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoBold.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoBoldOblique.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeMonoOblique.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSans.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansBold.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansBoldOblique.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSansOblique.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerif.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifBold.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifBoldItalic.otf
%{_texmfdistdir}/fonts/opentype/public/gnu-freefont/FreeSerifItalic.otf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMono.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoBold.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoBoldOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeMonoOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSans.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansBold.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansBoldOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSansOblique.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerif.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifBold.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifBoldItalic.ttf
%{_texmfdistdir}/fonts/truetype/public/gnu-freefont/FreeSerifItalic.ttf
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/AUTHORS
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/COPYING
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/CREDITS
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/INSTALL
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/README
#- source
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeMono.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeMonoBold.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeMonoBoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeMonoOblique.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSans.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSansBold.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSansBoldOblique.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSansOblique.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSerif.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSerifBold.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSerifBoldItalic.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/FreeSerifItalic.sfd
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/Malayalam.sfd

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
