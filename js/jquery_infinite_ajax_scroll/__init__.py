from fanstatic import (
    Library,
    Resource,
)

library = Library('jquery_infinite_ajax_scroll', 'resources')

jquery_infinite_ajax_scroll = Resource(library,
                              'jquery.ias.js',
                              minified='jquery.ias.min.js')
jquery_infinite_ajax_scroll_css = Resource(library,
                              'css/jquery.ias.css')
