from pre_sliced.matrix_entities import MatrixEntity, PartitionedMatrixEntity, ExposedMatrixEntity


class Scalar(MatrixEntity, PartitionedMatrixEntity, ExposedMatrixEntity):
    def __init__(self, value: float):
        self.value = value

    def partition(self):
        return self

    def expose(self):
        return self

    def is_complete(self):
        return True

    def combine(self):
        return self

    def exposed_value(self):
        return self.value

    def repartition(self):
        return self

    def update(self, alpha: float):
        return Scalar(alpha)
