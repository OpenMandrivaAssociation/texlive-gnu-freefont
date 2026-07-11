%global tl_name gnu-freefont
%global tl_revision 68624

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Unicode font, with rather wide coverage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gnu-freefont
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gnu-freefont.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of outline (i.e. OpenType) fonts covering as
much as possible of the Unicode character set. The set consists of three
typefaces: one monospaced and two proportional (one with uniform and one
with modulated stroke).

