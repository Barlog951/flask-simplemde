.. include:: ../README.rst


Configuration
=============

========================= =====================================================
Option                    Description
========================= =====================================================
:code:`SIMPLEMDE_JS_IIFE` If :code:`True`, the SimpleMDE loading javascript
                          will be in `IIFE`_ style.  If :code:`False`, a
                          simpler declaration will be used
:code:`SIMPLEMDE_USE_CDN` If :code:`True`, SimpleMDE's css and javascript files
                          will be served from CDN.  If :code:`False`, local
                          copies of these files will be served.  Default value
                          is :code:`True`
========================= =====================================================

.. _IIFE: https://en.wikipedia.org/wiki/Immediately-invoked_function_expression


SimpleMDE Version
=================

The bundled version of SimpleMDE is v1.10.1


API
===

.. automodule:: flask_simplemde
  :members:


Changelog
=========


Version 0.3.0
-------------

- Upgraded bundled SimpleMDE version to 1.10.1


Version 0.2
-----------

- SimpleMDE loading javascript is in IIFE style by default
- Added option to turn off the IIFE style


Version 0.1
-----------

- Initial public release
