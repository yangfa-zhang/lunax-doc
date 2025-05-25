lunax.xai
=========

This module provides interpretability analysis for tree-based models using SHAP (SHapley Additive exPlanations) values.

.. py:class:: TreeExplainer(model)

    Initialize a tree model explainer.

    :param model: A trained tree model instance (XGBoost, LightGBM, or CatBoost)
    :type model: Union[xgb_reg, xgb_clf, lgbm_reg, lgbm_clf, cat_reg, cat_clf]

    **Methods:**

    .. py:method:: get_shap_values(X)

        Calculate SHAP values for the input features.

        :param X: Feature data to explain
        :type X: pandas.DataFrame
        :return: Array of SHAP values
        :rtype: numpy.ndarray

    .. py:method:: plot_summary(X, max_display=20)

        Plot a SHAP summary plot showing the impact of each feature.

        :param X: Feature data to explain
        :type X: pandas.DataFrame
        :param max_display: Maximum number of features to display
        :type max_display: int
        :return: None

    .. py:method:: plot_dependence(X, feature, interaction_index=None)

        Plot a SHAP dependence plot for a specific feature.

        :param X: Feature data to explain
        :type X: pandas.DataFrame
        :param feature: Name of the feature to analyze
        :type feature: str
        :param interaction_index: Name of the interaction feature (optional)
        :type interaction_index: Optional[str]
        :return: None

    .. py:method:: plot_force(X, index=0)

        Plot a SHAP force plot for a single prediction.

        :param X: Feature data to explain
        :type X: pandas.DataFrame
        :param index: Index of the sample to explain
        :type index: int
        :return: None

    .. py:method:: get_feature_importance(X, print_table=True)

        Get feature importance based on SHAP values.

        :param X: Feature data to explain
        :type X: pandas.DataFrame
        :param print_table: Whether to print a formatted table
        :type print_table: bool
        :return: Series of feature importance values
        :rtype: pandas.Series

    **Features:**

    - Supports both regression and classification models from XGBoost, LightGBM, and CatBoost
    - For classification models, SHAP values are calculated for the positive class (class 1)
    - The summary plot uses blue/red coloring to indicate feature values (blue = low, red = high)
    - Feature importance is calculated as the mean absolute SHAP value for each feature

    **Example Usage:**

    .. code-block:: python

        from lunax.models import xgb_reg
        from lunax.xai import TreeExplainer
        import pandas as pd

        # Prepare your data
        X_train = pd.DataFrame(...)
        y_train = pd.Series(...)
        X_test = pd.DataFrame(...)

        # Train a model
        model = xgb_reg()
        model.fit(X_train, y_train)

        # Initialize explainer
        explainer = TreeExplainer(model)

        # Get and print feature importance
        importance = explainer.get_feature_importance(X_test)

        # Generate various explanation plots
        explainer.plot_summary(X_test)
        explainer.plot_dependence(X_test, feature='most_important_feature')
        explainer.plot_force(X_test, index=0)
