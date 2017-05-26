# ppgr (Python Piped GRapher)

## Examples
`ping -i 0.5 8.8.8.8 | sed -run 's/.*icmp_seq=([0-9]+).*time=([0-9.]+).*/\1 \2/p' | python -m ppgr --min-y 0`

## TODO
* Fix flickering
* More and better documentation
* Colors
* Running average
* Lines between points
* Histograms
* Bar graphs?
* Labels
    * each data set (if using colors)
    * x and y axes
* Basic statistics
    * min
    * max
    * avg
    * med
    * mean
