# ppgr (Python Piped GRapher) [![Build Status](https://travis-ci.org/PolarPayne/ppgr.svg?branch=master)](https://travis-ci.org/PolarPayne/ppgr)

## Installing
`ppgr` is available through pip, installation is as easy as `pip install ppgr`.

`ppgr` should work with all machines that have Python 3.4 or newer and a sane-ish terminal emulator.

*DO NOT* expect the APIs (CLI or otherwise) to be stable during the 0.x.x versions.
I will follow semantic versioning to at least some degree.

## Examples
Shows really nicely with what kind of inputs `ppgr` already excels at.
`ping -i 0.5 8.8.8.8 | sed -run 's/.*icmp_seq=([0-9]+).*time=([0-9.]+).*/\1 \2/p' | ppgr --min-y 0`

Not very useful without colors/lines between points.
`bash -c "while true; do dig google.com reddit.com twitter.com | sed -run 's/.*Query time: ([0-9]+).*/\1/p' | tr '\n' ' '; echo; sleep 1; done" | ppgr --format t t t`


## Contributing
All contributions are greatly appreciated. If you find any bugs or errors, or would simply like to
see some feature, please create an issue in GitHub. I will also accept sane pull requests.

## TODO
(in a somewhat priority order)

* More and better documentation
* Tests
* Labels
    * x and y axes
    * each data set (if using colors)
* Colors
    * for points (although it won't be perfect since there are up to 8 "pixels" per characters
    * background
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
* Support and test Python 2.7 (?)
* Improve how points are drawn to screen (don't draw everythin again on every frame)
