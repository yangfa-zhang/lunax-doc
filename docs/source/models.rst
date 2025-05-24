lunax.models
==========

This module contains wrapper classes for various tree models, including regression and classification models from XGBoost, LightGBM, and CatBoost.

XGBoost Models
-------------

.. py:class:: xgb_reg(params: Optional[Dict] = None)

   XGBoost regression model wrapper class.

   :param params: Dictionary of XGBoost model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted values

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics

.. py:class:: xgb_clf(params: Optional[Dict] = None)

   XGBoost classification model wrapper class.

   :param params: Dictionary of XGBoost model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted labels

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      Predict class probabilities.

      :param X: Feature data
      :return: Predicted probabilities

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics

LightGBM Models
--------------

.. py:class:: lgbm_reg(params: Optional[Dict] = None)

   LightGBM regression model wrapper class.

   :param params: Dictionary of LightGBM model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted values

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics

.. py:class:: lgbm_clf(params: Optional[Dict] = None)

   LightGBM classification model wrapper class.

   :param params: Dictionary of LightGBM model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted labels

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      Predict class probabilities.

      :param X: Feature data
      :return: Predicted probabilities

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics

CatBoost Models
--------------

.. py:class:: cat_reg(params: Optional[Dict] = None)

   CatBoost regression model wrapper class.

   :param params: Dictionary of CatBoost model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted values

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics

.. py:class:: cat_clf(params: Optional[Dict] = None)

   CatBoost classification model wrapper class.

   :param params: Dictionary of CatBoost model hyperparameters
   :type params: Dict, optional

   .. py:method:: fit(X: pd.DataFrame, y: pd.Series, k_fold: Optional[int] = None) -> None

      Train the model with optional k-fold cross validation.

      :param X: Feature data
      :param y: Target variable
      :param k_fold: Number of folds for cross validation, default is None (no cross validation)

   .. py:method:: predict(X: pd.DataFrame) -> np.ndarray

      Make predictions on new data.

      :param X: Feature data
      :return: Predicted labels

   .. py:method:: predict_proba(X: pd.DataFrame) -> np.ndarray

      Predict class probabilities.

      :param X: Feature data
      :return: Predicted probabilities

   .. py:method:: evaluate(X: pd.DataFrame, y: pd.Series, log_info: bool = True) -> Dict[str, float]

      Evaluate model performance.

      :param X: Feature data
      :param y: True labels
      :param log_info: Whether to print evaluation information
      :return: Dictionary of evaluation metrics