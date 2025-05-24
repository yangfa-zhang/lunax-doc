lunax.hyper_opt
=========================

This module provides hyperparameter optimization functionality using the Optuna framework.

.. py:module:: lunax.hyper_opt.optuna_tuner

.. py:class:: OptunaTuner(BaseTuner)

   Hyperparameter optimization using Optuna framework.

   :param param_space: Custom parameter search space definition
   :type param_space: Dict[str, Tuple], optional
   :param n_trials: Number of optimization trials
   :type n_trials: int
   :param model_class: Model class name to optimize
   :type model_class: str
   :param metric_name: Metric name for optimization
   :type metric_name: str, optional
   :param timeout: Maximum optimization time in seconds
   :type timeout: int, optional

   **Methods:**

   .. py:method:: optimize(X_train: pd.DataFrame, y_train: pd.Series, X_val: pd.DataFrame, y_val: pd.Series) -> Dict

      Perform hyperparameter optimization.

      :param X_train: Training features
      :param y_train: Training labels
      :param X_val: Validation features
      :param y_val: Validation labels
      :return: Optimization results dictionary
      :rtype: Dict

   **Supported Models:**

   - XGBoost:
      - XGBRegressor
      - XGBClassifier
   - LightGBM:
      - LGBMRegressor
      - LGBMClassifier
   - CatBoost:
      - CatRegressor
      - CatClassifier

   **Default Parameter Ranges:**

   XGBoost Models:
      - max_depth: [3, 18]
      - learning_rate: [0.01, 0.2]
      - n_estimators: [50, 1000]
      - min_child_weight: [0, 10]
      - subsample: [0.6, 1.0]
      - colsample_bytree: [0.5, 1.0]
      - reg_alpha: [0, 1]
      - reg_lambda: [0, 1]
      - grow_policy: ['depthwise', 'lossguide']

   LightGBM Models:
      - max_depth: [3, 10]
      - learning_rate: [0.01, 0.3]
      - n_estimators: [50, 1000]
      - num_leaves: [31, 127]
      - subsample: [0.5, 1.0]
      - colsample_bytree: [0.5, 1.0]
      - reg_alpha: [0, 1]
      - reg_lambda: [0, 1]

   CatBoost Models:
      - depth: [1, 12]
      - learning_rate: [0.01, 0.3]
      - iterations: [50, 1000]
      - l2_leaf_reg: [1, 10]
      - bootstrap_type: ['Bayesian', 'Bernoulli', 'MVS']
      - subsample: [0.5, 1.0] (for Bernoulli)
      - bagging_temperature: [0, 10] (for Bayesian)

   **Supported Metrics:**

   Regression:
      - mse (default)
      - mae
      - rmse
      - r2

   Classification:
      - f1 (default)
      - accuracy
      - precision
      - recall

   **Example Usage:**

   .. code-block:: python

      from lunax.hyper_opt import OptunaTuner

      # Basic usage
      tuner = OptunaTuner(
          n_trials=50,
          model_class='XGBClassifier',
          metric_name='f1'
      )

      # Run optimization
      results = tuner.optimize(X_train, y_train, X_val, y_val)
      best_params = results['best_params']

      # Custom parameter space
      param_space = {
          'max_depth': ('int', 3, 10),
          'learning_rate': ('float', 0.01, 0.1),
          'n_estimators': ('int', 100, 500)
      }
      tuner = OptunaTuner(param_space=param_space)