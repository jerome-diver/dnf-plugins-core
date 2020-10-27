# -*- coding: utf-8 -*-
#
# dnf-plugins-core documentation build configuration file, created by
# sphinx-quickstart on Mon May  5 18:07:07 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import codecs
import sys
import os
import os.path

_dirname = os.path.dirname(__file__)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, _dirname)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['rhbug']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'dnf-plugins-core'
copyright = u'2014, Red Hat, Licensed under GPLv2+'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

def version_readout():
    fn = os.path.join(_dirname, '../dnf-plugins-core.spec')
    with codecs.open(fn, "r", "utf-8") as f:
        for line in f.readlines():
            if line.startswith('Version:'):
                return line.split(':')[1].strip()

version = '%s' % version_readout()
# The full version, including alpha/beta/rc tags.
release = '%s-1' % version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']
if sys.version_info[0] > 2:
    exclude_patterns.append('migrate.rst')

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'dnf-plugins-coredoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'dnf-plugins-core.tex', u'dnf-plugins-core Documentation',
   u'Tim Lauridsen', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

AUTHORS=[u'See AUTHORS in your Core DNF Plugins distribution']

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('builddep', 'dnf-builddep', u'DNF builddep Plugin', AUTHORS, 8),
    ('changelog', 'dnf-changelog', u'DNF changelog Plugin', AUTHORS, 8),
    ('config_manager', 'dnf-config-manager', u'DNF config-manager Plugin', AUTHORS, 8),
    ('copr', 'dnf-copr', u'DNF copr Plugin', AUTHORS, 8),
    ('debug', 'dnf-debug', u'DNF debug Plugin', AUTHORS, 8),
    ('debuginfo-install', 'dnf-debuginfo-install', u'DNF debuginfo-install Plugin', AUTHORS, 8),
    ('download', 'dnf-download', u'DNF download Plugin', AUTHORS, 8),
    ('generate_completion_cache', 'dnf-generate_completion_cache',
        u'DNF generate_completion_cache Plugin', AUTHORS, 8),
    ('groups-manager', 'dnf-groups-manager', u'DNF groups-manager Plugin', AUTHORS, 8),
    ('leaves', 'dnf-leaves', u'DNF leaves Plugin', AUTHORS, 8),
    ('local', 'dnf-local', u'DNF local Plugin', AUTHORS, 8),
    ('needs_restarting', 'dnf-needs-restarting', u'DNF needs_restarting Plugin', AUTHORS, 8),
    ('repoclosure', 'dnf-repoclosure', u'DNF repoclosure Plugin', AUTHORS, 8),
    ('repodiff', 'dnf-repodiff', u'DNF repodiff Plugin', AUTHORS, 8),
    ('repograph', 'dnf-repograph', u'DNF repograph Plugin', AUTHORS, 8),
    ('repomanage', 'dnf-repomanage', u'DNF repomanage Plugin', AUTHORS, 8),
    ('reposync', 'dnf-reposync', u'DNF reposync Plugin', AUTHORS, 8),
    ('post-transaction-actions', 'dnf-post-transaction-actions',
     u'DNF post transaction actions Plugin', AUTHORS, 8),
    ('show-leaves', 'dnf-show-leaves', u'DNF show-leaves Plugin', AUTHORS, 8),
    ('versionlock', 'dnf-versionlock', u'DNF versionlock Plugin', AUTHORS, 8),

    # yum3 compatible layer for manpages
    ('copr', 'yum-copr', u'redirecting to DNF copr Plugin', AUTHORS, 8),
    ('debuginfo-install', 'debuginfo-install', u'redirecting to DNF debuginfo-install Plugin',
     AUTHORS, 1),
    ('groups-manager', 'yum-groups-manager', u'redirecting to DNF groups-manager Plugin', AUTHORS, 1),
    ('needs_restarting', 'needs-restarting', u'redirecting to DNF needs-restarting Plugin',
     AUTHORS, 1),
    ('repoclosure', 'repoclosure', u'redirecting to DNF repoclosure Plugin', AUTHORS, 1),
    ('repodiff', 'repodiff', u'redirecting to DNF repodiff Plugin', AUTHORS, 1),
    ('repograph', 'repo-graph', u'redirecting to DNF repograph Plugin', AUTHORS, 1),
    ('repomanage', 'repomanage', u'redirecting to DNF repomanage Plugin', AUTHORS, 1),
    ('reposync', 'reposync', u'redirecting to DNF reposync Plugin', AUTHORS, 1),
    ('versionlock', 'yum-versionlock', u'redirecting to DNF versionlock Plugin',
     AUTHORS, 8),
    ('versionlock', 'yum-versionlock.conf', u'redirecting to DNF versionlock Plugin',
     AUTHORS, 5),
    ('builddep', 'yum-builddep', u'redirecting to DNF builddep Plugin', AUTHORS, 1),
    ('changelog', 'yum-changelog', u'redirecting to DNF changelog Plugin', AUTHORS, 1),
    ('config_manager', 'yum-config-manager', u'redirecting to DNF config-manager Plugin',
     AUTHORS, 1),
    ('debug', 'yum-debug-dump', u'redirecting to DNF debug Plugin', AUTHORS, 1),
    ('debug', 'yum-debug-restore', u'redirecting to DNF debug Plugin', AUTHORS, 1),
    ('download', 'yumdownloader', u'redirecting to DNF download Plugin', AUTHORS, 1),
    ('package-cleanup', 'package-cleanup', u'clean up locally installed, duplicate, or '
     'orphaned packages.', AUTHORS, 1),
    ('dnf-utils', 'dnf-utils', u'classic YUM utilities implemented as CLI shims on top of DNF',
     AUTHORS, 1),
    ('dnf-utils', 'yum-utils', u'classic YUM utilities implemented as CLI shims on top of DNF',
     AUTHORS, 1),
]
if sys.version_info[0] < 3:
    man_pages.append(('migrate', 'dnf-migrate', u'DNF migrate Plugin', AUTHORS, 8))

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'dnf-plugins-core', u'dnf-plugins-core Documentation',
   AUTHORS[0], 'dnf-plugins-core', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

rst_prolog = """
.. default-domain:: py
"""
