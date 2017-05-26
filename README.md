# ppgr (Python Piped GRapher)

## Installing
`ppgr` is currently only tested with Python 3.5 on Ubuntu 16.04, but it should work on all
machines with a relatively new version of Python 3. `ppgr` is available through pip, install
it with simply `pip install ppgr`.

## Examples
`ping -i 0.5 8.8.8.8 | sed -run 's/.*icmp_seq=([0-9]+).*time=([0-9.]+).*/\1 \2/p' | ppgr --min-y 0`

## TODO
(in a somewhat priority order)

* Fix flickering
* More and better documentation
* Labels
    * x and y axes
    * each data set (if using colors)
* Colors
* Tests
* Lines between points
* Bar graphs?
* Histograms
* Running average
* Basic statistics from all points (or data sets)
    * min
    * max
    * avg
    * med
    * mean
* Support all (?) Python 3 versions
* Support Python 2.7
