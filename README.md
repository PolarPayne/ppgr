# ppgr (Python Piped GRapher)

## Installing
`ppgr` is available through pip, installation is as easy as `pip install ppgr`.

Although `ppgr` is currently only tested with Python 3.5 on Ubuntu 16.04, but it should work on all
machines that have a relatively new version of Python 3 and a sane-ish terminal emulator.

*DO NOT* expect the APIs (CLI or otherwise) to be stable during the 0.x.x versions.
I will follow semantic versioning to at least some degree.

## Examples
`ping -i 0.5 8.8.8.8 | sed -run 's/.*icmp_seq=([0-9]+).*time=([0-9.]+).*/\1 \2/p' | ppgr --min-y 0`

## Contributing
All contributions are greatly appreciated. If you find any bugs or errors, or would simply like to
see some feature, please create an issue in GitHub. I will also accept sane pull requests.

## TODO
(in a somewhat priority order)

* Fix flickering
* More and better documentation
* Labels
    * x and y axes
    * each data set (if using colors)
* Colors
    * for points (although it won't be perfect since there are up to 8 points per characters
    * background
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
