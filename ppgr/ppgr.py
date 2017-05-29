import time
from collections import namedtuple

from .screen import Screen
from .terminal import write

Point = namedtuple("Point", ("x", "y"))


class MinMax:
    def __init__(self, min_x=None, min_y=None, max_x=None, max_y=None):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def update(self, p):
        if self.min_x is None:
            self.min_x = p.x
        if self.min_y is None:
            self.min_y = p.y

        if self.max_x is None:
            self.max_x = p.x
        if self.max_y is None:
            self.max_y = p.y

        if self.min_x > p.x:
            self.min_x = p.x
        if self.min_y > p.y:
            self.min_y = p.y

        if self.max_x < p.x:
            self.max_x = p.x
        if self.max_y < p.y:
            self.max_y = p.y

    def recalculate(self, ps):
        self.min_x = None
        self.min_y = None
        self.max_x = None
        self.max_y = None

        for p in ps:
            self.update(p)


class PPGR:
    def __init__(self, format, fail_bad_line=False, wait=None, time_scale=None, limit=None):
        self.format = format
        self.fail_bad_line = fail_bad_line
        self.limit = limit

        self.wait = wait
        if self.wait is not None:
            self.wait /= 1000

        self.time_scale = time_scale
        if self.time_scale is None:
            self.t0 = time.monotonic()

        self.ps = []
        self.screen = Screen()
        self.t = 0
        self.min_max = MinMax()

    def _prep_canvas(self, max_x=None, min_x=None, max_y=None, min_y=None):
        """preps the canvas so that it can be drawn"""

        def f(length, ma, mi):
            try:
                return length / (ma - mi)
            except (ZeroDivisionError, TypeError):
                return 1

        def g(p):
            return Point(
                (p.x - low.x) * fact.x,
                size.y - ((p.y - low.y) * fact.y))

        if min_x is None:
            min_x = self.min_max.min_x
        if min_y is None:
            min_y = self.min_max.min_y
        low = Point(min_x, min_y)

        if max_x is None:
            max_x = self.min_max.max_x
        if max_y is None:
            max_y = self.min_max.max_y
        high = Point(max_x, max_y)

        self.screen.size = None, None
        size = Point(*self.screen.size)
        fact = Point(f(size.x, high.x, low.x), f(size.y, high.y, low.y))

        for p in map(g, self.ps):
            self.screen(*p)

    def _max_min(self, many):
        """updates mins and maxes based on the last `many` points"""

        for i in range(many):
            last = self.ps[-(many)]
            self.min_max.update(last)

    def _drop_extra(self):
        """drops extra points and recalculates mins and maxes if limit is set"""

        if self.limit is None:
            return

        old_len = len(self.ps)

        # store at most limit points
        self.ps[:] = self.ps[len(self.ps) - self.limit:]

        # recalculate mins and maxs if the some items were removed
        if old_len > len(self.ps):
            self.min_max.recalculate(self.ps)

    def _update_t(self):
        if self.time_scale is None:
            self.t = time.monotonic() - self.t0
        else:
            self.t += self.time_scale

    def line(self, line):
        # TODO better error handling
        # TODO better support for --fail-bad-line
        # TODO add support for histograms (difficult?)
        f = {
            "a": lambda a: f["d"](a) if len(a) >= 2 else f["t"](a),
            "t": lambda a: Point(self.t, a.pop()),
            "d": lambda a: Point(a.pop(), a.pop())}

        _line = line

        try:
            line = list(map(float, line.strip().split()))
        except (ValueError, TypeError) as e:
            if self.fail_bad_line:
                raise Exception("bad line: {}".format(_line))
            else:
                return

        a = list(reversed(line))

        # we need to keep track of how many points are added
        many = 0
        for i in self.format:
            try:
                if i == "s":
                    a.pop()
                    continue
                self.ps.append(f[i](a))
                many += 1
            except IndexError as e:
                if self.fail_bad_line:
                    raise Exception("bad line: {} failed".format(_line))

        # keep track of mins and maxs while reading data
        # it's faster than calculcating mins and maxs everytime
        self._max_min(many)

        self._drop_extra()
        self._update_t()

    def show(self, max_x=None, min_x=None, max_y=None, min_y=None, no_animate=False, newline=False):
        self._prep_canvas(max_x, min_x, max_y, min_y)
        write(
            self.screen,
            wait=None if no_animate else self.wait,
            end="\n" if newline else "")
