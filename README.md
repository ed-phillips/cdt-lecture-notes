# CDT lecture notes

A handout of lecture notes written in LaTeX, together with the Python code that
generates its figures. The same files live in two places:

- **GitHub:** https://github.com/ed-phillips/cdt-lecture-notes. This is where the code, the history and the pull requests are.
- **Overleaf:** https://www.overleaf.com/project/6ad4f8b2585b36f9af880940. This is where you edit and compile in the browser, and you need to be invited.

The two are kept in sync with plain git. There is no automation. The layout is
built on the [OxEngThesis](https://github.com/maurovm/thesis_template) LaTeX
class; see [TEMPLATE_README.md](TEMPLATE_README.md) for its options (fonts,
chapter styles, margins, ...).

## Ways to contribute

### 1. In Overleaf (no setup)

Ask Ed to share the Overleaf project with you, then edit as usual. Ed pulls
Overleaf edits into GitHub.

### 2. With git (and optionally a coding agent)

This is better for figures, code, or larger restructuring.

1. **Fork and clone:** fork the repo on GitHub (or ask Ed for write access), then clone it.
2. **Make your changes:** work on a branch and open a pull request against `main`.
3. **Merge:** once it's merged, Ed runs `git push`, which publishes it to Overleaf as well.

If you have write access and want to push to Overleaf directly, see
"Collaborating and the Overleaf sync" in [CLAUDE.md](CLAUDE.md) for the
one-time remote setup. You'll need access to the Overleaf project and an
Overleaf git token (Account Settings → Git integration). Overleaf's git
integration is a paid feature; the University of Oxford licence covers it.

Coding agents such as Claude Code read [CLAUDE.md](CLAUDE.md) automatically.
It covers the layout, the conventions, and what not to touch.

## Where things are

| Path | What it holds |
|---|---|
| `lecture_notes.tex` | Main document: title, author, class options, list of lectures |
| `lectures/` | One file per lecture, plus `references.bib` |
| `frontmatter/` | Title page (and optional abstract, acknowledgements, glossary) |
| `code/` | Python project that generates the figures |
| `figures/generated/` | Figure PDFs written by `code/`. These are committed so Overleaf can use them |

Everything else in the root (`oxengthesis.cls`, `sample_dphil_thesis.tex`,
`chap_*.tex`, ...) belongs to the upstream template. Please leave it unedited, so
that template updates merge cleanly.

## Common commands

Regenerate the figures (needs [uv](https://docs.astral.sh/uv/)):

```bash
cd code && uv run make-figures
```

Build the PDF locally (needs LuaLaTeX, which comes with MacTeX or TeX Live). If
you don't have it, recompile in Overleaf instead:

```bash
latexmk
```

Overleaf settings: **Compiler = LuaLaTeX**, **Main document = `lecture_notes.tex`**.
