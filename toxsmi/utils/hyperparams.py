from .wrappers import BCEIgnoreNaN

from paccmann_predictor.utils.hyperparams import LOSS_FN_FACTORY

LOSS_FN_FACTORY.update(
    {
        'binary_cross_entropy_ignore_nan_and_sum': BCEIgnoreNaN('sum'),
        'binary_cross_entropy_ignore_nan_and_mean': BCEIgnoreNaN('mean')
    }
)
