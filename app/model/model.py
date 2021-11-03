""" DenseNet121 Model """

from keras.applications.densenet import DenseNet121


def create_densenet() -> DenseNet121:
    """
    Returns an instance of DenseNet121 with the weights loading
    from densenet121_weights_tf_dim_ordering_tf_kernels.h5.
    """
    return DenseNet121(
        include_top=True,
        weights="model_weights/densenet121_weights_tf_dim_ordering_tf_kernels.h5",
        input_tensor=None,
        input_shape=(224, 224, 3),
        pooling=None,
    )
