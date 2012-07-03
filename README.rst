TIFFfile
========

Read and write image data from and to TIFF files.

Image and meta-data can be read from TIFF, BigTIFF, OME-TIFF, STK, LSM, NIH,
and FluoView files. Only a subset of the TIFF specification is supported,
mainly uncompressed and losslessly compressed 2**(0 to 6) bit integer,
16, 32 and 64-bit float, grayscale and RGB(A) images, which are commonly
used in bio-scientific imaging. Specifically, reading JPEG or CCITT
compressed image data is not implemented. Only primary info records are
read for STK, FluoView, and NIH image formats.

TIFF, the Tagged Image File Format, is under the control of Adobe Systems.
BigTIFF allows for files greater than 4 GB. STK, LSM, FluoView, and OME-TIFF
are custom extensions defined by MetaMorph, Carl Zeiss MicroImaging,
Olympus, and the Open Microscopy Environment consortium respectively.

The API is not stable yet and might change between revisions.
Tested on little-endian platforms only.

Please Note
-----------

This github project is clone of the tifffile.py_ script, hosted here as a 
package to be used with ``zc.buildout`` with an aim to publish to PyPI for 
use by others.

Requirements
------------

* CPython_ 2.7 or 3.2 
* Numpy_ 1.6 
* Matplotlib_ 1.1 (optional for plotting)
* tifffile.c_ 2012.01.01 (optional for faster decoding of PackBits and LZW encoded strings)

Example
-------

::

    >>> from tifffile import TIFFfile

    >>> data = numpy.random.rand(301, 219)
    >>> imsave('temp.tif', data)
    >>> image = imread('temp.tif')
    >>> assert numpy.all(image == data)

    >>> tif = TIFFfile('test.tif')
    >>> images = tif.asarray()
    >>> image0 = tif[0].asarray()
    >>> for page in tif:
    ...     for tag in page.tags.values():
    ...         t = tag.name, tag.value
    ...     image = page.asarray()
    ...     if page.is_rgb: pass
    ...     if page.is_palette:
    ...         t = page.color_map
    ...     if page.is_stk:
    ...         t = page.mm_uic_tags.number_planes
    ...     if page.is_lsm:
    ...         t = page.cz_lsm_info
    >>> tif.close()

.. _tifffile.py: http://www.lfd.uci.edu/~gohlke/code/tifffile.py.html
.. _CPython: http://www.python.org
.. _Numpy: http://numpy.scipy.org
.. _Matplotlib: http://matplotlib.sourceforge.net
.. _tifffile.c: http://www.lfd.uci.edu/~gohlke/
