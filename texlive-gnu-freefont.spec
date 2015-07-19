# revision 29349
# category Package
# catalog-ctan /fonts/gnu-freefont
# catalog-date 2012-07-05 15:28:28 +0200
# catalog-license gpl3
# catalog-version undef
Name:		texlive-gnu-freefont
Version:	20120705
Release:	10
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
Requires:	fontforge
%define __noautoreq '/usr/bin/fontforge'

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
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/BUILDING
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/COPYING
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/CREDITS
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/INSTALL
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/Makefile
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/README
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/TROUBLESHOOTING
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/USAGE
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/README-downloads.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/building.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/features.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/maintenance.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/troubleshooting.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/usage.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/notes/webfont_guidelines.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/MacTT
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/OpenType
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/TrueType
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/WOFF
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/buildutils.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/generate/buildutils.pyc
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OS2UnicodeRange
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OpenType/UnicodeRanges.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/OpenType/__init__.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/kernclasses.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/ligatureLookups.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/private_use.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/report/range_report.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/script-menu/nameBySlot.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/script-menu/unnameBySlot.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/CheckConformance.pl
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-1.lst
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-1.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-2.lst
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-2.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-3B.lst
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/MES-3B.txt
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/WGL4.lst
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/MES-Conformance/mes-list-expand.pl
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/checkGlyphNumbers.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/findBackLayers.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/isMonoMono.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/arabic_test.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/generate_arabic_shaping.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/ranges/Arabic/unicode_joining.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/test/validate.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/KerningNumerals.pl
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/fontforge-interp.sh
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/freefont-ttf.spec
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/hex_range.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/metafont/bulk_eps_import.py
%doc %{_texmfdistdir}/doc/fonts/gnu-freefont/tools/utility/special-purpose/makeBraille.py
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
%doc %{_texmfdistdir}/source/fonts/gnu-freefont/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc source %{buildroot}%{_texmfdistdir}
