UI Translation
==============


This module aims to easly translate Odoo or change terms from where you are,
`Ctrl` + `Click` on any string in the application to translate it!

Usage
-----

* Make sure your log user use the translated language (using preferences)
* Go to `Synchronize Terms` in Settings > Translations > Application Terms menu
  to generate ir.translation recrods to translate, this avoid to get headeak to
  collect extra data.
* `Ctrl` + `Click` on any string you want to translate

TODO
----

* Do not releoad the entire Page, what should be nice is to get the result from
  the validate on close wizard and only change the clicked label.
* When it's a label field, display its associated help message.

