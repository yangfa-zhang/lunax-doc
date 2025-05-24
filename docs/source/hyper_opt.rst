lunax.hyper_opt 
===========================

This module provides hyperparameter optimization functionality using Optuna framework for various tree-based models.

Classes
-------

.. py:class:: OptunaTuner(BaseTuner)

   A hyperparameter tuning class using Optuna framework.

   :param param_space: Dictionary defining the parameter search space
   :type param_space: Dict[str, Tuple], optional
   :param n_trials: Number of optimization trials
   :type n_trials: int
   :param model_class: Type of model to optimize
   :type model_class: str
   :param metric_name: Name of the evaluation metric
   :type metric_name: str, optional
   :param timeout: Maximum optimization time in seconds
   :type timeout: int, optional

   **Parameter Space Format:**

   .. code-block:: python

      {
          'param_name': ('param_type', low, high),
          # Example:
          'max_depth': ('int', 3, 10),
          'learning_rate': ('float', 0.01, 0.3),
          'booster': ('categorical', ['gbtree', 'gblinear'])
      }

   **Supported Models:**

   - XGBoost: 'XGBRegressor', 'XGBClassifier'
   - LightGBM: 'LGBMRegressor', 'LGBMClassifier'
   - CatBoost: 'CatRegressor', 'CatClassifier'

   **Methods:**

   .. py:method:: optimize(X_train: pd.DataFrame, y_train: pd.Series, X_val: pd.DataFrame, y_val: pd.Series) -> Dict

      Perform hyperparameter optimization.

      :param X_train: Training features
      :param y_train: Training labels
      :param X_val: Validation features
      :param y_val: Validation labels
      :return: Dictionary containing optimization results
      :rtype: Dict

      Returns a dictionary with:
         - best_params: Best found parameters
         - best_value: Best metric value
         - n_trials: Number of completed trials
         - study: Complete Optuna study object

   **Supported Metrics:**

   For Regression Models:
      - 'mse': Mean Squared Error (default)
      - 'mae': Mean Absolute Error
      - 'r2': R-squared Score
      - 'rmse': Root Mean Squared Error

   For Classification Models:
      - 'f1': F1 Score (default)
      - 'accuracy': Accuracy Score
      - 'precision': Precision Score
      - 'recall': Recall Score

   **Default Parameter Ranges:**

   XGBoost Models:
      - Base Parameters:
         - booster: ['gbtree', 'gblinear']
         - eta: [0.01, 0.2]
         - lambda: [0.0, 100]
         - reg_lambda: [0, 1]
         - reg_alpha: [40, 180]

      - Tree-specific Parameters (when booster='gbtree'):
         - gamma: [1, 9]
         - subsample: [0.6, 1]
         - max_depth: [3, 18]
         - colsample_bytree: [0.5, 1]
         - min_child_weight: [0, 10]
         - grow_policy: ['depthwise', 'lossguide']

   LightGBM Models:
      - max_depth: [3, 10]
      - learning_rate: [0.01, 0.3]
      - n_estimators: [50, 1000]
      - num_leaves: [31, 127]
      - subsample: [0.5, 1]
      - colsample_bytree: [0.5, 1]
      - reg_alpha: [0, 1]
      - reg_lambda: [0, 1]

   CatBoost Models:
      - colsample_bylevel: [0.01, 0.1]
      - depth: [1, 12]
      - boosting_type: ['Ordered', 'Plain']
      - bootstrap_type: ['Bayesian', 'Bernoulli', 'MVS']
      - Additional parameters based on bootstrap_type

   **Example Usage:**

   .. code-block:: python

      from lunax.hyper_opt import OptunaTuner

      # Initialize tuner
      tuner = OptunaTuner(
          n_trials=50,
          model_class='XGBClassifier',
          metric_name='f1'
      )

      # Perform optimization
      results = tuner.optimize(X_train, y_train, X_val, y_val)

      # Get best parameters
      best_params = results['best_params']