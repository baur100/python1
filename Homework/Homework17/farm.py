class Farm:
    def __init__(self, farmname, tractors, fields, workers, acres ):
        self._farmname = farmname
        self._tractors = tractors
        self._fields = fields
        self._workers = workers
        self._acres = acres

    def __repr__(self):
        return f" {self._farmname} have {self._tractors} tractors, {self._fields} fields {self._workers} workers and {self._acres} acres of land"

    def __add__(self, other):
        return Farm(f"all farms together ", self._tractors + other._tractors, self._fields + other._fields,
                    self._workers + other._workers, self._acres + other._acres)

    def __len__(self):
        return self._fields



